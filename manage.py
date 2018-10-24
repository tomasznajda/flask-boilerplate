from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import config

from api.models import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    manager.run()
