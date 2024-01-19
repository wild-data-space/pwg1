class Classe():
    def __init__(self, nom):
        self.nom = nom
        self.etudiants = []
    def ajouter_etudiant(self,etudiant):
        self.etudiants.append(etudiant)
    def nombre_etudiants(self):
        return len(self.etudiants)
    def __repr__(self) -> str:
        return self.nom
    def __str__(self) -> str:
        return self.nom
    