# batiment.py

from infra import Infra

class Batiment:
    def __init__(self, id_batiment, nb_maisons, infras):
        """
        Initialisation d'un bâtiment avec son ID, son nombre de maisons et ses infrastructures associées.
        """
        self.id_batiment = id_batiment
        self.nb_maisons = nb_maisons
        self.infras = infras  # Liste des infrastructures associées au bâtiment

    def compute_total_cost(self):
        """
        Calcule le coût total des infrastructures d'un bâtiment, en utilisant la formule indiquée :
        coût_{i,j} = (longueur_j / nombre_total_maisons_j) * nb_maisons_i
        """
        total_cost = 0
        for infra in self.infras:
            # Calcul du coût pour chaque infrastructure associée
            cost_per_infra = (infra.longueur / infra.nombre_total_maisons) * self.nb_maisons
            total_cost += cost_per_infra
        return total_cost

    def compute_repair_cost(self):
        """
        Calcule le coût total de réparation pour le bâtiment, en fonction des infrastructures à réparer.
        Exclut les infrastructures déjà réparées du calcul.
        """
        # Calcule le coût total de réparation en excluant celles déjà réparées
        return sum(infra.compute_repair_cost() for infra in self.infras if not infra.reparee)

    def __lt__(self, other):
        """
        Comparaison des bâtiments en fonction de leur coût total.
        Le bâtiment avec le coût total le plus faible sera traité en premier.
        """
        return self.compute_total_cost() < other.compute_total_cost()
