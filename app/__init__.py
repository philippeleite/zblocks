from flask import Flask


app = Flask(__name__, template_folder="/Users/philippeleite/PycharmProjects/zblocks/app/templates")

from app import routes
