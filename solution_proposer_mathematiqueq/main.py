

import pandas as pd
from planification import Planification

def main():
    """
    Le point d'entrée principal pour charger les données et exécuter la planification.
    """
    # Lecture des données depuis un fichier CSV
    arbre_df = pd.read_csv("reseau_en_arbre.csv", sep=";")
    
    # Création d'une instance de la classe Planification pour exécuter la planification
    planificateur = Planification(arbre_df)
    planificateur.run_planification()

# Lancer le programme si le script est exécuté directement
if __name__ == "__main__":
    main()
