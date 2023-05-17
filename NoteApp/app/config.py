import os
import socket

postgres_host = 'postgres'
ip_address = socket.gethostbyname(postgres_host)

database = os.environ.get('POSTGRES_DB')
username= os.environ.get('POSTGRES_USER')
pwd = os.environ.get('POSTGRES_PASSWORD')
port_id = 5432

url= f'postgresql://{username}:{pwd}@terraform-20230517123017087400000002.cpj4tdtofjrz.eu-west-3.rds.amazonaws.com:5432:{port_id}/{database}'