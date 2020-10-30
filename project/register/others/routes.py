from flask import Blueprint,jsonify, request
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from project import db
from project.models import Skill,Certification,Project



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


#Api to provide the drop down information.
@othersreg.route('/ddinfo', methods=['GET'])
def ddInfo():
    empid=101
    project_list=[]
    skill_list=[]
    cert_list=[]
    # projects = Transprojectassign.query.filter_by(emp_id=empid).all()
    # if projects:
    #     for project in projects:
    #         project_list.append(project.project.project_name)
    projects = Project.query.all()
    for project in projects:
        project_list.append(project.project_name)

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