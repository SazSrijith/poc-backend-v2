from flask import Blueprint,jsonify, request
from datetime import datetime
from project import db
from project.models import Project, Shristi



shregister= Blueprint('shreport',__name__)

#Api to add an entry to the shristi table
@shregister.route('/add_shristi', methods=['POST'])
def add_shristi():

    employee_id = 101
    if None in (request.get_json()['pop'],request.get_json()['shristiID'],request.get_json()['shristiTitle'],request.get_json()['des'],request.get_json()['dateP']):
        result = jsonify({"data": "False"})
        return result
    current_project = request.get_json()['pop']
    shristi_id = request.get_json()['shristiID']
    shristi_title = request.get_json()['shristiTitle']
    description = request.get_json()['des']
    date = request.get_json()['dateP']

    print("project_id= ",request.get_json()['pop'])
    print("shristi_id= ",request.get_json()['shristiID'])
    print("shristi_title= ",request.get_json()['shristiTitle'])
    print("description= ",request.get_json()['des'])
    print("date= ",request.get_json()['dateP'])

    project = Project.query.filter_by(project_name=current_project).first()
    current_project = project.project_id
    current_pm = project.pm.emp_id
    current_dm = project.dm.emp_id

    new_shristi_entry = Shristi(
        emp_id=employee_id,
        project_id=current_project,
        pm_id=current_pm,
        dm_id=current_dm,
        shristi_id=shristi_id,
        shristi_title=shristi_title,
        description=description,
        date=date
    )
    try:
        db.session.add(new_shristi_entry)
        db.session.commit()
        result = jsonify({"data": "True"})
    except:
        db.session.rollback()
        result = jsonify({"data": "False"})
    return result

#Api to get the entries in the shristi table
@shregister.route('/shristi_table', methods=['GET'])
def shristi_table():
    employee_id = 101
    stdata_list=[]

    stEntries = Shristi.query.filter_by(emp_id=employee_id)
    for stEntry in stEntries:
        case={"Name":stEntry.emp.name,"Project":stEntry.project.project_name,"PM":stEntry.pm.name,"DM":stEntry.dm.name,"ShristiID":stEntry.shristi_id,"ShristiTitle":stEntry.shristi_title,"Description":stEntry.description,"date":stEntry.date}
        stdata_list.append(case)
    return jsonify(stdata_list)

