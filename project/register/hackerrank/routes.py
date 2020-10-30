from flask import Blueprint,jsonify, request
from datetime import datetime
from project import db
from project.models import Skill, Certification, Project, Hackerrank



hrregister= Blueprint('hrregister',__name__)

#Api to add an entry to the hackerrank table
@hrregister.route('/add_hackerrank', methods=['POST'])
def add_hr_entry():
    # employee_id = request.get_json()['emp_id']
    employee_id = 102
    if None in (request.get_json()['pop'],request.get_json()['empName'],request.get_json()['cert'],request.get_json()['skill'],request.get_json()['mod'],request.get_json()['dateH'],request.get_json()['hScore']):
        result = jsonify({"data": "False"})
        return result
    current_project= request.get_json()['pop']
    hr_userid=request.get_json()['empName']
    cert=request.get_json()['cert']
    skill=request.get_json()['skill']
    contest_practice=request.get_json()['mod']
    date=request.get_json()['dateH']
    score = int(request.get_json()['hScore'])

    skill = Skill.query.filter_by(name=skill).first()
    skill_id = skill.id
    cert = Certification.query.filter_by(name=cert).first()
    cert_id = cert.id

    project = Project.query.filter_by(project_name=current_project).first()
    current_project = project.project_id

    current_pm = project.pm.emp_id
    current_dm = project.dm.emp_id

    if score < 100:
        badge = 'Bronze'
        no_of_stars = "★★"
    elif score < 200:
        badge = 'Silver'
        no_of_stars = "★★★"
    else:
        badge = 'Gold'
        no_of_stars = "★★★★"

    new_hackerrank_entry = Hackerrank(
        emp_id=employee_id,
        project_id=current_project,
        pm_id =current_pm,
        dm_id=current_dm,
        hr_userid=hr_userid,
        cert_id=cert_id,
        skill_id=skill_id,
        badge=badge,
        no_of_stars=no_of_stars,
        contest_practice=contest_practice,
        date=date,
        score=score
    )
    try:
        db.session.add(new_hackerrank_entry)
        db.session.commit()
        result = jsonify({"data": "True"})
    except:
        db.session.rollback()
        result = jsonify({"data": "False"})
    return result

#Api to get the entries in the hackerrank table.
@hrregister.route('/hackerrank_table', methods=['GET'])
def hackerrank_table():
    employee_id = 102
    hrdata_list=[]

    hrEntries = Hackerrank.query.filter_by(emp_id=employee_id)
    for hrEntry in hrEntries:
        case={"Name":hrEntry.emp.name,"Project":hrEntry.project.project_name,"PM":hrEntry.pm.name,"DM":hrEntry.dm.name,"HackerRankID":hrEntry.hr_userid,"Certification":None,"Skill":None,"Badge":hrEntry.badge,"Stars":hrEntry.no_of_stars,"Mode":hrEntry.contest_practice,"date":hrEntry.date,"Score":hrEntry.score}
        if hrEntry.cert_id is not None:
            case["Certification"]=hrEntry.cert.name
        if hrEntry.skill_id is not None:
            case["Skill"]=hrEntry.skill.name
        hrdata_list.append(case)
    return jsonify({"data":hrdata_list,"header":[{'Name':'Name'},{'Project':'Project'},{'PM':'PM'},{'DM':'DM'},{"HackerRankID":"HackerRankID"},{"Certification":"Certification"},{"Skill":"Skill"},{"Badge":"Badge"},{"Stars":"Stars"},{"Mode":"Mode"},{"Date":"Date"}]})
