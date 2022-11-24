from flask_bootstrap import Bootstrap
from app import create_app


app = create_app()
Bootstrap(app)


if __name__ == '__main__':
    app.run(debug=True)
