import time

class TIAdapter:
    __init__(self, name, type):
        self.__name = name
        self.__type = type
        self.__created_time = time()
        self.__updated_time = __created_time
        self.__description = ''
        self.__source = ''

    def update_timestamp(self):
        self.__updated_time = time()

    def set_type(self):
        self.__type = 

