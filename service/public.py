from service import app
from flask import request


@app.route('/getbody')
def getbody():
    filename = request.values['file']
    return app.send_static_file(filename+'.js')
