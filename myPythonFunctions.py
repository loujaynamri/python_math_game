import random
import os
def getUserPoint(userName):
    try:
        file = open("userScores.txt", "r")
        line = file.readline()
        while line != "":
            # Sépare le nom et le score.
            parts = line.strip().split(",")
            if len(parts) == 2:
                name = parts[0].strip()
                score = parts[1].strip()
                # Vérifie si le nom correspond.
                if name == userName:
                    file.close()
                    return score
            # Lit la ligne suivante.
            line = file.readline()
        file.close()
    except FileNotFoundError:
        pass
    # Utilisateur non trouvé.
    return "-1"

def updateUserPoints(newUser, userName, score):
    # Un nouvel utilisateur : ajoute simplement son nom et son score à la fin.
    if newUser:
        file=open("userScores.txt", "a")
        file.write(userName+","+str(score)+"\n")
    else:
       # Un utilisateur existant : réécrit le fichier via un fichier temporaire.
        old_file = open("userScores.txt", "r")
        temp_file = open("userScores.tmp", "w")
        line = old_file.readline()
        while line != "":
            parts = line.strip().split(",")
            if len(parts) == 2 and parts[0].strip() == userName:
                # Remplace le score de l'utilisateur trouvé.
                temp_file.write(userName+','+str(score)+"\n")
            else:
                # Conserve toutes les autres lignes.
                temp_file.write(line)

            line = old_file.readline()

        # Ferme les fichiers.
        old_file.close()
        temp_file.close()

        # Remplace le fichier original par le fichier temporaire.
        os.replace("userScores.tmp", "userScores.txt")
def generateQuestion():
    # Cinq opérandes : cinq nombres utilisés dans l'expression.
    operandList = [0, 0, 0, 0, 0]
    # Quatre opérateurs : un opérateur entre chaque paire de nombres.
    operatorList = ["", "", "", ""]
    # Chaque clé permet de choisir un opérateur au hasard.
    operatorDict = {
    1: "+",
    2: "-",
    3: "*",
    4: "**"
    }
    # Remplit la liste avec des entiers aléatoires entre 0 et 9.
    for i in range(len(operandList)):
        operandList[i] = random.randint(0, 9)
    # Choisit quatre opérateurs au hasard.
    for i in range(len(operatorList)):
        operatorList[i] = operatorDict[random.randint(1, 4)]
        # Évite deux puissances consécutives, comme ** suivi de **.
        if i > 0 and operatorList[i] == "**" and operatorList[i - 1] == "**":
            operatorList[i] = "+"
    # Assemble nombres et opérateurs en une seule chaîne.
    # Exemple : "6 - 2 * 3 + 2**2".
    questionString = str(operandList[0])
    for i in range(len(operatorList)):
        questionString += " " + str(operatorList[i] )+ " " + str(operandList[i + 1])
    # Calcule la bonne réponse à partir de l'expression construite.
    result = eval(questionString)
    # Affiche les puissances avec ^, plus lisible pour l'utilisateur.
    displayedQuestion = questionString.replace("**", "^")
    print("\nQuestion :", displayedQuestion)
    # Demande un entier. Si l'entrée n'est pas un entier, redemande.
    while True:
        try:
            answer = int(input("Votre réponse : "))
            # Compare la réponse saisie à la réponse calculée.
            if answer == result:
                print("Correct ! Vous gagnez 1 point.")
                return 1
            else:
                print("Incorrect. La bonne réponse est :", result)
                return 0
        except ValueError:
            print("Erreur : veuillez saisir un nombre entier.")





            
