from flask import Blueprint,jsonify, request
from datetime import datetime
from project import db
from project.models import Trendnxt,Employee,Project



tnregister= Blueprint('tnregister',__name__)

#Api to add an entry to the trendnext table
@tnregister.route('/add_trendnext', methods=['POST'])
def add_trendnxt():
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        employee_id = 101
    threshold_points = 0
    financial_year = "2019-2020"
    if None in (request.get_json()['pop'],request.get_json()['topics'],request.get_json()['trendScore'],request.get_json()['dateT']):
        result = jsonify({"data": "False"})
        return result
    current_project = request.get_json()['pop']
    topic = request.get_json()['topics']

    try:
        points = int(request.get_json()['trendScore'])
    except ValueError:
        return jsonify({"data": "False"})

    date = request.get_json()['dateT']

    employee = Employee.query.filter_by(emp_id = employee_id).first()
    band = employee.band
    if band in ("TRB","A3"):
        threshold_points = 40
    elif band in ("WASE","WiSTA","WIMS","SIM","B1"):
        threshold_points = 140    
    elif band == "B2":
        threshold_points = 200
    else:
        pass
    project = Project.query.filter_by(project_name=current_project).first()
    current_project = project.project_id
    current_pm = project.pm.emp_id
    current_dm = project.dm.emp_id

    new_trendnxt_entry = Trendnxt(
        emp_id=employee_id,
        project_id=current_project,
        pm_id=current_pm,
        dm_id=current_dm,
        topic=topic,
        points=points,
        date=date,
        threshold_points=threshold_points,
        financial_year=financial_year
    )
    try:
        db.session.add(new_trendnxt_entry)
        db.session.commit()
        result = jsonify({"data": "True"})
    except:
        db.session.rollback()
        result = jsonify({"data": "False"})
    return result

#Api to get the entries in the trendnext table
@tnregister.route('/trendnext_table', methods=['GET'])
def trendnext_table():
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
        print("id recieved")
    else:
        employee_id = 101
        print("id not recieved")
    if request.headers.get('role'):
        role = (request.headers.get('role')).strip('\"')
        print("role recieved")
        print("role not recieved")
    else:
        role = "Team Member"

    if role == "Team Member":
        tnEntries = Trendnxt.query.filter_by(emp_id=employee_id).all()
    elif role == "Project Manager":
        tnEntries = Trendnxt.query.filter_by(pm_id=employee_id).all()
    elif role == "Delivery Manager":
        tnEntries = Trendnxt.query.filter_by(dm_id=employee_id).all()
    else:
        print("ERROR")
        return jsonify(False)

    tndata_list=[]


    for tnEntry in tnEntries:
        if tnEntry.emp_id != tnEntry.pm_id:
            case={"Name":tnEntry.emp.name,"Project":tnEntry.project.project_name,"PM":tnEntry.pm.name,"DM":tnEntry.dm.name,"Topic":tnEntry.topic,"Points":tnEntry.points,"Threshold":tnEntry.threshold_points,"date":tnEntry.date,"FY":tnEntry.financial_year}
            tndata_list.append(case)
    return jsonify(tndata_list)