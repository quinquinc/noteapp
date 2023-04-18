import os
import docker
import socket

# client = docker.from_env()
# container = client.containers.get('postgres')
# ip_address = container.attrs['NetworkSettings']['IPAddress']

postgres_host = 'postgres'
ip_address = socket.gethostbyname(postgres_host)

database = os.environ.get('POSTGRES_DB')
username= os.environ.get('POSTGRES_USER')
pwd = os.environ.get('POSTGRES_PASSWORD')
port_id = 5432

url= f'postgresql://{username}:{pwd}@{ip_address}:{port_id}/{database}'