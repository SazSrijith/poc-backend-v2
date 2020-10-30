from flask import Blueprint,jsonify, request
from datetime import datetime
from project import db
from project.models import Pragati, Project



prregister= Blueprint('prregister',__name__)

#Api to add an entry to the pragati table
@prregister.route('/add_pragati', methods=['POST'])
def add_pragati():

    employee_id = 101
    if None in (request.get_json()['pop'],request.get_json()['pragatiID'],request.get_json()['pragatiTitle'],request.get_json()['des'],request.get_json()['dateP']):
        result = jsonify({"data": "False"})
        return result
    current_project = request.get_json()['pop']
    pragati_id = request.get_json()['pragatiID']
    pragati_title = request.get_json()['pragatiTitle']
    description = request.get_json()['des']
    date = request.get_json()['dateP']

    print("project_id= ",request.get_json()['pop'])
    print("pragati_id= ",request.get_json()['pragatiID'])
    print("pragati_title= ",request.get_json()['pragatiTitle'])
    print("description= ",request.get_json()['des'])
    print("date= ",request.get_json()['dateP'])

    project = Project.query.filter_by(project_name=current_project).first()
    current_project = project.project_id
    current_pm = project.pm.emp_id
    current_dm = project.dm.emp_id

    new_pragati_entry = Pragati(
        emp_id=employee_id,
        project_id=current_project,
        pm_id=current_pm,
        dm_id=current_dm,
        pragati_id=pragati_id,
        pragati_title=pragati_title,
        description=description,
        date=date
    )
    try:
        db.session.add(new_pragati_entry)
        db.session.commit()
        result = jsonify({"data": "True"})
    except:
        db.session.rollback()
        result = jsonify({"data": "False"})
    return result

#Api to get the entries in the pragati table
@prregister.route('/pragati_table', methods=['GET'])
def pragati_table():
    employee_id = 101
    pgdata_list=[]

    pgEntries = Pragati.query.filter_by(emp_id=employee_id)
    for pgEntry in pgEntries:
        case={"Name":pgEntry.emp.name,"Project":pgEntry.project.project_name,"PM":pgEntry.pm.name,"DM":pgEntry.dm.name,"PragatiID":pgEntry.pragati_id,"PragatiTitle":pgEntry.pragati_title,"Description":pgEntry.description,"date":pgEntry.date}
        pgdata_list.append(case)
    return jsonify(pgdata_list)
