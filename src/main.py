#!/usr/bin/python3

from os import path
from flask import Flask
from jinja2 import Template

app = Flask("babar")
template_dir = "/usr/src/templates"


def read_template(name):
    template_path = path.join(template_dir, name)
    with open(template_path, "r") as f:
        html = f.read()
    template = Template(html)
    return template


@app.route("/")
def index():
    template = read_template("babar.html")
    return template.render(name="babar")
