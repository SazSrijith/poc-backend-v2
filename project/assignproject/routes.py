from flask import Blueprint,jsonify, request
from sqlalchemy.exc import IntegrityError
from project import db
from project.models import Transprojectassign



assign = Blueprint('assign',__name__)

#Api to assign project to the employees
@assign.route('/add_details', methods=['POST'])
def add_details():
    employee_id = 101
    if None in (request.get_json()['pop'],request.get_json()['dateFrom'],request.get_json()['dateTill']):
        result = jsonify({"data": "False"})
        return result
    project_name = request.get_json()['pop']
    start_date = request.get_json()['dateFrom']
    end_date = request.get_json()['dateTill']

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
    employee_id = 101
    projectAssign_list = Transprojectassign.query.filter_by(emp_id=employee_id)

    for projectAssign in projectAssign_list:
        case={"Name":projectAssign.emp.name,"Project":projectAssign.project.project_name,"PM":projectAssign.pm.name,"DM":projectAssign.dm.name,"Start_Date":projectAssign.start_date,"end_Date":projectAssign.end_date}
        proassignlist.append(case)
    return jsonify(proassignlist)

