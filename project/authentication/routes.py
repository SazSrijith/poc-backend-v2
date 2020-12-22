from flask import Blueprint,jsonify, request , session
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from project import db
from project.models import Employee,User, Project



auth = Blueprint('auth',__name__)

#Api to register the user to the user table, after validation  
@auth.route('/register', methods=['POST'])
def register():
    if None in (request.get_json()['firstName'],request.get_json()['email'],request.get_json()['password']):
        return jsonify({"data": "False"})
    emp_info = request.get_json()
    created = datetime.now()
    employee_id = emp_info['firstName']
    emp = Employee.query.filter_by(emp_id=employee_id).first()

    if not emp:
        return jsonify({"data": "False"})
    if emp.email == emp_info['email']:
        new_user = User(
            emp_id=employee_id,
            # password=bcrypt.generate_password_hash(emp_info['password']).decode('utf-8'),
            password=emp_info['password'],
            # email=emp_info['employee_email'],
            date=created
        )
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return jsonify({'data': "False"})
        return jsonify({'data': "True"})
    else:
        return jsonify({"data": "False"})


#Api to sign in the user after validation
@auth.route('/signin', methods=['POST'])
def signin():
    if None in (request.get_json()['role'], request.get_json()['email'], request.get_json()['password']):
        return jsonify({"data": "False"})
    emp_info = request.get_json()
    role = emp_info['role']
    employee=Employee.query.filter_by(email=emp_info['email']).first()

    if not employee:
        return jsonify({"data": "False"})
    id = employee.emp_id
    user = User.query.filter_by(emp_id=id).first()

    if not user or not user.password == emp_info['password']:
        return jsonify({"data": "False"})

    if role == "Project Manager":
        # Searching if the id is in the PM column in Master Project Table
        projects = Project.query.filter_by(pm_id=id).all()
    elif role == "Delivery Manager":
        # Searching if the id is in the DM column in Master Project Table
        projects = Project.query.filter_by(dm_id=id).all()
    elif role == "Team Member":
        projects = True
    else:
        projects = None

    if not projects:
        return jsonify({"data": "False"})

    # session['id'] = id
    # session['role'] = role
    return jsonify({"data": "True","id":id,"role":role})


# To display the user with his password after validation
@auth.route('/forgot_password', methods=['POST'])
def forgot_password():
    employee_id = request.get_json()['firstName']
    employee_email = request.get_json()['email']
    employee = User.query.filter_by(emp_id = employee_id).first()
    if not employee:
        return jsonify({"msg": "False", "message": "Incorrect Credentials"})
    if not employee.emp.email == employee_email:
        return jsonify({"msg": "False", "message": "Incorrect Credentials"})
    return jsonify({"msg":"True","password":employee.password})

#To get all the details in user table
@auth.route('/get_usertable', methods=['GET'])
def get_usertable():
    userlist=[]
    users=User.query.all()
    for user in users:
        case={"id":user.emp_id,"pass":user.password}
        userlist.append(case)
    return jsonify(userlist)


@auth.route('/get_roles', methods=['GET'])
def get_roles():
    roles = ["Team Member","Project Manager","Delivery Manager","PMO/Admin"]
    return jsonify(roles)

@auth.route('/logout', methods=['GET'])
def logout():
    session.pop("id", None)
    session.pop("role", None)
    return jsonify(True)