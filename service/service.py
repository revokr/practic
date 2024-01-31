from repo.repo import repo_examene
from domain.examene import examen
import datetime

class service:
    def __init__(self, path):
        self.__repo = repo_examene(path)

    def adauga_examen(self, examen):
        '''
        :param examen: un obiect de tip examen
        :return: daca nu exista alt examen la acceasi materie si de acelasi tip adauga examenul in fisier
        '''
        materie = examen.get_materie()
        tip = examen.get_tip()
        l = self.__repo.get_all()
        for el in l:
            if materie == el.get_materie() and tip == el.get_tip():
                print("EXAMEN EXISTENT!!!\n" )
                return
        self.__repo.adauga_examen(examen)

    def sorteaza_ora(self):
        '''
        l: lista de obiecte
        sorteaza examenele din lista l dupa ora
        :return: lista sortata
        '''
        l = self.__repo.get_all()
        for j in range(0, len(l) - 1):
            ex = l[j]
            ora = ex.get_ora()
            ora = ora.split(":")
            minute = ora[1]
            ora = ora[0]
            for i in range(j + 1, len(l)):
                ex = l[i]
                ora1 = ex.get_ora()
                ora1 = ora1.split(":")
                minute1 = ora1[1]
                ora1 = ora1[0]
                if ora > ora1:
                    l[i], l[j] = l[j], l[i]
                if ora == ora1:
                    if minute > minute1:
                        l[i], l[j] = l[j], l[i]
            return l

    def sorteaza_ora2(self, l):
        for j in range(0, len(l) - 1):
            el = l[j]
            d = el.get_ora()
            d = d.split(":")
            d_ora = d[0]
            d_minute = d[1]
            for i in range(j+1, len(l)):
                ex = l[i]
                d1 = ex.get_ora()
                d1 = d1.split(":")
                minute1 = d1[1]
                ora1 = d1[0]
                if d_ora > ora1:
                    l[j], l[i] = l[i], l[j]
                if d_ora == ora1:
                    if d_minute > minute1:
                        l[j], l[i] = l[i], l[j]
            return l

    def sorteaza_data(self, l):
        '''
        l : lista cu examenele pe care le sorteaza functia
            sorteaza examenele din lista dupa data
        :return: lista sortata
        '''
        for j in range(0, len(l) - 1):
            ex = l[j]
            ora = ex.get_data()
            ora = ora.split(".")
            luna = ora[1]
            zi = ora[0]
            for i in range(j + 1, len(l)):
                ex = l[i]
                ora1 = ex.get_data()
                ora1 = ora1.split(".")
                luna1 = ora1[1]
                zi1 = ora1[0]
                if luna > luna1:
                    l[i], l[j] = l[j], l[i]
                if ora == ora1:
                    if zi > zi1:
                        l[i], l[j] = l[j], l[i]
            return l


    def get_all(self):
        return self.__repo.get_all()
