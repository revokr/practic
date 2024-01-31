class examen:
    '''
    obiect clasificat dupa materie, tip, data, ora 
    '''
    def __init__(self, materie, tip, data, ora):
        self.__materie = materie
        self.__tip = tip
        self.__data = data
        self.__ora = ora

    def get_tip(self):
        return self.__tip
    def get_materie(self):
        return self.__materie
    def get_data(self):
        return self.__data
    def get_ora(self):
        return self.__ora

    def __str__(self):
        return f"{self.__materie} {self.__tip} {self.__data} {self.__ora}"

    def __eq__(self, other):
        return self.__materie == other.__materie and self.__tip == other.__tip

