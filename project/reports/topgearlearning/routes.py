# from flask import Blueprint,jsonify, request
# from datetime import datetime
# from project import db
# from project.models import Winnercircle
#
#
#
# wcreport= Blueprint('wcreport',__name__)
#
# #Api to calculate the table queries.
# @wcreport.route('/wctable_totalpoints', methods=['POST'])
# def wctable_totalpoints():
#     total_points = 0
#     employee_id = request.get_json()['empID']
#     role = request.get_json()['role']
#     if role == 'Team Member':
#         entry_list = Winnercircle.query.filter_by(emp_id=employee_id).all()
#     elif(role == 'Project Manager'):
#         entry_list = Winnercircle.query.filter_by(pm_id=employee_id).all()
#     elif (role == 'Delivery Manager'):
#         entry_list = Winnercircle.query.filter_by(dm_id=employee_id).all()
#     else:
#         pass
#     year_start_date = datetime(request.get_json()['year'], 1, 1)
#     year_end_date = datetime(request.get_json()['year'], 12, 31)
#     if entry_list:
#         for entry in entry_list:
#             date = datetime.strptime(entry.date, '%Y-%m-%d')
#             if ( date > year_start_date) and ( date < year_end_date):
#                 total_points = total_points + entry.points
#     return jsonify({'total_points': total_points})
#
#
# @wcreport.route('/wctable_totaltimes', methods=['POST'])
# def wctable_totaltimes():
#     total_times = 0
#     employee_id = request.get_json()['empID']
#     role = request.get_json()['role']
#     if role == 'Team Member':
#         entry_list = Winnercircle.query.filter_by(emp_id=employee_id).all()
#     elif(role == 'Project Manager'):
#         entry_list = Winnercircle.query.filter_by(pm_id=employee_id).all()
#     elif (role == 'Delivery Manager'):
#         entry_list = Winnercircle.query.filter_by(dm_id=employee_id).all()
#     else:
#         pass
#     year_start_date = datetime(request.get_json()['year'], 1, 1)
#     year_end_date = datetime(request.get_json()['year'], 12, 31)
#     if entry_list:
#         for entry in entry_list:
#             date = datetime.strptime(entry.date, '%Y-%m-%d')
#             if ( date > year_start_date) and ( date < year_end_date):
#                 total_times=total_times+1
#
#     return jsonify({'total_times': total_times})
#
#
# @wcreport.route('/wctable_highest_point', methods=['POST'])
# def wctable_highest_point():
#     highest_point = 0
#     employee_id = request.get_json()['empID']
#     role = request.get_json()['role']
#     if role == 'Team Member':
#         entry_list = Winnercircle.query.filter_by(emp_id=employee_id).all()
#     elif(role == 'Project Manager'):
#         entry_list = Winnercircle.query.filter_by(pm_id=employee_id).all()
#     elif (role == 'Delivery Manager'):
#         entry_list = Winnercircle.query.filter_by(dm_id=employee_id).all()
#     else:
#         pass
#     year_start_date = datetime(request.get_json()['year'], 1, 1)
#     year_end_date = datetime(request.get_json()['year'], 12, 31)
#     if entry_list:
#         for entry in entry_list:
#             date = datetime.strptime(entry.date, '%Y-%m-%d')
#             if ( date > year_start_date) and ( date < year_end_date):
#                 if entry.points> highest_point:
#                     highest_point = entry.points
#     return jsonify({'highest_point': highest_point})
#
