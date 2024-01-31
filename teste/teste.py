from repo.repo import repo_examene
from domain.examene import examen
from service.service import service

class teste:
    def ruleaza(self):
        self.__teste_repo()
        self.__teste_service()
        print("teste finalizate cu succes")
        self.clear_file()

    def __teste_repo(self):
        repo = repo_examene("C:\\Users\\rafael\\PycharmProjects\\practic\\test.txt")
        ex = examen("FP", "normal", "12.07", "17:30")
        repo.adauga_examen(ex)
        assert len(repo) == 1
        l = repo.get_all()
        assert len(l) == 1

    def __teste_service(self):
        Service = service("C:\\Users\\rafael\\PycharmProjects\\practic\\test.txt")
        ex = examen("FP", "restanta", "11.07", "12:30")
        Service.adauga_examen(ex)
        l2 = Service.get_all()
        assert len(l2) == 2
        l = Service.sorteaza_ora()
        assert l[0] == ex
        l1 = Service.sorteaza_data(l)
        assert l1[0] == ex




    def clear_file(self):
        with open("C:\\Users\\rafael\\PycharmProjects\\practic\\test.txt", "w") as f:
                f.write("")

