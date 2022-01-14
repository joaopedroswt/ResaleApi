import json
import mysql.connector

class Conexao:

    def select(self, sql):
        con = mysql.connector.connect(host='localhost', database='resale', user='root', password='159753')
        if con.is_connected():
            cursor = con.cursor()

            cursor.execute(sql)

            row_headers = [x[0] for x in cursor.description]
            rv = cursor.fetchall()
            json_data = []
            for result in rv:
                json_data.append(dict(zip(row_headers, result)))

            if json_data == []:
                json_data = [{'CodErro':99, 'Mensagem': 'Não foi encontrado nenum dado nesta consulta.'}]

            return json.loads(json.dumps(json_data))

    def executa(self, sql, param):
        con = mysql.connector.connect(host='localhost', database='resale', user='root', password='159753')
        if con.is_connected():
            try:
                cursor = con.cursor()
                cursor.execute(sql, param)
                con.commit()

            except Exception as e:
                print(f'Exception: {e}')

            pass