from flask import Blueprint,jsonify, request
from datetime import datetime
from project import db
from project.models import Topgearc, Project



tgcregister= Blueprint('/tgcregister',__name__)

#Api to add an entry to the TopgearC table
@tgcregister.route('/add_topgearc', methods=['POST'])
def add_topgearc():
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        employee_id = 101
    if None in (request.get_json()['pop'],request.get_json()['topID'],request.get_json()['topTitle'],request.get_json()['dateH'],request.get_json()['cert'],request.get_json()['points']):
        result = jsonify({"data": "False"})
        return result
    current_project = request.get_json()['pop']
    challenge_id = request.get_json()['topID']
    challenge_title = request.get_json()['topTitle']

    date = request.get_json()['dateH']

    if request.get_json()['cert']:
        certificate = request.get_json()['cert']
    else:
        certificate = None
    try:
        cash_prize = int(request.get_json()['cash'])
        points = int(request.get_json()['points'])
    except ValueError:
        return jsonify({"data": "False"})


    project = Project.query.filter_by(project_name=current_project).first()
    current_project = project.project_id
    current_pm = project.pm.emp_id
    current_dm = project.dm.emp_id

    new_topgearc_entry = Topgearc(
        emp_id=employee_id,
        project_id=current_project,
        pm_id=current_pm,
        dm_id=current_dm,
        topgear_id=challenge_id,
        challenge_title=challenge_title,
        points = points ,
        cash_prize=cash_prize,
        certificate=certificate,
        date=date
    )
    try:
        db.session.add(new_topgearc_entry)
        db.session.commit()
        result = jsonify({"data": "True"})
    except:
        db.session.rollback()
        result = jsonify({"data": "False"})
    return result

#Api to get the entries in the TopgearC table
@tgcregister.route('/topgearc_table', methods=['GET'])
def topgearc_table():
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        employee_id = 101
    if request.headers.get('role'):
        role = (request.headers.get('role')).strip('\"')
    else:
        role = "Team Member"

    if role == "Team Member":
        tgcEntries = Topgearc.query.filter_by(emp_id=employee_id).all()
    elif role == "Project Manager":
        tgcEntries = Topgearc.query.filter_by(pm_id=employee_id).all()
    elif role == "Delivery Manager":
        tgcEntries = Topgearc.query.filter_by(dm_id=employee_id).all()
    else:
        return jsonify(False)

    tgcdata_list = []
    for tgcEntry in tgcEntries:
        if tgcEntry.emp_id != tgcEntry.pm_id:
            case={"name":tgcEntry.emp.name,"project":tgcEntry.project.project_name,"pm":tgcEntry.pm.name,"dm":tgcEntry.dm.name,"tgid":tgcEntry.topgear_id,"chaltitle":tgcEntry.challenge_title,"points":tgcEntry.points,"cert":tgcEntry.certificate,"cashprize":tgcEntry.cash_prize,"date":tgcEntry.date}
            tgcdata_list.append(case)
    return jsonify(tgcdata_list)