from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins(self)

    def getAllCorsi(self):
        return DAO.getAllCorsi(self)

    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPDwIscritti(self, pd):
        result = DAO.getCorsiPDwIscritti(pd)
        result.sort(key = lambda s:s[1], reverse = True)
        return result

    def getStudentiCorso(self, codins):
        studenti = DAO.getStudenticorso(codins)
        studenti.sort(key = lambda s:s.cognome)
        return studenti