from flask import render_template, request, redirect, url_for
from app import app
from app.models.base import zblocks_list
from app.models.pcca import PCCA
from app.models.psa import PSA
from app.models.lcca import LCCA
from app.models.cvt import CVT

@app.template_test()
def flag(value, flags) -> bool:
    return value & flags != 0

@app.route('/')
def index():
    return render_template(
        "index.html",
        title="zBlocks",
        blocks=zblocks_list,
    )

@app.route('/psa')
def psa():
    psa = PSA()
    return render_template("psa.html", block=psa)

@app.route('/lcca')
def lcca():
    lcca = LCCA()
    return render_template("lcca.html", block=lcca)

@app.route('/pcca')
def pcca():
    pcca = PCCA()
    return render_template("pcca.html", block=pcca)

@app.route('/cvt')
def cvt_address():
    cvt = CVT()
    return render_template("cvt.html", block=cvt)

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