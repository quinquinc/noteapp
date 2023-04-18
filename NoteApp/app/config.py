import os
import socket

postgres_host = 'postgres'
ip_address = socket.gethostbyname(postgres_host)

database = os.environ.get('POSTGRES_DB')
username= os.environ.get('POSTGRES_USER')
pwd = os.environ.get('POSTGRES_PASSWORD')
port_id = 5432

url= f'postgresql://{username}:{pwd}@{ip_address}:{port_id}/{database}'