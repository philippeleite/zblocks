from flask import Flask, render_template
from .utils import read_memory

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    cvt_address_buffer = bytearray(4)
    read_memory(cvt_address_buffer, 4, int("10", 16))
    cvt_address = int.from_bytes(cvt_address_buffer, byteorder='big')
    cvt_address_str = cvt_address_buffer.hex().upper()

    cvt_buffer = bytearray(1280)
    read_memory(cvt_buffer, 1280, cvt_address)
    cvt_str = cvt_buffer.hex().upper()

    return render_template("index.html", cvt_str=cvt_str, cvt_address_str=cvt_address_str)

if __name__ == '__main__':
    app.run()
