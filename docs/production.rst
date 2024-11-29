Prédiction de la Production
===========================

Cette fonctionnalité utilise des données historiques et environnementales pour prédire la production agricole d'un champ donné.

Caractéristiques Utilisées
--------------------------

Les prédictions sont basées sur les caractéristiques suivantes :  

- **Area** : Superficie cultivée (en hectares).  
- **Item** : Type de culture ou produit agricole.  
- **Year** : Année de production.  
- **hg/ha_yield** : Rendement par hectare (en hectogrammes).  
- **average_rain_fall_mm_per_year** : Pluviométrie annuelle moyenne (en mm).  
- **pesticides_tonnes** : Quantité de pesticides utilisés (en tonnes).  
- **avg_temp** : Température moyenne (°C).  

Modèles Entraînés
-----------------

Huit modèles de régression ont été testés pour prédire la production agricole :  

- **Linear Regression** 
- **Lasso**  
- **Ridge**  
- **K-Nearest Neighbors** 
- **Decision Tree Regressor** 
- **Random Forest Regressor**  
- **Gradient Boosting**  
- **XGBoost** 

Résultats et Meilleur Modèle
----------------------------

Parmi les modèles testés, le modèle **Random Forest Regressor**  a montré les meilleures performances avec les métriques suivantes :  

- **MSE (Erreur Quadratique Moyenne)** : 9892.72  
- **R² Score** : 0.9867  

Grâce à ces résultats exceptionnels, ce modèle a été adopté pour cette fonctionnalité.

Conclusion
----------

La prédiction de la production permet aux agriculteurs de planifier leurs ressources et d'optimiser leurs rendements. En utilisant le modèle **Random Forest Regressor**, l'application fournit des prévisions fiables basées sur des données historiques et environnementales.
