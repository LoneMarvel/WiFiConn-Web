from flask import Flask
import sys
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fa1f944ab8bd63090d9d4bc945bc0dfd'

from app import routes