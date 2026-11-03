import myPythonFunctions

try:
    # Demande le nom de l'utilisateur.
    userName = input("Entrez votre nom : ").strip()
    # Récupère le score sauvegardé. La fonction renvoie du texte.
    savedScore = myPythonFunctions.getUserPoint(userName)
    userScore = int(savedScore)
    # Si le score vaut -1, l'utilisateur n'existe pas encore.
    if userScore == -1:
        userScore = 0
        newUser=True
    else :
        newUser=False
    print("Bonjour " +userName+" !"+ " Votre score actuel est "+str(userScore)+".")
    # Le jeu continue tant que l'utilisateur ne saisit pas "-1".
    userChoice = ""
    while userChoice != "-1":
        # Pose une question ; la fonction renvoie 1 si juste, sinon 0.
        points = myPythonFunctions.generateQuestion()
        userScore += points
        print("Score actuel :", userScore)
        # Permet de quitter avant de poser une autre question.
        userChoice = input("Tapez Entrée pour continuer ou -1 pour terminer : ").strip()
    # Enregistre le score final, que l'utilisateur soit nouveau ou existant.
    myPythonFunctions.updateUserPoints(newUser, userName, userScore)
    print("Score sauvegardé : "+ str(userScore)+". Au revoir !")
except Exception as error:
    # Affiche un message si une erreur inattendue empêche le jeu de continuer.
    print("Une erreur est survenue :", error)
