from fastapi import FastAPI

from src.cloud_services.cloud_service import CloudService


class Server:
    _host : str
    _port : int
    _app : FastAPI
    _service : CloudService

    def __init__(self, host : str, port : int):
        pass

    def start(self, service : CloudService):
        pass

    def stop(self):
        pass

    def load(self, content : any):
        pass