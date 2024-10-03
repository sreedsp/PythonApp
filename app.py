# app.py

from flask import Flask 

def create_app():
    app = Flask(__name__)
    @app.route('/')
    def home():
<<<<<<< HEAD
        return 'Hello Chatters-The web is still under construction'
=======
        return 'Hello Chatters - Welcome'
>>>>>>> a0d85e516c352c600220e48e70605f930e0cce06

    return app

    
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
