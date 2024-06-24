from fastapi import FastAPI # type: ignore
from core.config import settings

class App(FastAPI):
    def __init__(self, *args, **kwargs)-> None:
        super().__init__(
            *args, 
            **kwargs, 
            version= "0.0.1",
            title = settings.PROJECT_NAME,
            rootpath = settings.ROOT_PATH)

app = App()

