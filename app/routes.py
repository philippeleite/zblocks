from flask import render_template, request
from app import app
from app.models.cvt import CVT

@app.route('/')
def index():  # put application's code here
    return render_template("index.html", title="zBlocks")

@app.route('/cvt')
def cvt_address():
    cvt = CVT()
    return render_template("block.html", block=cvt)