from flask import Flask


def create_app():
    app = Flask('game')
    from .game_resource import bp
    app.register_blueprint(bp)
    return app
