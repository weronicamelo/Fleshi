from appfleshi import app, database
from flask_migrate import Migrate

migrate = Migrate(app, database)

if __name__ == '__main__':
    app.run(debug=True)
