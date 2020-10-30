from flask import Blueprint,jsonify, request
from datetime import datetime
from project import db
from project.models import Winnercircle



wcreport= Blueprint('wcreport',__name__)



@wcreport.route('/wctable_totalpoints', methods=['GET'])
def wctable_totalpoints():
    total_points = 0
    employee_id = 101
    entry_list = Winnercircle.query.filter_by(emp_id=employee_id).all()
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if ( date >= year_start_date) and ( date <= year_end_date):
                total_points = total_points + entry.points
    result = "Total Winner Circle Points : " + str(total_points)
    return jsonify({'total_points': result})


@wcreport.route('/wctable_totaltimes', methods=['GET'])
def wctable_totaltimes():
    total_times = 0
    employee_id = 101
    entry_list = Winnercircle.query.filter_by(emp_id=employee_id).all()
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                total_times = total_times + 1
    result = "Total Number of Recognitions Received : " + str(total_times)
    return jsonify({'total_times': result})


@wcreport.route('/wctable_highest_point', methods=['GET'])
def wctable_highest_point():
    highest_point = 0
    employee_id = 101
    entry_list = Winnercircle.query.filter_by(emp_id=employee_id).all()
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                if entry.points > highest_point:
                    highest_point = entry.points
    result = "Highest Winner Circle Points Received : " + str(highest_point)
    return jsonify({'highest_point': result})

@wcreport.route('/wctable_graphdata', methods=['GET'])
def wctable_graphdata():
    months = []
    points = []
    for i in range(1, 13):
        date = datetime.strptime("2020-" + str(i) + "-01", '%Y-%m-%d')
        months.append(date.strftime("%B"))
        points.append(0)

    employee_id = 101
    entry_list = Winnercircle.query.filter_by(emp_id=employee_id).all()
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                month_no = date.strftime("%m")
                points[int(month_no) - 1] = entry.points

    return jsonify({'months': months, "points": points})

