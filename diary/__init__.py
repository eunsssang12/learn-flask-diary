from flask import Flask

# Create APP
def create_app():
    app = Flask(__name__)
    app.config['SECRET KEY'] = 'sadfafdjsdlfjljslfjljl'
    
    return app