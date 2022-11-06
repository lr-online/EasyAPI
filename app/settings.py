import os
import json
from enum import Enum, unique

import nacos
from loguru import logger


# ----------------修复 nacos-sdk-python==0.1.9 中的bug----------------
def fixed_inject_version_info(self, headers):
    headers.update({"User-Agent": "Nacos-Python-Client:v" + nacos.client.VERSION})


nacos.client.NacosClient._inject_version_info = fixed_inject_version_info

# ----------------连接nacos----------------

NACOS_SERVER = os.getenv("NACOS_SERVER")
NACOS_NAMESPACE = os.getenv("NACOS_NAMESPACE")
NACOS_ENV = os.getenv("ENV", "prod")

client = nacos.NacosClient(NACOS_SERVER, namespace=NACOS_NAMESPACE)


@unique
class NacosConfigDataID(str, Enum):
    SERVER_CONFIG = "easy-api-srv"
    CONSUL_CONFIG = "easy-api-consul"


# ----------------本服务----------------
_server_config = json.loads(client.get_config(NacosConfigDataID.SERVER_CONFIG.value, NACOS_ENV))
SERVER_HOST = _server_config["SERVER_HOST"]
SERVER_PORT = _server_config["SERVER_PORT"]
SERVER_NAME = _server_config["SERVER_NAME"]

# ----------------服务注册 & 服务发现----------------
_consul_config = json.loads(client.get_config(NacosConfigDataID.CONSUL_CONFIG.value, NACOS_ENV))
CONSUL_HOST = _consul_config["CONSUL_HOST"]
CONSUL_PORT = _consul_config["CONSUL_PORT"]


# ----------------监听配置变化----------------
def on_config_changed(new_config: dict):
    # {
    #   'data_id': 'test',
    #   'group': 'prod',
    #   'namespace': '29c6a0a3-6a95-4517-b90d-103a335df065',
    #   'raw_content': '{\n    "ip": "1.2.3.5"\n}',
    #   'content': '{\n    "ip": "1.2.3.5"\n}'
    # }
    logger.info("配置文件发生变化")
    logger.info(new_config)


for data_id in NacosConfigDataID:
    client.add_config_watchers(data_id.value, NACOS_ENV, cb_list=[on_config_changed, ])
