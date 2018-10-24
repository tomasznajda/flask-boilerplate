from flask import Flask
from flask.blueprints import Blueprint
from config import config, host, port
import api.routes

from api.models import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
db.app = app


# Blueprints
app.url_map.strict_slashes = False
for blueprint in vars(api.routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(host = host, port = port)
