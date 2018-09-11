#!/usr/bin/env python3

import connexion
from swagger_server import encoder
import os
import sqlalchemy
from swagger_server.postgres_utils import schemas

def create_database(user, pword, server_ip, port, database_name):
    """Create a database on the PostgreSQL server

    :param user: name of the connection user
    :param pword: password of the db user
    :param server_ip: ip address of the machine hosting the server
    :param port: port the server is exposed on
    :param database_name: name of the database

    :return None
    """
    engine = sqlalchemy.create_engine("postgresql://{user}:{pword}@{server_ip}:{port}" \
                                  .format(user=user, pword=pword, server_ip=server_ip, port=port))
    conn = engine.connect()
    conn.execute("commit")
    conn.execute("create database {database_name}".format(database_name=database_name))
    conn.close()

def create_tables(user, pword, server_ip, port, database_name):
    """Create a database on the PostgreSQL server

    :param user: name of the connection user
    :param pword: password of the db user
    :param server_ip: ip address of the machine hosting the server
    :param port: port the server is exposed on
    :param database_name: name of the database

    :return None
    """
    engine = sqlalchemy.create_engine("postgresql://{user}:{pword}@{server_ip}:{port}/{database_name}" \
                                  .format(user=user, pword=pword, server_ip=server_ip, port=port, database_name=database_name))

    conn = engine.connect()
    schemas.Base.metadata.create_all(conn)
    conn.close()

def main(user, pword, server_ip, port, database_name):
    try:
        create_database(user, pword, server_ip, port, database_name)
    except:
        pass

    create_tables(user, pword, server_ip, port, database_name)

    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'LadybugTools API'})
    app.run(port=8080)


if __name__ == '__main__':
    user = os.getenv("DB_USER")
    pword = os.getenv("PASSWORD")
    server_ip = os.getenv("SERVER_IP")
    port = os.getenv("PORT")
    database_name = os.getenv("DATABASE_NAME")

    main(user, pword, server_ip, port, database_name)
