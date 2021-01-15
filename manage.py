import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main.models import user

from app.main import create_app, db
from flask_socketio import SocketIO

app = create_app('dev')

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

socketio = SocketIO(app)

@manager.command
def run():
    socketio.run(app)

if __name__ == '__main__':
    manager.run()
