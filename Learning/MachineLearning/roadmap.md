# Machine Learning — From Hero to Zero

**Complete learning roadmap | Beginner → Intermediate → Advanced**

This syllabus mirrors the LangChain track in this repository: eight categories, three levels each, theory in `.md` files and hands-on work in `.ipynb` notebooks.

---

## Phase 0: Machine Learning Foundations

Build ML concepts, mathematics, datasets, and Python libraries before algorithm-specific modules.

| Lesson | Exercise |
| ------ | -------- |
| [0.0 Getting Started](00_foundations/0.0_getting_started.md) | — |
| [0.1 Machine Learning Mental Model](00_foundations/0.1_ml_mental_model.md) | — |
| [0.2 Types of Machine Learning](00_foundations/0.2_types_of_ml.md) | — |
| [0.3 Python for Machine Learning](00_foundations/0.3_python_for_ml.md) | [0.3](../../Exercises/MachineLearning/00_foundations/0.3_python_for_ml.ipynb) |
| [0.4 Mathematics for ML](00_foundations/0.4_mathematics.md) | — |
| [0.5 Data Understanding & EDA](00_foundations/0.5_eda.md) | [0.5](../../Exercises/MachineLearning/00_foundations/0.5_eda.ipynb) |
| [0.6 Data Preprocessing](00_foundations/0.6_preprocessing.md) | [0.6](../../Exercises/MachineLearning/00_foundations/0.6_preprocessing.ipynb) |
| [0.7 Training & Testing](00_foundations/0.7_train_test.md) | [0.7](../../Exercises/MachineLearning/00_foundations/0.7_train_test.ipynb) |
| [0.8 Model Evaluation Fundamentals](00_foundations/0.8_evaluation.md) | — |
| [0.9 CRISP-DM Workflow](00_foundations/0.9_crisp_dm.md) | [0.9](../../Exercises/MachineLearning/00_foundations/0.9_crisp_dm.ipynb) |

**Duration (guide):** 2–3 weeks at 5–7 h/week.

---

## 01 · Regression

**Supervised learning** — predict continuous values (prices, revenue, temperature).  
**Core algorithm:** Linear Regression  
**Capstone:** [Property tax revenue](../../Projects/MachineLearning/01_property_tax_prediction/README.md)

### Beginner

- [1.1 Introduction to Regression](01_regression/01_beginner/1.1_intro_regression.md)
- [1.2 Simple Linear Regression](01_regression/01_beginner/1.2_simple_linear.md) · [Exercise](../../Exercises/MachineLearning/01_regression/01_beginner/1.2_simple_linear.ipynb)
- [1.3 Multiple Linear Regression](01_regression/01_beginner/1.3_multiple_linear.md) · [Exercise](../../Exercises/MachineLearning/01_regression/01_beginner/1.3_multiple_linear.ipynb)
- [1.4 Regression Evaluation](01_regression/01_beginner/1.4_evaluation.md) · [Exercise](../../Exercises/MachineLearning/01_regression/01_beginner/1.4_evaluation.ipynb)

### Intermediate

- [2.1 Gradient Descent](01_regression/02_intermediate/2.1_gradient_descent.md) · [Exercise](../../Exercises/MachineLearning/01_regression/02_intermediate/2.1_gradient_descent.ipynb)
- [2.2 Polynomial Regression](01_regression/02_intermediate/2.2_polynomial.md) · [Exercise](../../Exercises/MachineLearning/01_regression/02_intermediate/2.2_polynomial.ipynb)
- [2.3 Ridge, Lasso & ElasticNet](01_regression/02_intermediate/2.3_regularization.md)
- [2.4 Regression Diagnostics](01_regression/02_intermediate/2.4_diagnostics.md) · [Exercise](../../Exercises/MachineLearning/01_regression/02_intermediate/2.4_diagnostics.ipynb)

### Advanced

- [3.1 Advanced Feature Engineering](01_regression/03_advanced/3.1_features.md)
- [3.2 Hyperparameter Optimization](01_regression/03_advanced/3.2_tuning.md) · [Exercise](../../Exercises/MachineLearning/01_regression/03_advanced/3.2_tuning.ipynb)
- [3.3 Regression Model Explainability](01_regression/03_advanced/3.3_explainability.md)
- [3.4 Regression Deployment](01_regression/03_advanced/3.4_deployment.md) · [Exercise](../../Exercises/MachineLearning/01_regression/03_advanced/3.4_deployment.ipynb)

