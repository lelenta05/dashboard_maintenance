import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Initialiser le générateur de nombres aléatoires
np.random.seed(42)
random.seed(42)

# Paramètres
N_LIGNES = 300

#le nom des machines 
machines = [f"MACH_{i}" for i in range(1, 9)]  # 8 machines

#type de panne detecte 
types_pannes = [
    "Panne électrique",
    "Panne mécanique",
    "Défaillance capteur",
    "Erreur logiciel",
    "Usure pièce"
]


techniciens = [
    "Technicien A",
    "Technicien B",
    "Technicien C",
    "Technicien D"
]

causes = [
    "Usure normale",
    "Mauvaise calibration",
    "Surcharge machine",
    "Défaut composant",
    "Erreur humaine"
]

# Génération des dates 
#2025
date_debut = datetime.now() - timedelta(days=365)
#2026
date_fin = datetime.now()

data = []

for _ in range(N_LIGNES):
    date_panne = date_debut + (date_fin - date_debut) * random.random()
    
    duree_arret = round(random.uniform(0.5, 12), 2)  # heures
    
    date_intervention = date_panne + timedelta(hours=duree_arret)

    data.append({
        "DatePanne": date_panne.date(),
        "MachineID": random.choice(machines),
        "TypePanne": random.choice(types_pannes),
        "DureeArret": duree_arret,
        "DateIntervention": date_intervention,
        "Technicien": random.choice(techniciens),
        "Cause": random.choice(causes)
    })

# Création DataFrame
df = pd.DataFrame(data)

# Tri chronologique en fonction de la date de panne 
df = df.sort_values("DatePanne").reset_index(drop=True)

# Export CSV
df.to_csv("donnees_maintenance_simulees.csv", index=False)