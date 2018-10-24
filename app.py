from flask import Flask, url_for
from flask.blueprints import Blueprint
from flask_security import Security
from flask_admin import helpers as admin_helpers
from adminlte.admin import AdminLte, admins_store
from adminlte.views import FaLink
from config import config, host, port
import api.routes

from api.models import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
db.app = app


# AdminLTE Panel
security = Security(app, admins_store)
admin = AdminLte(app, skin = 'green', name = 'FlaskCMS', short_name = "<b>F</b>C", long_name = "<b>Flask</b>CMS")
admin.add_link(FaLink(name = "Documentation", icon_value = 'fa-book', icon_type = "fa", url = '/apidocs/'))


@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template = admin.base_template,
        admin_view = admin.index_view,
        h = admin_helpers,
        get_url = url_for
    )


# Blueprints
app.url_map.strict_slashes = False
for blueprint in vars(api.routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(host = host, port = port)
