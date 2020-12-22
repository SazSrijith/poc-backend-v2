from flask import Blueprint,jsonify, request
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from project import db
from project.models import Skill,Certification,Project, Transprojectassign , Employee



othersreg = Blueprint('othersreg',__name__)

#Api to add skill and certificate to their respective table.
@othersreg.route('/add_skillcert', methods=['POST'])
def add_skillcert():
    if None in (request.get_json()['skill_name'],request.get_json()['cert_name']):
        result = jsonify({"data": "False"})
        return result
    newskill=Skill(
        name = request.get_json()['skill_name']
    )
    newcert=Certification(
        name = request.get_json()['cert_name']
    )
    db.session.add(newskill)
    db.session.add(newcert)
    db.session.commit()
    return jsonify({"data":"True"})

@othersreg.route('/resources', methods=['GET'])
def resources():
    resourceList = []
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        employee_id = 101

    if request.headers.get('role'):
        role = (request.headers.get('role')).strip('\"')
    else:
        role = "Team Member"
    if role == "Team Member":
        emp = Employee.query.filter_by(emp_id=employee_id).first()
        resourceList.append(emp.name)
        return jsonify({"resource": resourceList})
    elif role == "Project Manager":
        tpaEntries = Transprojectassign.query.filter_by(pm_id=employee_id).all()
    elif role == "Delivery Manager":
        tpaEntries = Transprojectassign.query.filter_by(dm_id=employee_id).all()
    else:
        return jsonify(False)

    for tpaEntry in tpaEntries:
        if not tpaEntry.emp.name in resourceList:
            resourceList.append(tpaEntry.emp.name)
    return jsonify({"resource":resourceList})


#Api to provide the drop down information.
@othersreg.route('/ddinfo', methods=['GET'])
def ddInfo():
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        employee_id = 101
    project_list=[]
    skill_list=[]
    cert_list=[]
    projects = Transprojectassign.query.filter((Transprojectassign.emp_id == employee_id) | (Transprojectassign.pm_id == employee_id)).all()
    if projects:
        for project in projects:
            if not project.project.project_name in project_list:
                project_list.append(project.project.project_name)
    # projects = Project.query.all()
    # for project in projects:
    #     project_list.append(project.project_name)

    skills = Skill.query.all()
    for skill in skills:
        skill_list.append(skill.name)

    certs = Certification.query.all()
    for cert in certs:
        cert_list.append(cert.name)

    return jsonify({"projectList":project_list,
                    "skillList":skill_list,
                    "certList":cert_list
                    })