---

## 02 · Classification

**Supervised learning** — predict discrete classes.  
**Core algorithms:** Logistic Regression, Decision Tree, SVM, KNN, Naive Bayes  
**Capstone:** [Complaint classification](../../Projects/MachineLearning/02_complaint_classification/README.md)

### Beginner

- [1.1 Introduction](02_classification/01_beginner/1.1_intro.md)
- [1.2 Logistic Regression](02_classification/01_beginner/1.2_logistic.md) · [Exercise](../../Exercises/MachineLearning/02_classification/01_beginner/1.2_logistic.ipynb)
- [1.3 Decision Tree](02_classification/01_beginner/1.3_decision_tree.md) · [Exercise](../../Exercises/MachineLearning/02_classification/01_beginner/1.3_decision_tree.ipynb)
- [1.4 Classification Evaluation](02_classification/01_beginner/1.4_evaluation.md) · [Exercise](../../Exercises/MachineLearning/02_classification/01_beginner/1.4_evaluation.ipynb)

### Intermediate

- [2.1 K-Nearest Neighbors](02_classification/02_intermediate/2.1_knn.md) · [Exercise](../../Exercises/MachineLearning/02_classification/02_intermediate/2.1_knn.ipynb)
- [2.2 Naive Bayes](02_classification/02_intermediate/2.2_naive_bayes.md) · [Exercise](../../Exercises/MachineLearning/02_classification/02_intermediate/2.2_naive_bayes.ipynb)
- [2.3 Support Vector Machine](02_classification/02_intermediate/2.3_svm.md) · [Exercise](../../Exercises/MachineLearning/02_classification/02_intermediate/2.3_svm.ipynb)
- [2.4 Class Imbalance](02_classification/02_intermediate/2.4_imbalance.md)
- [2.5 ROC, AUC & PR Curves](02_classification/02_intermediate/2.5_roc_auc.md)

### Advanced

- [3.1 Model Comparison & Selection](02_classification/03_advanced/3.1_comparison.md)
- [3.2 Probability Calibration](02_classification/03_advanced/3.2_calibration.md)
- [3.3 Advanced Feature Selection](02_classification/03_advanced/3.3_feature_selection.md)
- [3.4 Classification Pipelines](02_classification/03_advanced/3.4_pipelines.md) · [Exercise](../../Exercises/MachineLearning/02_classification/03_advanced/3.4_pipelines.ipynb)
- [3.5 Explainable Classification API](02_classification/03_advanced/3.5_deployment.md)

---

## 03 · Ensemble Learning

**Supervised learning** — combine models for accuracy and stability.  
**Core algorithms:** Random Forest, Gradient Boosting, XGBoost  
**Capstone:** [Tax payment risk](../../Projects/MachineLearning/03_tax_risk_prediction/README.md)

### Beginner · Intermediate · Advanced

See lesson files under [03_ensemble/](03_ensemble/) — full index matches Phase 0 table style in the repository tree.

Key exercises: [Random Forest](../../Exercises/MachineLearning/03_ensemble/01_beginner/1.3_random_forest.ipynb), [Gradient Boosting](../../Exercises/MachineLearning/03_ensemble/02_intermediate/2.1_gradient_boosting.ipynb), [XGBoost](../../Exercises/MachineLearning/03_ensemble/02_intermediate/2.2_xgboost.ipynb), [Optuna](../../Exercises/MachineLearning/03_ensemble/03_advanced/3.3_optuna.ipynb).

---

## 04 · Clustering

**Unsupervised learning** — discover groups without labels.  
**Core algorithms:** K-Means, DBSCAN, Hierarchical Clustering  
**Capstone:** [Complaint hotspots](../../Projects/MachineLearning/04_complaint_hotspots/README.md)

Exercises: [K-Means](../../Exercises/MachineLearning/04_clustering/01_beginner/1.3_kmeans.ipynb), [DBSCAN](../../Exercises/MachineLearning/04_clustering/02_intermediate/2.1_dbscan.ipynb), [Hierarchical](../../Exercises/MachineLearning/04_clustering/02_intermediate/2.2_hierarchical.ipynb), [Geospatial](../../Exercises/MachineLearning/04_clustering/03_advanced/3.3_geospatial.ipynb).

---

