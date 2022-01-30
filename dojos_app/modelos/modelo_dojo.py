from dojos_app.config.mysqlconnection import MySQLConnection,connectToMySQL
from dojos_app.modelos.modelo_ninja import Ninja
class Dojo:
    def __init__(self, id,nombre,created_at,updated_at):
        self.id = id
        self.nombre=nombre
        self.created_at=created_at
        self.updated_at=updated_at
        self.ninjas:list[Ninja] = []

    def agregaNinja(self, ninja:Ninja):
        self.ninjas.append( ninja )

    @classmethod
    def crearDojo(cls,dojo):
        query = '''
                    INSERT INTO dojos(nombre, created_at, updated_at)
                    VALUES (%(nombre)s, NOW(), NOW())
                '''
        resultado = connectToMySQL("esquema_dojos_y_ninjas").query_db(query, dojo)
        return resultado

    @classmethod
    def obtenerDojos(cls):
        query = '''
                    SELECT * FROM dojos;
                '''

        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db( query )
        listaDojos = []
        for dojo in resultado:
            listaDojos.append(cls(dojo["id"], dojo["nombre"], dojo["created_at"], dojo["updated_at"]))
        return listaDojos

    @classmethod
    def obtenerDojoConNinjas(cls, dojo):
        query = '''
                    SELECT * FROM dojos
                    LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
                    WHERE dojos.id = %(dojo_id)s
                '''
        resultado = connectToMySQL('esquema_dojos_y_ninjas').query_db( query, dojo )
        dojoObtenido = cls(resultado[0]["id"], resultado[0]["nombre"], resultado[0]["created_at"], resultado[0]["updated_at"])
        for row in resultado:
            dojoObtenido.agregaNinja(Ninja(row["ninjas.id"],row["first_name"], row["last_name"], row["age"], row["dojo_id"],row["ninjas.created_at"], row["ninjas.updated_at"]))
        return dojoObtenido