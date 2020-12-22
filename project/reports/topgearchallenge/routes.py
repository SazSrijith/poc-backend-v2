from flask import Blueprint,jsonify , request
from datetime import datetime
from project.models import Topgearc

tgcreport= Blueprint('tgcreport',__name__)

@tgcreport.route('/tgctable_highestcashprize', methods=['GET'])
def tgctable_top_highest_cashprize():
    top_highest_cashprize = 0
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        employee_id = 101
    entry_list = Topgearc.query.filter_by(emp_id=employee_id).all()
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            if not entry.cash_prize:
                continue
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                if entry.cash_prize > top_highest_cashprize:
                    top_highest_cashprize = entry.cash_prize
    result = "Highest TopGear Cash Prize Received: " + str(top_highest_cashprize)
    return jsonify({"highest_cashprize": result})

@tgcreport.route('/tgctable_totalcashprize', methods=['GET'])
def tctable_total_cashprize():
    total_cashprize = 0
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        employee_id = 101
    entry_list = Topgearc.query.filter_by(emp_id=employee_id).all()
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            if not entry.cash_prize:
                continue
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                total_cashprize = total_cashprize + entry.cash_prize
    result = "Total TopGear Cash Prize Received: " + str(total_cashprize)
    return jsonify({"total_cashprize": result})

@tgcreport.route('/tgctable_totaltimes', methods=['GET'])
def tgctable_totaltimes():
    total_times = 0
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        employee_id = 101
    entry_list = Topgearc.query.filter_by(emp_id=employee_id).all()
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                total_times = total_times + 1
    result = "Total TopGear Challenges Attempted: " + str(total_times)
    return jsonify({"total_times": result})


@tgcreport.route('/tgctable_highestpoint', methods=['GET'])
def tgctable_highestpoint():
    highest_point = 0
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        employee_id = 101
    entry_list = Topgearc.query.filter_by(emp_id=employee_id).all()
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                if entry.points > highest_point:
                    highest_point = entry.points
    result = "Highest TopGear Challenge Point Received: " + str(highest_point)
    return jsonify({"highest_point": result})


@tgcreport.route('/tgctable_totalpoints', methods=['GET'])
def tgctable_totalpoints():
    total_points = 0
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        employee_id = 101
    entry_list = Topgearc.query.filter_by(emp_id=employee_id).all()
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                total_points = total_points + entry.points
    result = "Total TopGear Challenge Points Received: " + str(total_points)
    return jsonify({"total_points": result})


@tgcreport.route('/tgctable_graphdata', methods=['GET'])
def tgctable_graphdata():
    months=[]
    points = []
    cash=[]
    for i in range(1, 13):
        date = datetime.strptime("2020-" + str(i) + "-01", '%Y-%m-%d')
        months.append(date.strftime("%B"))
        points.append(0)
        cash.append(0)
    if request.headers.get('id'):
        employee_id = request.headers.get('id')
    else:
        employee_id = 101
    entry_list = Topgearc.query.filter_by(emp_id=employee_id).all()
    date = datetime.now()
    year_start_date = datetime(date.year, 1, 1)
    year_end_date = datetime(date.year, 12, 31)
    if entry_list:
        for entry in entry_list:
            date = datetime.strptime(entry.date, '%Y-%m-%d')
            if (date >= year_start_date) and (date <= year_end_date):
                month_no = date.strftime("%m")
                points[int(month_no)-1]=entry.points
                cash[int(month_no)-1]=entry.cash_prize
    return jsonify({'months': months, "points": points, "cash": cash})