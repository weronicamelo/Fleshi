from appfleshi import app, database
from appfleshi.models import User, Photo, Comment

if __name__ == "__main__":
    with app.app_context():
        database.create_all()
        print("Banco e tabelas criadas com sucesso!")
