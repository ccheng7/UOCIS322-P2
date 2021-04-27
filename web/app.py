"""
cheng cheng's Flask API.
"""

from flask import Flask, render_template,abort
import os 

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
@app.route("/<path:web>")
def send(wp):
    wp = f'{DOCROOT}{wp}'
    if "//" or  "~" or ".." in web:
        abort(403)
    elif os.path.isfile(wp):
        f=open(wp, 'r')
        return f.read(), 200
    else:
        abort(404)




    






@qpp.errorhandler(403)
def error_403(e):
    return render_remplate("403.html")

@app.errorhandler(404)
def erroe404(e):
    return render_templete("404.html")

