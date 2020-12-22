from project.models import Trendnxt
# newemp = Employee(
#     emp_id = 444,
#     name = "Baiju",
#     email = "baiju@gmail.com",
#     band = "B2",
#     location = "Bangalore",
#     role = "Delivery Manager"
# )
# db.session.add(newemp)
# db.session.commit()

# newpro = Project(
#     project_id = 5,
#     project_name = "POC",
#     start_date = "2020-01-01",
#     end_date = "2020-12-01",
#     pm_id = 333,
#     dm_id = 444
# )
# db.session.add(newpro)
# db.session.commit()
id = 333
id_dict={}
entry_list = Trendnxt.query.filter_by(pm_id=id).all()
for entry in entry_list:
    if entry.emp.name not in id_dict:
        id_dict[entry.emp.name] = entry.emp_id
for item in id_dict:
    print(id_dict[item])