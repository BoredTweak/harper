from typing import List
from os import path, getcwd

class Configuration: 
    data: List[str]

    def __init__(self):
        __config__ = path.realpath(path.join(getcwd(), path.dirname(__file__), 'config.txt'))
        with open(__config__, 'r') as file:
            content = file.read()
            self.data = list(filter(None, content.split('\n')))
