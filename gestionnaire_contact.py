import os
from contact import Contact
from utils import saisir_champ

class GestionnaireContact:
    def __init__(self):
        """
        Initialise la liste des contacts et charge les contacts depuis le fichier s'il existe.
        """
        self.liste_contact = []
        self.charger_contacts()

    

    def ajouter_contact(self, contact):
        """
        Ajoute un nouveau contact à la liste après vérification d'unicité (numéro et email).
        Si un contact avec le même téléphone ou email existe déjà, il ne sera pas ajouté.
        """
        for cont in self.liste_contact:
            if contact.get_telephone() == cont.get_telephone() or contact.get_email() == cont.get_email():
                print("Le contact existe déjà !")
                return
        self.liste_contact.append(contact)
        self.sauvegarder_contacts()
        print("Contact ajouté avec succès !")

    def afficher_contact(self):
        """
        Affiche tous les contacts enregistrés dans la liste.
        Si la liste est vide, affiche un message approprié.
        """
        if self.liste_contact:
            for cont in self.liste_contact:
                print(f"Nom : {cont.get_nom()} Prénom : {cont.get_prenom()} Téléphone : {cont.get_telephone()} Email : {cont.get_email()}")
        else:
            print("La liste des contacts est vide.")

    def rechercher_contact(self, nom):
        """
        Recherche un contact par son nom (insensible à la casse).
        Retourne le contact s'il est trouvé, sinon retourne None.
        """
        for cont in self.liste_contact:
            if nom.lower() == cont.get_nom().lower():
                return cont
        return None
    
    

    def modifier_contact(self, nom):
        """
        Modifie les informations d'un contact existant.
        L'utilisateur peut laisser un champ vide pour conserver l'ancienne valeur.
        """
        contact = self.rechercher_contact(nom)

        if contact:
            print("Laissez vide pour ne pas modifier.")

            # Utilisation de la fonction optimisée pour chaque champ
            contact.set_nom(saisir_champ("nom", contact.get_nom()))
            contact.set_prenom(saisir_champ("prénom", contact.get_prenom()))
            contact.set_email(saisir_champ("email", contact.get_email()))
            contact.set_telephone(saisir_champ("téléphone", contact.get_telephone()))

            self.sauvegarder_contacts()
            print("Contact modifié avec succès !")
        else:
            print("Contact introuvable.")


    

    def supprimer_contact(self, telephone):
        """
        Supprime un contact de la liste en fonction de son numéro de téléphone.
        Si le contact n'existe pas, affiche un message d'erreur.
        """
        telephone = str(telephone).strip()
        
        for cont in self.liste_contact:
            num_stocker = str(cont.get_telephone()).strip()  # Normaliser aussi les numéros stockés
            print(f"Comparaison : {repr(num_stocker)} vs {repr(telephone)}")  # Afficher chaque comparaison

            if num_stocker == telephone:
                contact_trouvé = True

        if not contact_trouvé:
            print(f"Aucun contact trouvé avec le téléphone {telephone}.")
            return  # Arrête la fonction si aucun contact trouvé

        # Supprimer le contact trouvé
        self.liste_contact = [cont for cont in self.liste_contact if str(cont.get_telephone()).strip() != telephone]
        print(f"Le contact avec le téléphone {telephone} a été supprimé.")

        self.sauvegarder_contacts()



    def sauvegarder_contacts(self):
        """
        Sauvegarde tous les contacts de la liste dans un fichier texte (liste_contact.txt).
        Chaque contact est stocké sous forme de ligne avec des valeurs séparées par des points-virgules.
        """
        with open("liste_contact.txt", "w", encoding="utf-8") as fichier:
            for contact in self.liste_contact:
                fichier.write(f"{contact.get_nom()};{contact.get_prenom()};{contact.get_email()};{contact.get_telephone()}\n")

    def charger_contacts(self):
        """
        Charge les contacts à partir d'un fichier texte (liste_contact.txt).
        Si le fichier n'existe pas, affiche un message et ne charge rien.
        """
        try:
            with open("liste_contact.txt", "r", encoding="utf-8") as fichier:
                for line in fichier:
                    nom, prenom, email, telephone = line.strip().split(";")
                    self.liste_contact.append(Contact(nom, prenom, email, telephone))
        except FileNotFoundError:
            print("Le fichier de contacts n'existe pas encore.")
