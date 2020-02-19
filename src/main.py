#!/usr/bin/python3

from flask import Flask, request, send_from_directory
from jinja2 import FileSystemLoader, Environment

app = Flask("babar")
loader = FileSystemLoader('/usr/src/templates')

env = Environment(
    loader=loader
)


class FormModel:
    def __init__(self, name=None, firm=None, amount=None, total=None, show=True):
        self.name = name
        self.firm = firm
        self.amount = amount
        self.total = total
        self.show = show


@app.route("/")
def index():
    template = env.get_template('index.html')
    tva = 5 + 5
    return template.render(name=str(tva))


@app.route("/css/bootstrap.css")
def boostrap():
    return send_from_directory('/usr/src/css/', 'bootstrap.css')


@app.route("/form.html", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        firm = request.form["firm"]
        amount = request.form["amount"]
        amount = float(amount)
        tva = amount * 0.21
        tot = amount + tva
        model = FormModel(name, firm, amount, tot)
    else:
        model = FormModel(name='test', show=False)

    template = env.get_template('form.html')
    # return template.render(name=name, firm=firm, amount=amount, tva=tva, tot=tot, ok=ok)
    return template.render(model=model)
