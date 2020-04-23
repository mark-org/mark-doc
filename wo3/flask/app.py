
from flask import Flask, Blueprint
import os
from flask import render_template
import importlib
import glob

app = Flask(__name__)
profile = Blueprint('app', __name__, url_prefix='/xxx')
# app.register_blueprint(profile, url_prefix='/xxx')


for filename in glob.glob('./src/**/*_controller.py'):
    module_name = filename.replace("\\", "/").replace("./", "").replace("/", ".").replace(".py", "")
    print(module_name)
    metaclass = importlib.import_module(module_name)
    metaclass.add_url_rule(app, module_name.split(".")[1])


# @app1.error_handler(404)
# def a1404():
# return 'a1 404'

@app.route('/')
def hello_world():
    return 'Hello Worldx1234!xxxx'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('scan/xxx.html', name=name)



if __name__ == '__main__':
    print("-------1")
    # linux export FLASK_ENV=development
    # windows set FLASK_ENV=development
    os.system("set FLASK_ENV=development")

    app.run(debug=True)
