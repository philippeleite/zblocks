from flask import render_template, request, redirect, url_for
from app import app
from app.models.base import zblocks_list
from app.models.cvt import CVT

@app.route('/')
def index():
    return render_template(
        "index.html",
        title="zBlocks",
        blocks=zblocks_list,
    )

@app.route('/psa')
def psa():
    pass

@app.route('/lcca')
def lcca():
    pass

@app.route('/pcca')
def pcca():
    pass

@app.route('/cvt')
def cvt_address():
    cvt = CVT()
    return render_template("block.html", block=cvt)

@app.route('/ecvt')
def ecvt():
    pass

@app.route('/asvt')
def asvt():
    pass

@app.route('/ascb')
@app.route('/ascb/<address>')
def ascb(address=None):
    _ = address

@app.route('/assb')
@app.route('/assb/<address>')
def assb(address=None):
    pass

@app.route('/jsab')
@app.route('/jsab/<address>')
def jsab(address=None):
    pass

@app.route('/asxb')
@app.route('/asxb/<address>')
def asxb(address=None):
    pass

@app.route('/oucb')
@app.route('/oucb/<address>')
def oucb(address=None):
    pass

@app.route('/acee')
@app.route('/acee/<address>')
def acee(address=None):
    pass