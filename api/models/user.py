from . import db
from .abc import BaseModel


class User(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255), nullable = False)
    age = db.Column(db.Integer, nullable = True)
    created_at = db.Column(db.DateTime, server_default = db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, server_default = db.func.current_timestamp(),
                           onupdate = db.func.current_timestamp())

    to_json_filter = (created_at, updated_at)

    def __str__(self):
        return self.first_name + " " + self.last_name
