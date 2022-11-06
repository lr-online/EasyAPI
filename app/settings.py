import os
import json

import nacos


NACOS_SERVER = os.getenv("NACOS_SERVER")
NACOS_NAMESPACE = os.getenv("NACOS_NAMESPACE")
NACOS_ENV = os.getenv("ENV", "prod")

client = nacos.NacosClient(NACOS_SERVER, namespace=NACOS_NAMESPACE)

# 本服务
_server_config = json.loads(client.get_config("easy-api-srv", NACOS_ENV))
SERVER_HOST = _server_config["SERVER_HOST"]
SERVER_PORT = _server_config["SERVER_PORT"]
SERVER_NAME = _server_config["SERVER_NAME"]

# 服务注册 & 服务发现
_consul_config = json.loads(client.get_config("easy-api-consul", NACOS_ENV))
CONSUL_HOST = _consul_config["CONSUL_HOST"]
CONSUL_PORT = _consul_config["CONSUL_PORT"]
