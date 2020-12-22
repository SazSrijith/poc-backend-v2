from flask import Blueprint,jsonify, request
from datetime import datetime
from project import db
from project.models import Topgearl, Project



tglregister= Blueprint('tglregister',__name__)

#Api to add an entry to the topgearL table
@tglregister.route('/add_topgearl', methods=['POST'])
def add_topgearl():
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        employee_id = 101
    if None in (request.get_json()['pop'],request.get_json()['chalID'],request.get_json()['cert'],request.get_json()['dateT']):
        result = jsonify({"data": "False"})
        return result
    current_project = request.get_json()['pop']
    topgearl_id = request.get_json()['chalID']
    certificate = request.get_json()['cert']
    date = request.get_json()['dateT']

    project = Project.query.filter_by(project_name=current_project).first()
    current_project = project.project_id
    current_pm = project.pm.emp_id
    current_dm = project.dm.emp_id

    new_topgearl_entry = Topgearl(
        emp_id=employee_id,
        project_id=current_project,
        pm_id=current_pm,
        dm_id=current_dm,
        topgearlearning_id=topgearl_id,
        certificate=certificate,
        date=date
    )
    try:
        db.session.add(new_topgearl_entry)
        db.session.commit()
        result = jsonify({"data": "True"})
    except:
        db.session.rollback()
        result = jsonify({"data": "False"})
    return result

#Api to get the entries in the topgearl table
@tglregister.route('/topgearl_table', methods=['GET'])
def topgearl_table():
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        employee_id = 101
    tgldata_list=[]

    tglEntries = Topgearl.query.filter_by(emp_id=employee_id)
    for tglEntry in tglEntries:
        if tglEntry.emp_id != tglEntry.pm_id:
            case={"name":tglEntry.emp.name,"project":tglEntry.project.project_name,"pm":tglEntry.pm.name,"dm":tglEntry.dm.name,"topglid":tglEntry.topgearlearning_id,"cert":tglEntry.certificate,"date":tglEntry.date}
            tgldata_list.append(case)
    return jsonify(tgldata_list)
