class Contat :
    #constructeur
    def __init__(self,nom,prenom, email,telephone):
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone

    # getters and setters
    def set_nom(self,nom):
        self.nom = nom
    
    def set_prenom(self,prenom):
        self.prenom = prenom

    def set_email(self,email):
        self.email = email

    def set_telephone(self,telephone):
        self.telephone = telephone


    def get_nom(self):
        return self.nom 
    
    def get_prenom(self):
        return self.prenom

    def get_email(self):
        return self.email

    def get_telephone(self):
        return self.telephone
    
    #methode __str__ pour l'affichage d'un contact
    def __str__(self):
        return f"{self.prenom}{self.get_nom}, Email : {self.email}, Telephone: {self.telephone}" 
    