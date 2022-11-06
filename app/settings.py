import os

# 本服务
SERVER_HOST = os.getenv("SERVER_HOST")
SERVER_PORT = int(os.getenv("SERVER_PORT"))
SERVER_NAME = os.getenv("SERVER_NAME")

# 服务注册 & 服务发现
CONSUL_HOST = os.getenv("CONSUL_HOST")
CONSUL_PORT = int(os.getenv("CONSUL_PORT"))
