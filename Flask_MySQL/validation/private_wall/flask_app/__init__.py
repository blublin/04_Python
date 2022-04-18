from flask_bcrypt import Bcrypt
from flask import Flask, session, flash
import re

app = Flask(__name__)
# generated from 1password on 4/17/2022
app.secret_key = "G.azTyvzq3*o6t6NqfQU"