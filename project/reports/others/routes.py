from flask import Blueprint,jsonify, session , request
# form Flask-JSON import JSON
from project.models import Employee



othersrep = Blueprint('othersrep',__name__)


@othersrep.route('/find_name', methods=['GET'])
def find_name():
    if None in (request.headers.get('role'), request.headers.get('id')):
        return jsonify({"data": "False"})
    id = (request.headers.get('id'))
    role = (request.headers.get('role')).strip('\"')
    emp = Employee.query.filter_by(emp_id=id).first()
    if not emp:
        return jsonify({"data": "False"})
    return jsonify({"data":"True","name":emp.name,"role":role})