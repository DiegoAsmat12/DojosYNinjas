from dojos_app import app
from flask import render_template, request, redirect
from dojos_app.modelos.modelo_dojo import Dojo

@app.route("/")
def index():
    return redirect("/dojos")


@app.route("/dojos", methods=["GET"])
def paginaDojos():
    dojos = Dojo.obtenerDojos()
    print(dojos)
    return render_template("index.html", dojos=dojos)

@app.route("/dojos/create", methods=["POST"])
def crearDojo():
    dojo = {
        "nombre": request.form["dojo-name"]
    }
    resultado = Dojo.crearDojo(dojo)
    if(type(resultado) is bool and not resultado):
        print("Algo salio mal")
    return redirect("/")

@app.route("/dojos/<int:id>", methods=["GET"])
def paginaDojosConNinjas(id):
    dojo = {
        "dojo_id": id
    }
    dojoConNinjas = Dojo.obtenerDojoConNinjas(dojo)
    return render_template("dojo.html", dojo = dojoConNinjas)