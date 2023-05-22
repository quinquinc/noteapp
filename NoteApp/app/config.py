import os
import socket

postgres_host = 'postgres'
ip_address = socket.gethostbyname(postgres_host)

database = os.environ.get('POSTGRES_DB')
username= os.environ.get('POSTGRES_USER')
pwd = os.environ.get('POSTGRES_PASSWORD')


url= f'postgresql://{username}:{pwd}@{ip_address}:5432/{database}'