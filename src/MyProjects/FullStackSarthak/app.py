from flask import Flask

def myFirstApp():
    app = Flask(__name__)
    from FullStackSarthak.src.views import views
    from FullStackSarthak.src.auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

app = myFirstApp()

if __name__ == '__main__':
    app.run(debug=True)