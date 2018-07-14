from views import db
import datetime

"""

The ForeignKey() and relationship() functions are dependent on the type of
relationship. In most One to Many relationships the ForeignKey() is placed on the
"many" side, while the relationship() is on the "one" side. The new field associated
with the relationship() function is not an actual field in the database. Instead, it simply
references the objects associated with the "many" side. This can be confusing at first,
but it should become clear after you go through an example.

"""
class Task(db.Model):

    __tablename__ = "tasks"

    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    posted_date = db.Column(db.Date, default=datetime.datetime.utcnow())
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, due_date, priority, posted_date, status, user_id):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.posted_date = posted_date
        self.status = status
        self.user_id = user_id
    def __repr__(self):
        return '<name {0}>'.format(self.name)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    tasks = db.relationship('Task', backref='poster')

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password
        
    def __repr__(self):
        return '<User {0}>'.format(self.name)