## 05 · Dimensionality Reduction

**Unsupervised learning** — compress features while preserving signal.  
**Core algorithm:** PCA  
**Capstone:** [KPI analysis](../../Projects/MachineLearning/05_kpi_analysis/README.md)

Exercises: [Scaling](../../Exercises/MachineLearning/05_dimensionality/01_beginner/1.2_scaling.ipynb), [PCA](../../Exercises/MachineLearning/05_dimensionality/01_beginner/1.3_pca.ipynb), [t-SNE](../../Exercises/MachineLearning/05_dimensionality/02_intermediate/2.3_tsne.ipynb), [Pipeline](../../Exercises/MachineLearning/05_dimensionality/03_advanced/3.4_pipeline.ipynb).

---

## 06 · Neural Networks & Deep Learning

**Deep learning** — complex patterns with layered networks.  
**Capstone:** [Asset detection (YOLO)](../../Projects/MachineLearning/06_asset_detection/README.md)

Exercises: [Perceptron](../../Exercises/MachineLearning/06_neural_networks/01_beginner/1.2_perceptron.ipynb), [Feedforward](../../Exercises/MachineLearning/06_neural_networks/01_beginner/1.4_feedforward.ipynb), [PyTorch](../../Exercises/MachineLearning/06_neural_networks/02_intermediate/2.3_pytorch.ipynb), [CNN](../../Exercises/MachineLearning/06_neural_networks/02_intermediate/2.4_cnn.ipynb), [Transfer learning](../../Exercises/MachineLearning/06_neural_networks/03_advanced/3.1_transfer_learning.ipynb), [YOLO](../../Exercises/MachineLearning/06_neural_networks/03_advanced/3.2_yolo.ipynb).

---

## 07 · Time Series Forecasting

**Forecasting** — predict future from temporal history.  
**Core algorithm:** ARIMA  
**Capstone:** [Revenue forecasting](../../Projects/MachineLearning/07_revenue_forecasting/README.md)

Exercises: [Components](../../Exercises/MachineLearning/07_time_series/01_beginner/1.2_components.ipynb), [ARIMA](../../Exercises/MachineLearning/07_time_series/02_intermediate/2.3_arima.ipynb), [SARIMA/SARIMAX](../../Exercises/MachineLearning/07_time_series/02_intermediate/2.4_sarima.ipynb).

---

## 08 · Association Rule Learning

**Unsupervised learning** — co-occurrence and frequent patterns.  
**Core algorithm:** Apriori  
**Capstone:** [Complaint patterns](../../Projects/MachineLearning/08_complaint_patterns/README.md)

Exercises: [Metrics](../../Exercises/MachineLearning/08_association/01_beginner/1.3_metrics.ipynb), [Apriori](../../Exercises/MachineLearning/08_association/01_beginner/1.4_apriori.ipynb), [Implementation](../../Exercises/MachineLearning/08_association/02_intermediate/2.1_implementation.ipynb).

---

## Recommended study sequence

```text
Phase 0 → 01 Regression → 02 Classification → 03 Ensemble
       → 04 Clustering → 05 Dimensionality → 06 Neural Networks
       → 07 Time Series → 08 Association Rules
       → Final capstone (CRISP-DM → API → Docker → monitoring)
```

## Repository layout

```text
Learning/MachineLearning/     # This folder — theory (.md)
Exercises/MachineLearning/    # Labs (.ipynb)
Datasets/MachineLearning/     # raw / processed / sample
Projects/MachineLearning/     # Eight capstone folders
```

## Algorithms covered (16 core + extensions)

| Category | Algorithms & methods |
| -------- | -------------------- |
| Regression | Linear, polynomial, regularized |
| Classification | Logistic, tree, KNN, Naive Bayes, SVM |
| Ensemble | Random Forest, boosting, XGBoost, LightGBM, CatBoost |
| Clustering | K-Means, DBSCAN, hierarchical, HDBSCAN |
| Dimensionality | PCA, t-SNE, UMAP, kernel PCA |
| Neural networks | MLP, CNN, transfer learning, transformers (intro) |
| Time series | ARIMA, SARIMA, ML/DL forecasting |
| Association | Apriori, FP-Growth |

---

*Stub lessons are scaffolded; fill each `.md` before publishing. Re-run `scripts/scaffold_ml_curriculum.py` only to add missing paths — it does not overwrite existing files.*
