from appfleshi import database, app
from appfleshi.models import Photo, User, Comment

with app.app_context():
    database.create_all()