import os

from flask import Flask, jsonify
from db import db

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
    db.init_app(app)

    return app


app = create_app()


@app.route('/')
def index():
    return 'hello world'


@app.route('/test_db')
def test_db():
    res = db.session.execute(
        """
            SELECT 1
        """
    ).scalar()

    return jsonify(
        {
            'result': res
        }
    )


if __name__ == '__main__':
    app.run()

