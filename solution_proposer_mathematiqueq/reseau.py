import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Chargement de l'échantillon de données depuis votre fichier CSV
# Remplacez le chemin par celui de votre fichier
file_path = 'reseau_en_arbre.csv'
data = pd.read_csv(file_path, sep=";")

# Créez un sous-échantillon de données pour une visualisation miniature
sample_data = data.sample(n=10)  # Prend 10 lignes de l'échantillon, vous pouvez ajuster ce nombre

# Initialiser le graphe
G = nx.Graph()

# Ajouter les nœuds et les arêtes basées sur l'échantillon de données
for _, row in sample_data.iterrows():
    # Ajout des nœuds pour les bâtiments et les infrastructures avec des labels
    building_node = f"id_batiment_{row['id_batiment']}"
    infra_node = f"infra_id_{row['infra_id']}"

    # Ajout des nœuds dans le graphe
    G.add_node(building_node, type="batiment")
    G.add_node(infra_node, type="infrastructure")
    
    # Ajouter une arête avec la longueur de l'infrastructure comme poids
    G.add_edge(building_node, infra_node, longueur=row['longueur'])

# Options de visualisation
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)  # Seed pour une disposition fixe

# Définir les couleurs des nœuds
node_colors = ["lightblue" if G.nodes[node]["type"] == "batiment" else "lightgreen" for node in G.nodes]

# Affichage du graphe avec NetworkX
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=800)
nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold")
nx.draw_networkx_edges(G, pos, edge_color="gray")

# Affichage des poids sur les arêtes (longueur des infrastructures)
edge_labels = nx.get_edge_attributes(G, 'longueur')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Échantillon du Réseau d'Infrastructures")
plt.show()
