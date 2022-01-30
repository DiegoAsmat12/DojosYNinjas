from dojos_app import app
from flask import render_template, request,redirect
from dojos_app.modelos import modelo_dojo, modelo_ninja

@app.route("/ninjas", methods=["GET"])
def renderNinja():
    dojos = modelo_dojo.Dojo.obtenerDojos()
    return render_template('ninja.html',dojos = dojos)

@app.route("/ninjas/create", methods=["POST"])
def createNinja():
    ninja={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "age":request.form["age"],
        "dojo_id":request.form["dojo_id"]
    }
    resultado = modelo_ninja.Ninja.createNinja(ninja)
    if(type(resultado) is bool and not resultado):
        print("Algo salio mal")
    return redirect("/")