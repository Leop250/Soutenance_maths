
import pandas as pd
from batiment import Batiment
from infra import Infra

class Planification:
    def __init__(self, arbre_df):
        """
        Initialisation de la planification en nettoyant les données et en préparant les objets nécessaires.
        """
        self.arbre_df = arbre_df.drop_duplicates()  # Suppression des doublons dans les données
        self.dict_of_infra, self.batiments = self.prepare_data()

    def prepare_data(self):
        """
        Prépare les données en regroupant les infrastructures et les bâtiments.
        Crée des objets Infra et Batiment à partir des données du DataFrame.
        """
        dict_of_infra = {
            infra_id: Infra(
                infra_id,
                infra_type,
                longueur,
                infra_df["nb_maisons"].sum()
            )
            for infra_id, (infra_type, longueur, infra_df) 
            in self.arbre_df.groupby("infra_id").apply(
                lambda df: (df["infra_type"].iloc[0], df["longueur"].iloc[0], df)
            ).items()
        }

        batiments = [
            Batiment(
                id_batiment,
                df["nb_maisons"].iloc[0],
                [
                    dict_of_infra[infra_id]
                    for infra_id in df["infra_id"]
                    if dict_of_infra[infra_id].infra_type == "a_remplacer"
                ]
            )
            for id_batiment, df in self.arbre_df.groupby("id_batiment")
            if any(
                dict_of_infra[infra_id].infra_type == "a_remplacer" 
                for infra_id in df["infra_id"]
            )
        ]
        
        return dict_of_infra, batiments

    def run_planification(self):
        """
        Exécute la planification des réparations en ordonnant les bâtiments par priorité (coût de réparation).
        Calcule les coûts totaux de chaque bâtiment et génère un rapport.
        """
        planification_data = []  # Liste pour stocker les résultats de la planification

        # Ordonne les bâtiments par priorité et les traite un par un
        for i, batiment in enumerate(
            sorted(self.batiments, key=lambda b: b.compute_total_cost()), 
            start=1
        ):
            infra_ids = []  # Liste pour stocker les identifiants des infrastructures
            total_cost = batiment.compute_total_cost()  # Calcul du coût total des infrastructures
            total_repair_cost = batiment.compute_repair_cost()  # Calcul du coût de réparation

            planification_data.append({
                "id_batiment": batiment.id_batiment,
                "infra_ids": ", ".join(map(str, [infra.infra_id for infra in batiment.infras])),  # Concaténation des infra_id
                "ordre": i,
                "coût_total": total_cost,
                "coût_reparation": total_repair_cost
            })

            # Marque les infrastructures comme réparées
            for infra in batiment.infras:
                infra.mark_as_built()

        # Conversion des données de la planification en DataFrame pour un rapport
        planification_df = pd.DataFrame(planification_data)

        # Affiche le DataFrame
        print(planification_df)

        # Exporte les résultats dans un fichier Excel
        planification_df.to_excel("planification_reparations_grouped.xlsx", index=False)
        print("Le fichier Excel 'planification_reparations_grouped.xlsx' a été généré avec succès.")
