from datetime import date
from Gestion import Classe

class Personne:
    def __init__(self, nom: str, prenom: str, cin: str, date_naissance: date):
        self.nom = nom
        self.prenom = prenom
        self.cin = cin
        self.date_naissance = date_naissance

    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_naissance.year - ((today.month, today.day) < (self.date_naissance.month, self.date_naissance.day))
        return age

    def intro(self):
        print(f"Nome: {self.nom}",
              f"Prenom: {self.prenom}",
              f"CIN: {self.cin}",
              f"Age: {self.calculate_age()}",
              sep='\n'
              )

class Etudiant(Personne):
    def __init__(self, nom: str, prenom: str, cin: str, date_naissance: date, classe: Classe, notes: dict):
        super().__init__(nom, prenom, cin, date_naissance)
        if not isinstance(classe, Classe):
            raise NameError("La classe declaree n'exsiste pas.")
        self.classe = classe
        classe.ajouter_etudiant(self)
        self.notes = notes

    def a_reussit(self):
        notes = [v for k, v in self.notes.items()]
        if sum(notes) / len(notes) >= 10:
            return True
        return False

    @classmethod
    def from_dict(cls, data: dict, classe_instance: Classe):
        return cls(
            nom=data['nom'],
            prenom=data['prenom'],
            cin = data['cin'],
            date_naissance=data['date_naissance'],
            classe=classe_instance,
            notes=data['notes']
        )
classe1 = Classe('C1')
data = {
    'nom': 'IDRISSI AZAMI',
    'prenom': 'Abdellah',
    'date_naissance': date(1994, 5, 9),
    'cin':'AD231907',
    'classe': classe1,
    'notes': {
        'M1': 10,
        'M2': 15
    }
}

etudiant1 = Etudiant.from_dict(data, data['classe'])
print(etudiant1.a_reussit())
print(etudiant1.classe)