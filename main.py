from classes import Contact, GestionnaireContact

gestion = GestionnaireContact()

contact1 = Contact("nasser", "Habibou", "habibouhassaneabdoulnasser@gmail.com", "0751256044")
contact2 = Contact("nasser", "Habibou", "habibouhassaneabdoulnasser123@gmail.com", "0752256044")


gestion.ajouter_contact(contact1)
gestion.ajouter_contact(contact2)


gestion.afficher_contact()

nom = "Kader"
contact_chercher = gestion.rechercher_contact(nom)
if contact_chercher :
    print(f"le contact avec le nom : {nom} à comme information : Nom: {contact_chercher.get_nom()} Prenom: {contact_chercher.get_prenom()} Email: {contact_chercher.get_email()} Telephone: {contact_chercher.get_telephone()}")
else :
    print(f"le contact avec le nom {nom} n'est pas enregistrer")


