from flask import Flask
from flask_security import Security
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_security.utils import hash_password
from config import config

from api.models import db
from adminlte.admin import admin_db, admins_store, Role

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

Security(app, admins_store)

Migrate(app, db)
Migrate(app, admin_db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def recreate_admin_db():
    admin_db.drop_all()
    admin_db.create_all()
    admin_db.session.commit()


@manager.command
def create_admin_record():
    with app.app_context():
        super_admin_role = Role(name = 'superadmin')
        admin_role = Role(name = 'admin')
        admin_db.session.add(super_admin_role)
        admin_db.session.add(admin_role)
        admin_db.session.commit()

        test_user = admins_store.create_user(
            first_name = 'John',
            last_name = 'Doe',
            email = 'admin@admin.com',
            password = hash_password('admin'),
            roles = [super_admin_role, admin_role]
        )
        admin_db.session.add(test_user)
        admin_db.session.commit()
    return


if __name__ == '__main__':
    manager.run()
