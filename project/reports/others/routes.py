from flask import Blueprint,jsonify, session
from project.models import Employee



othersrep = Blueprint('othersrep',__name__)


@othersrep.route('/find_name', methods=['GET'])
def find_name():
    if "role" in session:
        role = session['role']
    else:
        role = None
    if "id" in session:
        empid = session['id']
        emp = Employee.query.filter_by(emp_id=empid).first()
        name = emp.name
    else:
        name = None
    return jsonify({"name":name,"role":role})