Recommandation de Culture
=========================

Cette fonctionnalité utilise des données collectées sur le terrain pour prédire la meilleure culture / semence à planter.  

Caractéristiques Utilisées
--------------------------

Les caractéristiques suivantes sont collectées et analysées pour effectuer les prédictions :  

- **N** : Ratio of Nitrogen content in soil - kg/ha.  
- **P** : Ratio of Phosphorous content in soil - kg/ha.  
- **K** : Ratio of Potassium content in soil - kg/ha.  
- **Température** : Température ambiante (°C).  
- **Humidité** : Taux d'humidité (%).  
- **pH** : Niveau de pH du sol.  
- **Pluviométrie** : Quantité de précipitations (mm).    

Modèles Entraînés
-----------------

Cinq modèles de machine learning ont été testés pour prédire la culture optimale à cultiver :  

- **LightGBM**  
- **Random Forest**
- **Support Vector Machine**
- **Neural Network** 
- **Naïve Bayes** 

Résultats et Meilleur Modèle
----------------------------

Parmi les modèles testés, le modèle **Naïve Bayes** a montré les meilleures performances, avec une précision de **99 %**.  
En raison de sa précision et de sa simplicité, il a été adopté pour cette fonctionnalité.

Conclusion
----------

La recommandation de culture permet aux agriculteurs d'optimiser leurs rendements en utilisant des analyses basées sur des données terrain. Grâce au modèle **Naïve Bayes**, l'application fournit des prédictions rapides et précises, adaptées aux conditions spécifiques de chaque champ.
