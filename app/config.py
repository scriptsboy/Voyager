import docker
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOCKER_CLIENT = docker.from_env()

# AWVS配置相关
AWVS_API_KEY = "1986ad8c0a5b3df4d7028d5f3c06e936cb2bb5b2fe8454374af5bc8e350ec2da6"
AWVS_HOST_ADDRESS = "https://127.0.0.1:13443/"


# Flask配置文件
class BaseConfig(object):
    MONGO_URI = "mongodb://root:shad0wBrok3r@127.0.0.1:27017/pioneer1?authSource=admin"
    SECRET_KEY = "NEVEW"


class DevConfig(BaseConfig):
    DEBUG = True
