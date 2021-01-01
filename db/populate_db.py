from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import getenv
import csv

load_dotenv()

user = getenv("PODEMOS_DB_USER")
password = getenv("PODEMOS_DB_PASS")
db_url = getenv("PODEMOS_DB_URL")
db_port = getenv("PODEMOS_DB_PORT")
db_uri = f"mysql+pymysql://{user}:{password}@{db_url}:{db_port}"

engine = create_engine(db_uri)

with engine.connect() as con:
    with open('db_initial_values/data_clientes.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                con.execute(f"INSERT INTO podemos_eval.Clientes(id, nombre) VALUES ('{row[0]}', '{row[1]}');")
                line_count += 1
    with open('db_initial_values/data_grupos.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                nombre = row[1].replace("'","''")
                con.execute(f"INSERT INTO podemos_eval.Grupos(id, nombre) VALUES ('{row[0]}', '{nombre}');")
                line_count += 1
    with open('db_initial_values/data_miembros.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                con.execute(f"INSERT INTO podemos_eval.Miembros(grupo_id, cliente_id) VALUES ('{row[0]}', '{row[1]}');")
                line_count += 1
    with open('db_initial_values/data_cuentas.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                con.execute(f"INSERT INTO podemos_eval.Cuentas(id, grupo_id, estatus, monto, saldo) VALUES ('{row[0]}', '{row[1]}', '{row[2]}', {row[3]}, {row[4]});")
                line_count += 1
    with open('db_initial_values/data_calendariopagos.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                con.execute(f"INSERT INTO podemos_eval.CalendarioPagos(id, cuenta_id, num_pago, monto, fecha_pago, estatus) VALUES ({row[0]}, '{row[1]}', {row[2]}, {row[3]}, '{row[4]}', '{row[5]}');")
                line_count += 1
    with open('db_initial_values/data_transacciones.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                con.execute(f"INSERT INTO podemos_eval.Transacciones(id, cuenta_id, fecha, monto) VALUES ({row[0]}, '{row[1]}', '{row[2]}', {row[3]});")
                line_count += 1