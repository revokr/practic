from domain.examene import examen

class repo_examene:
    def __init__(self, path):
        self.__path = path
        self.__examene = []

    def adauga_examen(self, examen):
        '''
        :param examen: obiect de tip examen
        :return: introduce in lista repo examenul si il adauga in fisier
        '''
        self.__read_from_file()
        self.__examene.append(examen)
        self.__append_to_file(examen)

    def __read_from_file(self):
        '''
        :return: citeste toate elementele din fisier si le stocheaza in dictionarul de examene
        '''
        with open(self.__path, "r") as f:
            self.__examene.clear()
            lines = f.readlines()
            for line in lines:
                line = line.split(" ")
                materie = line[0]
                tip = line[1]
                data = line[2]
                ora = line[3]
                ex = examen(materie, tip, data, ora)
                self.__examene.append(ex)

    def __append_to_file(self, examen):
        '''
        :param examen: un obiect de tip examen
        :return: adauga obietul la fisier dupa toate obiectele deja existente in respectiv fisier
        '''
        with open(self.__path, "a") as f:
            f.write(str(examen)+"\n")


    def __len__(self):
        return len(self.__examene)
    def get_all(self):
        self.__read_from_file()
        return [self.__examene[x] for x in range(len(self.__examene))]
