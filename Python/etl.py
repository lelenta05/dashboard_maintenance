#importation des libairies de python
#pour la manipulation des matrices ou tableaux ,ainsi que les fonctions mathematiques
import numpy as np
#pour la transformation en dataframe et nettoyage
import pandas as pd

data = pd.read_csv('data/donnees_maintenance_simulees.csv')
data.head()

"""Informations sur les données"""

#information sur les colonnes et leurs types
data.info()

#Statistique descriptive sur notre dataframe : sur les valeurs numeriques ou decimal
data.describe()

"""Nettoyage et transformation"""

#Nombre de ligne et de colonnne
data.shape

#verification des valeurs manquantes
data.isnull().sum()

#verification si il y'a pas de doublons
data.duplicated().sum()

#Pour juste avoir les types des differentes colonnes
data.dtypes

#Normalisation des colonnes dates
data['DatePanne'] = pd.to_datetime(data['DatePanne'])
data['DateIntervention'] = pd.to_datetime(data['DateIntervention'])

data.dtypes

#telechargement du dataframe propre
data.to_csv('donnees_maintenance.csv',index=False)

