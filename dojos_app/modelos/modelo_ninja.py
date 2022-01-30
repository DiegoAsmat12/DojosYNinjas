from dojos_app.config.mysqlconnection import MySQLConnection,connectToMySQL

class Ninja:
    def __init__(self, id, first_name, last_name, age, dojo_id, created_at, updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.dojo_id = dojo_id
        self.created_at= created_at
        self.updated_at= updated_at
    
    @classmethod
    def createNinja(cls, ninja):
        query = '''
                    INSERT INTO ninjas(first_name, last_name, age, dojo_id, created_at, updated_at)
                    VALUES(%(first_name)s,%(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW())
                '''
        resultado = connectToMySQL("esquema_dojos_y_ninjas").query_db(query, ninja)
        return resultado