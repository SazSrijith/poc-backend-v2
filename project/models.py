from project import db



class Employee(db.Model):
    emp_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    band = db.Column(db.Text)
    location = db.Column(db.Text)
    role = db.Column(db.Text)

class User(db.Model):
    emp_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'), primary_key=True)
    emp = db.relationship("Employee", foreign_keys='User.emp_id')

    password = db.Column(db.Text)
    date = db.Column(db.DateTime)


class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.Text)
    start_date = db.Column(db.Text)
    end_date = db.Column(db.Text)

    pm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    pm = db.relationship("Employee", foreign_keys='Project.pm_id')

    dm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    dm = db.relationship("Employee", foreign_keys='Project.dm_id')


class Certification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)


class Transprojectassign(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    emp_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    emp = db.relationship("Employee", foreign_keys='Transprojectassign.emp_id')

    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'))
    project = db.relationship("Project", foreign_keys='Transprojectassign.project_id')

    start_date = db.Column(db.Text)
    end_date = db.Column(db.Text)

    pm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    pm = db.relationship("Employee", foreign_keys='Transprojectassign.pm_id')

    dm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    dm = db.relationship("Employee", foreign_keys='Transprojectassign.dm_id')


class Hackerrank(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    emp_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    emp = db.relationship("Employee", foreign_keys='Hackerrank.emp_id')

    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'))
    project = db.relationship("Project", foreign_keys='Hackerrank.project_id')

    pm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    pm = db.relationship("Employee", foreign_keys='Hackerrank.pm_id')

    dm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    dm = db.relationship("Employee", foreign_keys='Hackerrank.dm_id')

    hr_userid = db.Column(db.Text)

    cert_id = db.Column(db.Integer, db.ForeignKey('certification.id'))
    cert = db.relationship("Certification", foreign_keys='Hackerrank.cert_id')

    skill_id = db.Column(db.Integer, db.ForeignKey('skill.id'))
    skill = db.relationship("Skill", foreign_keys='Hackerrank.skill_id')

    badge = db.Column(db.Text)
    no_of_stars = db.Column(db.Text)
    contest_practice = db.Column(db.Text)
    date = db.Column(db.Text)
    score = db.Column(db.Integer)

class Winnercircle(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    emp_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    emp = db.relationship("Employee", foreign_keys='Winnercircle.emp_id')

    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'))
    project = db.relationship("Project", foreign_keys='Winnercircle.project_id')

    pm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    pm = db.relationship("Employee", foreign_keys='Winnercircle.pm_id')

    dm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    dm = db.relationship("Employee", foreign_keys='Winnercircle.dm_id')

    description = db.Column(db.Text)
    points = db.Column(db.Integer)
    received_from = db.Column(db.Text)
    date =  db.Column(db.Text)

class Trendnxt(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    emp_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    emp = db.relationship("Employee", foreign_keys='Trendnxt.emp_id')

    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'))
    project = db.relationship("Project", foreign_keys='Trendnxt.project_id')

    pm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    pm = db.relationship("Employee", foreign_keys='Trendnxt.pm_id')

    dm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    dm = db.relationship("Employee", foreign_keys='Trendnxt.dm_id')

    topic = db.Column(db.Text)
    points = db.Column(db.Integer)
    date = db.Column(db.Text)
    threshold_points = db.Column(db.Integer)
    financial_year = db.Column(db.Text)

class Topgearl(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    emp_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    emp = db.relationship("Employee", foreign_keys='Topgearl.emp_id')

    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'))
    project = db.relationship("Project", foreign_keys='Topgearl.project_id')

    pm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    pm = db.relationship("Employee", foreign_keys='Topgearl.pm_id')

    dm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    dm = db.relationship("Employee", foreign_keys='Topgearl.dm_id')

    topgearlearning_id = db.Column(db.Integer)
    certificate = db.Column(db.Text)
    date = db.Column(db.Text)


class Topgearc(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    emp_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    emp = db.relationship("Employee", foreign_keys='Topgearc.emp_id')

    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'))
    project = db.relationship("Project", foreign_keys='Topgearc.project_id')

    pm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    pm = db.relationship("Employee", foreign_keys='Topgearc.pm_id')

    dm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    dm = db.relationship("Employee", foreign_keys='Topgearc.dm_id')

    topgear_id = db.Column(db.Text)
    challenge_title = db.Column(db.Text)
    points = db.Column(db.Integer)
    cash_prize = db.Column(db.Integer)
    certificate = db.Column(db.Text)
    date = db.Column(db.Text)

class Pragati(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    emp_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    emp = db.relationship("Employee", foreign_keys='Pragati.emp_id')

    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'))
    project = db.relationship("Project", foreign_keys='Pragati.project_id')

    pm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    pm = db.relationship("Employee", foreign_keys='Pragati.pm_id')

    dm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    dm = db.relationship("Employee", foreign_keys='Pragati.dm_id')

    pragati_id = db.Column(db.Text)
    pragati_title = db.Column(db.Text)
    description = db.Column(db.Text)
    date = db.Column(db.Text)

class Shristi(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    emp_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    emp = db.relationship("Employee", foreign_keys='Shristi.emp_id')

    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'))
    project = db.relationship("Project", foreign_keys='Shristi.project_id')

    pm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    pm = db.relationship("Employee", foreign_keys='Shristi.pm_id')

    dm_id = db.Column(db.Integer, db.ForeignKey('employee.emp_id'))
    dm = db.relationship("Employee", foreign_keys='Shristi.dm_id')

    shristi_id = db.Column(db.Text)
    shristi_title = db.Column(db.Text)
    description = db.Column(db.Text)
    date = db.Column(db.Text)