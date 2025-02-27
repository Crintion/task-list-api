from flask import current_app
from app import db


class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    tasks = db.relationship('Task', backref= 'goal', lazy=True)


    def now_json(self):
        return {
            "id": self.goal_id,
            "title": self.title
        }

    def tasks_json(self):
        result = []
        for task in self.tasks:
            task = task.to_json()
            task["goal_id"] = self.goal_id
            result.append(task)
        return result  
        

    def full_json(self):
        return {
            "id": self.goal_id,
            "title": self.title,
            "tasks": self.tasks_json()
        }
                