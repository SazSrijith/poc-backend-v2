from flask import Blueprint,jsonify
from datetime import datetime
from project.models import Trendnxt

tnreport= Blueprint('tnreport',__name__)

@tnreport.route('/tntable_thresholdpoints', methods=['GET'])
def tntable_thresholdpoints():
    threshold_points = 0
    employee_id = 101
    entry_list = Trendnxt.query.filter_by(emp_id=employee_id).all()
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                if entry.threshold_points > threshold_points:
                    threshold_points = entry.threshold_points
    result = "Threshold Points: " + str(threshold_points)
    return jsonify({'threshold_points': result})

@tnreport.route('/tntable_points', methods=['GET'])
def tntable_points():
    points = 0
    employee_id = 101
    entry_list = Trendnxt.query.filter_by(emp_id=employee_id).all()
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                points=points+entry.points
    result = "Total Trendnext Points: " + str(points)
    return jsonify({"trendnxt_points": result })


@tnreport.route('/tntable_graphdata', methods=['GET'])
def tntable_graphdata():
    sum = 0
    months = []
    points = []
    threshold = []
    for i in range(1, 13):
        date = datetime.strptime("2020-" + str(i) + "-01", '%Y-%m-%d')
        months.append(date.strftime("%B"))
        points.append(0)
        threshold.append(0)

    employee_id = 101
    entry_list = Trendnxt.query.filter_by(emp_id=employee_id).all()
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                sum = sum + entry.points
                month_no = date.strftime("%m")
                points[int(month_no) - 1] = sum
                threshold[int(month_no) - 1] = entry.threshold_points
    new_threshold = 0
    for index,item in enumerate(threshold):
        if item != 0:
            new_threshold = item
        else:
            threshold[index] = new_threshold
    new_trendnxtpoint = 0
    for index,item in enumerate(points):
        if item != 0:
            new_trendnxtpoint = item
        else:
            points[index] = new_trendnxtpoint

    return jsonify({'months': months, "points": points, "threshold": threshold})