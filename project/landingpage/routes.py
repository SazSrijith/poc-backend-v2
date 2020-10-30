from flask import Blueprint,jsonify, request
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from project import db
from project.models import Winnercircle,Trendnxt



home= Blueprint('home',__name__)

#Api to display the highlights in home.
@home.route('/result', methods=['GET'])
def result():
    total_points = 0
    total_times = 0
    highest_point = 0
    employee_id = 101
    entry_list = Winnercircle.query.filter_by(emp_id=employee_id).all()
    for entry in entry_list:
        date = datetime.strptime(entry.date, '%Y-%m-%d')
        year_start_date = datetime(2020, 1, 1)
        year_end_date = datetime(2020, 12, 31)
        if ( date > year_start_date) and ( date < year_end_date):
            total_times=total_times+1
            total_points = total_points + entry.points
            if entry.points> highest_point:
                highest_point = entry.points

    threshold_points = 0
    trendnxt_points = 0
    details=[]

    employee_id = 101
    entry_list = Trendnxt.query.filter_by(emp_id=employee_id).all()
    for entry in entry_list:
        trendnxt_points = trendnxt_points + entry.points
        case = (entry.topic,entry.points)
        details.append(case)
        if entry.threshold_points > threshold_points:
            threshold_points = entry.threshold_points
    return jsonify(True)