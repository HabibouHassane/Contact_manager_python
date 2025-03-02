class Contact:
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
    

class GestionnaireContact:
    #constructeur
        def __init__(self):
            self.liste_contact = []
            


        #fonction qui ajoute un contact à la liste des contactes
        def ajouter_contact(self,contact):
            for cont in self.liste_contact:
                if contact.get_telephone() == cont.get_telephone() or contact.get_email() == cont.get_email():
                    print("le contact exite deja!")
                    return 
            self.liste_contact.append(contact)
        
        #fonction qui affiche les contacts à


        def afficher_contact(self):
            for cont in self.liste_contact:
                print (f"Nom : {cont.get_nom()} Prénom : {cont.get_prenom()} Téléphone : {cont.get_telephone()} Mail : {cont.get_email()}") 

        #fonction qui recherche un contact par son nom
        def rechercher_contact(self,nom):
            for cont in self.liste_contact:
                if nom == cont.get_nom():
                    return cont
            return None
        
        # fonction qui supprime un contact par son telephone 
        def supprimer_contact(self, telephone):
            for i, cont in range (self.liste_contact):
                if telephone == cont.get_telephone():
                    del self.liste_contact[i]

    

        