## Présentation du projet – Méthode STAR

### Situation
Ce projet a pour objectif de concevoir un **tableau de bord automatisé de suivi de la maintenance** à partir d’un fichier CSV simulant des données industrielles.  
Il a été réalisé dans le cadre de la préparation à un **stage**, afin de démontrer ma capacité à gérer des données, définir des KPI métier et produire un dashboard exploitable.

---

### Task 
Les missions réalisées dans ce projet sont les suivantes :
- Génération d’un fichier CSV simulant des données industrielles de maintenance
- Préparation et nettoyage des données selon le principe ETL
- Définition des indicateurs de performance (KPI)
- Modélisation des données dans Power BI
- Création d’un dashboard de maintenance interactif
- Documentation complète du projet

---

### Action
- Génération du fichier CSV à l’aide de **Python**, en utilisant les bibliothèques **Pandas** et **NumPy**, afin de produire des données représentatives d’un environnement industriel.
- Application du concept **ETL (Extract, Transform, Load)** pour préparer les données. Bien que généralement utilisé pour des gros volumes de donnée (Big data), ce choix permet d’apporter une valeur méthodologique au projet.
- Transformation et nettoyage des données :
  - Conversion des types de colonnes 
  - Formatage des dates (date et datetime)
  - Suppression des doublons
  - Traitement des valeurs aberrantes
- À noter que ces transformations peuvent également être réalisées directement dans **Power BI via Power Query**.
- Définition de quatre **KPI de maintenance** :
  - **MTBF (Mean Time Between Failures)** : temps moyen de fonctionnement d’une machine entre deux pannes  
    *Formule :* `MTBF = Temps total de production / Nombre de pannes`
  - **MTTR (Mean Time To Repair)** : temps moyen nécessaire à la réparation d’un équipement  
    *Formule :* `MTTR = Temps total de réparation / Nombre d’interventions`
  - **Taux de disponibilité** : proportion du temps où la machine est réellement disponible  
    *Formule :* `(Temps planifié – Temps d’arrêt) / Temps planifié`
  - **Nombre de pannes par machine** : identification des équipements les plus critiques
- Création du dashboard Power BI intégrant l’ensemble des KPI et des visualisations.

---

### Résultat
Le dashboard final permet :
- L’affichage clair de chaque **indicateur de performance (KPI)**
- L’analyse du nombre de pannes par année
- L’identification du nombre de machines en panne
- L’analyse de la disponibilité par machine
- Le suivi du taux de disponibilité global de l’ensemble des machines
- L’analyse du nombre de pannes par type ou cause
- Le suivi du nombre d’interventions par technicien
- La mise en place de filtres interactifs (date, MachineID, type de panne, cause)

---

### Conclusion
Ce projet démontre ma capacité à structurer un projet data de bout en bout, depuis la génération et la préparation des données jusqu’à la création d’un dashboard métier, tout en respectant une méthodologie claire et professionnelle.
