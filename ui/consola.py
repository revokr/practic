from service.service import service
from domain.examene import examen
import datetime
import fileinput

class consola:
    def __init__(self, path):
        self.__service = service(path)

    def __ui_trei_zile(self, zi_, luna_):
        '''
        :param zi_: un numar intreg >= 1 si <= 31
        :param luna_: un numar intreg >= 1 si <= 12
        :return: printeaza un tabel cu examenele din urmatoarele
                 trei zile dupa data introdusa
        '''
        l1 = self.__service.sorteaza_ora()
        l = self.__service.sorteaza_data(l1)
        for el in l:

            data_el = el.get_data()
            data_el = data_el.split(".")
            zi = int(data_el[0])
            luna = int(data_el[1])
            Data = datetime.date(day=zi, month=luna, year=2024) - datetime.date(day=zi_, month=luna_, year=2024)
            if Data.days <= 3 and Data.days >= 0:
                print("_______________________________________")
                print(el)
                print("_______________________________________")


    def __sortat_ora(self):
        l1 = self.__service.get_all()
        l = self.__service.sorteaza_ora2(l1)
        for el in l:
            print(str(el))

    def __ui_print_examene(self):
        '''
        :return: printeaza examenele din ziua urmatoare ordonate dupa ora la care se desfasoara
        '''
        l = self.__service.get_all()
        l1 = []
        a = datetime.date.today()
        day = a.day
        mo = a.month
        for el in l:
            data = el.get_data()
            data = data.split(".")
            zi = int(data[0])
            luna = int(data[1])
            data_el = datetime.date(day=zi, month=luna, year=2024) - a
            if data_el.days == 1:
                l1.append(el)
        l13 = self.__service.sorteaza_ora2(l1)
        for el in l13:
            print(str(el))



    def __ui_adauga(self, params):
        '''

        :param params: o lista de stringuri ce reprezinta materia, tipul, data, ora obiectului examen
        :return: daca nu mai exista un examen la aceeasi materie si de acelasi tip il adauga in fisier
        '''
        materie = params[0]
        tip = params[1]
        data = params[2]
        ora = params[3]
        ex = examen(materie, tip, data, ora)
        self.__service.adauga_examen(ex)


    def __ui_creeaza_fisier(self, nume_fisier, string):
        '''

        :param nume_fisier: nume de fisier care se termina in .txt
        :param string: un string oarecare
        :return: functia creeaza un fisier cu numele nume_fisier si adauga in zis fisier
                 examenele care au in materie sirul string
        '''
        fisier = "C:\\Users\\rafael\\PycharmProjects\\practic\\" + nume_fisier
        l1 = self.__service.get_all()
        l = self.__service.sorteaza_data(l1)

        with open(fisier, "a") as f:
            for el in l:
                materie = el.get_materie()
                if string in materie:
                    f.write(str(el)+"\n")

    def run(self):
        data__ = datetime.date.today()
        while True:
            if data__ == datetime.date.today():
                self.__ui_print_examene()
            else:
                self.__ui_trei_zile(data__.day, data__.month)
            n = input(">>>")
            n = n.split(" ")
            exe = n[0]
            params = n[1:]
            if exe == "x":
                return False
            if exe == "adauga":
                self.__ui_adauga(params)
            if exe == "setez_data":
                zi = int(params[0])
                luna = int(params[1])
                data__1 = datetime.date(day=zi, month=luna, year=2024)
                data__ = data__1
            if exe == "creeaza":
                nume = params[0]
                string = params[1]
                self.__ui_creeaza_fisier(nume, string)
            if exe == "ora":
                self.__sortat_ora()
