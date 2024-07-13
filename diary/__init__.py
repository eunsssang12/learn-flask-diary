from flask import Flask

# Create APP
def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'sadfafdjsdlfjljslfjljl'
    
    # Import Blueprint
    from .views import views
    from .auth import auth
    
    # Apply BluePrint
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    return app