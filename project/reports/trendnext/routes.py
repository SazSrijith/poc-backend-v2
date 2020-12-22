from flask import Blueprint,jsonify, request
from datetime import datetime
from project.models import Trendnxt

tnreport= Blueprint('tnreport',__name__)

@tnreport.route('/tntable_thresholdpoints', methods=['GET'])
def tntable_thresholdpoints():
    id = request.headers.get('id')
    result = "Threshold Points: " + str(calculateThrehsold(id))
    return jsonify({'threshold_points': result})

@tnreport.route('/tntable_points', methods=['GET'])
def tntable_points():
    id = request.headers.get('id')
    result = "Total Trendnext Points: " + str(calculateTotalPoints(id))
    return jsonify({"trendnxt_points": result })


@tnreport.route('/tntable_graphdata', methods=['GET'])
def tntable_graphdata():
    sum = 0
    months = []
    points = []
    threshold = []
    value = None
    for i in range(1, 13):
        date = datetime.strptime("2020-" + str(i) + "-01", '%Y-%m-%d')
        months.append(date.strftime("%B"))
        points.append(0)
        threshold.append(0)

    employee_id = request.headers.get('id')
    role = (request.headers.get('role')).strip('\"')
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)

    if role == "Team Member":
        entry_list = Trendnxt.query.filter_by(emp_id=employee_id).all()
        if entry_list:
            for entry in entry_list:
                date = datetime.strptime(entry.date, '%Y-%m-%d')
                if (date >= year_start_date) and (date <= year_end_date):
                    sum = sum + entry.points
                    month_no = date.strftime("%m")
                    points[int(month_no) - 1] = sum
                    threshold[int(month_no) - 1] = entry.threshold_points
                    if not value:
                        value = entry.threshold_points
        new_threshold = value
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

    elif role == "Project Manager":
        names = []
        points = []
        threshold = []
        id_dict = {}
        employee_id = request.headers.get('id')
        entry_list = Trendnxt.query.filter_by(pm_id=employee_id).all()
        for entry in entry_list:
            if entry.emp_id != entry.pm_id:
                if entry.emp.name not in id_dict:
                    id_dict[entry.emp.name] = entry.emp_id
        for item in id_dict:
            id = id_dict[item]
            points.append(calculateTotalPoints(id))
            threshold.append(calculateThrehsold(id))
            names.append(item)
        points.append(0)
        return jsonify({"names":names,"points": points, "threshold": threshold})
    else:
        return jsonify({"data":False})


@tnreport.route('/tntable_percentgraph', methods=['GET'])
def tntable_percentgraph():
    id_dict = {}
    noCompleted = 0
    noIncompleted = 0
    percent1 = []
    percent2 = []
    total = 0
    employee_id = request.headers.get('id')
    entry_list = Trendnxt.query.filter_by(pm_id=employee_id).all()
    for entry in entry_list:
        if entry.emp_id != entry.pm_id:
            if entry.emp.name not in id_dict:
                id_dict[entry.emp.name] = entry.emp_id
    for item in id_dict:
        total = total  + 1
        id = id_dict[item]
        totalPoint = calculateTotalPoints(id)
        thresholdPoint = calculateThrehsold(id)
        if  totalPoint >= thresholdPoint:
            noCompleted = noCompleted + 1
        else :
            noIncompleted = noIncompleted + 1
    percent1.append(noCompleted/total * 100)
    percent2.append(noIncompleted/ total * 100)
    percent1.append(0)
    return jsonify({"incompletion": percent2,"completion": percent1, "labels": ["Completion Status"]})

def calculateThrehsold(id):
    threshold_points = 0
    employee_id = id
    entry_list = Trendnxt.query.filter_by(emp_id=employee_id).all()
    if not entry_list:
        print("No data for the current id")
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                if entry.threshold_points > threshold_points:
                    threshold_points = entry.threshold_points
    return threshold_points

def calculateTotalPoints(id):
    points = 0
    employee_id = id
    entry_list = Trendnxt.query.filter_by(emp_id=employee_id).all()
    if not entry_list:
        print("No data for the current id")
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                print("Value of entry.points:",entry.points)
                points = points + int(entry.points)
    return points
