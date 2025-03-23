print("Lancement de l'application...")  

from gestionnaire_contact import GestionnaireContact
from contact import Contact

class Main:
    def __init__(self):
        self.gestionnaire = GestionnaireContact()

    def afficher_menu(self):
        print("\n--- Gestionnaire de Contacts ---")
        print("1. Ajouter un nouveau contact")
        print("2. Consulter la liste des contacts")
        print("3. Rechercher un contact par nom")
        print("4. Modifier un contact")
        print("5. Supprimer un contact")
        print("6. Quitter")

    def ajouter_contact(self):
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        email = input("Email : ")
        telephone = input("Téléphone : ")
        contact = Contact(nom, prenom, email, telephone)
        self.gestionnaire.ajouter_contact(contact)
        # print("Contact ajouté avec succès !")

    def afficher_contacts(self):
        self.gestionnaire.afficher_contact()

    def rechercher_contact(self):
        nom = input("Nom du contact à rechercher : ")
        contact = self.gestionnaire.rechercher_contact(nom)
        if contact:
            print(contact)
        else:
            print("Contact introuvable.")

    def modifier_contact(self):
        nom = input("Nom du contact à modifier : ")
        self.gestionnaire.modifier_contact(nom)

    def supprimer_contact(self):
        telephone = input("Téléphone du contact à supprimer : ")
        self.gestionnaire.supprimer_contact(telephone)
        
    def run(self):
        while True:
            self.afficher_menu()
            choix = input("Votre choix : ")
            if choix == "1":
                self.ajouter_contact()
            elif choix == "2":
                self.afficher_contacts()
            elif choix == "3":
                self.rechercher_contact()
            elif choix == "4":
                self.modifier_contact()
            elif choix == "5":
                self.supprimer_contact()
            elif choix == "6":
                print("Au revoir !")
                break
            else:
                print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
     print("Exécution de main.py...")  # Ajoute cette ligne aussi
     app = Main()
     app.run()