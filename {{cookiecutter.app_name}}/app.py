import werkzeug
import gevent
import os
from flask import Flask


def create_app(config_object, env):
    '''An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    :param env: A string, the current environment. Either "dev" or "prod"
    '''
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config['ENV'] = env

    # Initialize SQLAlchemy
    # db.init_app(app)

    # Register blueprints
    # from {{cookiecutter.repo_name}}.modules import public, member
    # app.register_blueprint(public.blueprint)
    # app.register_blueprint(member.blueprint)

    return app


if __name__ == '__main__':
    # Get the environment setting from the system environment variable
    env = os.environ.get("ENV", "prod")
    app = create_app("{{cookiecutter.package_namespace}}."
                     "{{cookiecutter.app_name}}.settings.{env}Config"
                     .format(env=env.capitalize()), env)

    @werkzeug.serving.run_with_reloader
    def runServer():
        app.debug = True
        ws = gevent.wsgi.WSGIServer(('', 3000), app)
        ws.serve_forever()
