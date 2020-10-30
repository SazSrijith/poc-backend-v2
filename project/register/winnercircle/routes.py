from flask import Blueprint,jsonify, request
from datetime import datetime
from project import db
from project.models import Winnercircle, Project



wcregister= Blueprint('wcregister',__name__)

#Api to add an entry to the winnercircle table
@wcregister.route('/add_winnercircle', methods=['POST'])
def add_wc():
    
    employee_id = 101
    if None in (request.get_json()['pop'],request.get_json()['des'],request.get_json()['rFrom'],request.get_json()['dateP'],request.get_json()['wcPoints']):
        result = jsonify({"data": "False"})
        return result
    current_project= request.get_json()['pop']
    description=request.get_json()['des']
    received_from=request.get_json()['rFrom']
    date=request.get_json()['dateP']
    points = int(request.get_json()['wcPoints'])

    print("current_project= ", request.get_json()['pop'])
    print("description= ",request.get_json()['des'])
    print("recieved_from= ",request.get_json()['rFrom'])
    print("date= ",request.get_json()['dateP'])
    print("points= ",request.get_json()['wcPoints'])

    project = Project.query.filter_by(project_name=current_project).first()
    current_project = project.project_id
    current_pm = project.pm.emp_id
    current_dm = project.dm.emp_id

    new_winnercircle_entry = Winnercircle(
        emp_id=employee_id,
        project_id=current_project,
        pm_id=current_pm,
        dm_id=current_dm,
        description=description,
        points=points,
        received_from=received_from,
        date=date
    )
    try:
        db.session.add(new_winnercircle_entry)
        db.session.commit()
        result = jsonify({"data": "True"})
    except:
        db.session.rollback()
        result = jsonify({"data": "False"})
    return result

#Api to get the entries in the winnercircle table
@wcregister.route('/winnercircle_table', methods=['GET'])
def winnercircle_table():
    employee_id = 101
    wcdata_list=[]

    wcEntries = Winnercircle.query.filter_by(emp_id=employee_id)
    for wcEntry in wcEntries:
        case={"Name":wcEntry.emp.name,"Project":wcEntry.project.project_name,"PM":wcEntry.pm.name,"DM":wcEntry.dm.name,"Description":wcEntry.description,"Points":wcEntry.points,"From":wcEntry.received_from,"date":wcEntry.date}
        wcdata_list.append(case)
    return jsonify(wcdata_list)