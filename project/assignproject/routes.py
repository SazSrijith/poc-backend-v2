from flask import Blueprint,jsonify, request
from sqlalchemy.exc import IntegrityError
from project import db
from project.models import Transprojectassign,Project, Employee
import datetime



assign = Blueprint('assign',__name__)

#Api to assign project to the employees
@assign.route('/add_details', methods=['POST'])
def add_details():
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        return jsonify(False)
    if None in (request.get_json()['res'],request.get_json()['pop'],request.get_json()['dateFrom'],request.get_json()['dateTill']):
        result = jsonify({"data": "False"})
        return result
    employee_name = request.get_json()['res']
    emp_record = Employee.query.filter_by(name=employee_name).first()
    employee_id = emp_record.emp_id
    project_name = request.get_json()['pop']
    start_date = request.get_json()['dateFrom']
    end_date = request.get_json()['dateTill']
    conv_start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    conv_end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    if conv_end_date < conv_start_date:
        return jsonify({"data": "False"})


    project = Project.query.filter_by(project_name=project_name).first()
    pm_id = project.pm_id
    dm_id = project.dm_id

    new_project_assign = Transprojectassign(
        emp_id=employee_id,
        project_id=project.project_id,
        start_date=start_date,
        end_date=end_date,
        pm_id=pm_id,
        dm_id=dm_id
    )
    try:

        db.session.add(new_project_assign)
        db.session.commit()
        result = jsonify({"data": "True"})
    except:
        db.session.rollback()
        result = jsonify({"data": "False"})
    return result


#Api to get the project_assign table
@assign.route('/get_details', methods=['GET'])
def get_details():
    proassignlist=[]
    if request.headers.get('role'):
        print("id received")
    if request.headers.get('id') and request.headers.get('role'):
        employee_id = request.headers.get('id')
        role = (request.headers.get('role')).strip('\"')
    else:
        return jsonify(False)
    if role == "Team Member":
        projectAssign_list = Transprojectassign.query.filter_by(emp_id=employee_id).all()
    elif role == "Project Manager":
        projectAssign_list = Transprojectassign.query.filter_by(pm_id=employee_id).all()
    elif role == "Delivery Manager":
        projectAssign_list = Transprojectassign.query.filter_by(dm_id=employee_id).all()
    else:
        return jsonify(False)

    for projectAssign in projectAssign_list:
        case={"Name":projectAssign.emp.name,"Project":projectAssign.project.project_name,"PM":projectAssign.pm.name,"DM":projectAssign.dm.name,"Start_Date":projectAssign.start_date,"end_Date":projectAssign.end_date}
        proassignlist.append(case)
    return jsonify(proassignlist)

