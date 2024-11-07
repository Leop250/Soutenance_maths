

class Infra:
    def __init__(self, infra_id, infra_type, longueur, nombre_total_maisons):
        # Initialisation des attributs de l'infrastructure
        self.infra_id = infra_id
        self.infra_type = infra_type
        self.longueur = longueur
        self.nombre_total_maisons = nombre_total_maisons
        self.reparee = False  # Marque si l'infrastructure a été réparée

    def compute_metric(self):
        """
        Calcule une métrique pour l'infrastructure basée sur sa longueur et le nombre total de maisons.
        Si l'infrastructure est déjà existante, son coût est de 0.
        """
        # Si l'infrastructure est un "fourreau_existant", son coût est de 0
        return 0 if self.infra_type == "fourreau_existant" else self.longueur / self.nombre_total_maisons

    def mark_as_built(self):
        """
        Marque l'infrastructure comme réparée et change son type à 'fourreau_existant'.
        """
        self.infra_type = "fourreau_existant"
        self.reparee = True

    def compute_repair_cost(self):
        """
        Calcule le coût de réparation en fonction de la longueur de l'infrastructure.
        Si l'infrastructure est déjà réparée, le coût est de 0.
        """
        return self.longueur if not self.reparee else 0
