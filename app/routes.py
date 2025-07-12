from flask import render_template, request, redirect, url_for
from app import app
from app.models.base import zblocks_list
from app.models.psa import PSA
from app.models.lcca import LCCA
from app.models.pcca import PCCA
from app.models.cvt import CVT
from app.models.ecvt import ECVT
from app.models.asvt import ASVT
from app.models.ascb import ASCB
from app.models.assb import ASSB
from app.models.jsab import JSAB
from app.models.asxb import ASXB
from app.models.acee import ACEE
from app.models.tcb import TCB

@app.template_test()
def flag(value, flags) -> bool:
    return value & flags != 0

@app.template_test()
def all_zero(value) -> bool:
    return int.from_bytes(value, byteorder='big') == 0

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
    ecvt = ECVT()
    return render_template("ecvt.html", block=ecvt)

@app.route('/asvt')
def asvt():
    asvt = ASVT()
    return render_template("asvt.html", block=asvt)

@app.route('/ascb')
@app.route('/ascb/<address>')
def ascb(address=None):
    ascb = ASCB(int(address, 16) if address else None)
    return render_template("ascb.html", block=ascb)

@app.route('/assb')
@app.route('/assb/<address>')
def assb(address=None):
    assb = ASSB(int(address, 16) if address else None)
    return render_template("assb.html", block=assb)

@app.route('/jsab')
@app.route('/jsab/<address>')
def jsab(address=None):
    jsab = JSAB(int(address, 16) if address else None)
    return render_template("jsab.html", block=jsab)

@app.route('/asxb')
@app.route('/asxb/<address>')
def asxb(address=None):
    asxb = ASXB(int(address, 16) if address else None)
    return render_template("asxb.html", block=asxb)

@app.route('/oucb')
@app.route('/oucb/<address>')
def oucb(address=None):
    pass

@app.route('/acee')
@app.route('/acee/<address>')
def acee(address=None):
    acee = ACEE(int(address, 16) if address else None)
    return render_template("acee.html", block=acee)

@app.route('/tcb/<address>')
def tcb(address):
    tcb = TCB(int(address,16))
    return render_template("tcb.html", block=tcb)