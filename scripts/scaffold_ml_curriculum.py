#!/usr/bin/env python3
"""Create Machine Learning curriculum directories and stub files."""

from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

LEARNING = REPO / "Learning" / "MachineLearning"
EXERCISES = REPO / "Exercises" / "MachineLearning"
DATASETS = REPO / "Datasets" / "MachineLearning"
PROJECTS = REPO / "Projects" / "MachineLearning"

# (relative_path_under_MachineLearning, optional_exercise_filename)
CURRICULUM: list[tuple[str, str | None]] = [
    # Phase 0
    ("00_foundations/0.0_getting_started.md", None),
    ("00_foundations/0.1_ml_mental_model.md", None),
    ("00_foundations/0.2_types_of_ml.md", None),
    ("00_foundations/0.3_python_for_ml.md", "00_foundations/0.3_python_for_ml.ipynb"),
    ("00_foundations/0.4_mathematics.md", None),
    ("00_foundations/0.5_eda.md", "00_foundations/0.5_eda.ipynb"),
    ("00_foundations/0.6_preprocessing.md", "00_foundations/0.6_preprocessing.ipynb"),
    ("00_foundations/0.7_train_test.md", "00_foundations/0.7_train_test.ipynb"),
    ("00_foundations/0.8_evaluation.md", None),
    ("00_foundations/0.9_crisp_dm.md", "00_foundations/0.9_crisp_dm.ipynb"),
    # 01 Regression
    ("01_regression/01_beginner/1.1_intro_regression.md", None),
    ("01_regression/01_beginner/1.2_simple_linear.md", "01_regression/01_beginner/1.2_simple_linear.ipynb"),
    ("01_regression/01_beginner/1.3_multiple_linear.md", "01_regression/01_beginner/1.3_multiple_linear.ipynb"),
    ("01_regression/01_beginner/1.4_evaluation.md", "01_regression/01_beginner/1.4_evaluation.ipynb"),
    ("01_regression/02_intermediate/2.1_gradient_descent.md", "01_regression/02_intermediate/2.1_gradient_descent.ipynb"),
    ("01_regression/02_intermediate/2.2_polynomial.md", "01_regression/02_intermediate/2.2_polynomial.ipynb"),
    ("01_regression/02_intermediate/2.3_regularization.md", None),
    ("01_regression/02_intermediate/2.4_diagnostics.md", "01_regression/02_intermediate/2.4_diagnostics.ipynb"),
    ("01_regression/03_advanced/3.1_features.md", None),
    ("01_regression/03_advanced/3.2_tuning.md", "01_regression/03_advanced/3.2_tuning.ipynb"),
    ("01_regression/03_advanced/3.3_explainability.md", None),
    ("01_regression/03_advanced/3.4_deployment.md", "01_regression/03_advanced/3.4_deployment.ipynb"),
    # 02 Classification
    ("02_classification/01_beginner/1.1_intro.md", None),
    ("02_classification/01_beginner/1.2_logistic.md", "02_classification/01_beginner/1.2_logistic.ipynb"),
    ("02_classification/01_beginner/1.3_decision_tree.md", "02_classification/01_beginner/1.3_decision_tree.ipynb"),
    ("02_classification/01_beginner/1.4_evaluation.md", "02_classification/01_beginner/1.4_evaluation.ipynb"),
    ("02_classification/02_intermediate/2.1_knn.md", "02_classification/02_intermediate/2.1_knn.ipynb"),
    ("02_classification/02_intermediate/2.2_naive_bayes.md", "02_classification/02_intermediate/2.2_naive_bayes.ipynb"),
    ("02_classification/02_intermediate/2.3_svm.md", "02_classification/02_intermediate/2.3_svm.ipynb"),
    ("02_classification/02_intermediate/2.4_imbalance.md", None),
    ("02_classification/02_intermediate/2.5_roc_auc.md", None),
    ("02_classification/03_advanced/3.1_comparison.md", None),
    ("02_classification/03_advanced/3.2_calibration.md", None),
    ("02_classification/03_advanced/3.3_feature_selection.md", None),
    ("02_classification/03_advanced/3.4_pipelines.md", "02_classification/03_advanced/3.4_pipelines.ipynb"),
    ("02_classification/03_advanced/3.5_deployment.md", None),
    # 03 Ensemble
    ("03_ensemble/01_beginner/1.1_intro.md", None),
    ("03_ensemble/01_beginner/1.2_bagging_boosting.md", None),
    ("03_ensemble/01_beginner/1.3_random_forest.md", "03_ensemble/01_beginner/1.3_random_forest.ipynb"),
    ("03_ensemble/01_beginner/1.4_evaluation.md", None),
    ("03_ensemble/02_intermediate/2.1_gradient_boosting.md", "03_ensemble/02_intermediate/2.1_gradient_boosting.ipynb"),
    ("03_ensemble/02_intermediate/2.2_xgboost.md", "03_ensemble/02_intermediate/2.2_xgboost.ipynb"),
    ("03_ensemble/02_intermediate/2.3_tuning.md", None),
    ("03_ensemble/02_intermediate/2.4_importance.md", None),
    ("03_ensemble/03_advanced/3.1_lightgbm_catboost.md", None),
    ("03_ensemble/03_advanced/3.2_stacking.md", None),
    ("03_ensemble/03_advanced/3.3_optuna.md", "03_ensemble/03_advanced/3.3_optuna.ipynb"),
    ("03_ensemble/03_advanced/3.4_shap.md", None),
    ("03_ensemble/03_advanced/3.5_production.md", None),
    # 04 Clustering
    ("04_clustering/01_beginner/1.1_intro.md", None),
    ("04_clustering/01_beginner/1.2_distance.md", None),
    ("04_clustering/01_beginner/1.3_kmeans.md", "04_clustering/01_beginner/1.3_kmeans.ipynb"),
    ("04_clustering/01_beginner/1.4_elbow.md", None),
    ("04_clustering/02_intermediate/2.1_dbscan.md", "04_clustering/02_intermediate/2.1_dbscan.ipynb"),
    ("04_clustering/02_intermediate/2.2_hierarchical.md", "04_clustering/02_intermediate/2.2_hierarchical.ipynb"),
    ("04_clustering/02_intermediate/2.3_evaluation.md", None),
    ("04_clustering/02_intermediate/2.4_profiling.md", None),
    ("04_clustering/03_advanced/3.1_hdbscan.md", None),
    ("04_clustering/03_advanced/3.2_high_dimensional.md", None),
    ("04_clustering/03_advanced/3.3_geospatial.md", "04_clustering/03_advanced/3.3_geospatial.ipynb"),
    ("04_clustering/03_advanced/3.4_monitoring.md", None),
    # 05 Dimensionality
    ("05_dimensionality/01_beginner/1.1_intro.md", None),
    ("05_dimensionality/01_beginner/1.2_scaling.md", "05_dimensionality/01_beginner/1.2_scaling.ipynb"),
    ("05_dimensionality/01_beginner/1.3_pca.md", "05_dimensionality/01_beginner/1.3_pca.ipynb"),
    ("05_dimensionality/02_intermediate/2.1_pca_math.md", None),
    ("05_dimensionality/02_intermediate/2.2_components.md", None),
    ("05_dimensionality/02_intermediate/2.3_tsne.md", "05_dimensionality/02_intermediate/2.3_tsne.ipynb"),
    ("05_dimensionality/02_intermediate/2.4_umap.md", None),
    ("05_dimensionality/03_advanced/3.1_kernel_pca.md", None),
    ("05_dimensionality/03_advanced/3.2_comparison.md", None),
    ("05_dimensionality/03_advanced/3.3_autoencoders.md", None),
    ("05_dimensionality/03_advanced/3.4_pipeline.md", "05_dimensionality/03_advanced/3.4_pipeline.ipynb"),
    # 06 Neural networks
    ("06_neural_networks/01_beginner/1.1_intro.md", None),
    ("06_neural_networks/01_beginner/1.2_perceptron.md", "06_neural_networks/01_beginner/1.2_perceptron.ipynb"),
    ("06_neural_networks/01_beginner/1.3_activation.md", None),
    ("06_neural_networks/01_beginner/1.4_feedforward.md", "06_neural_networks/01_beginner/1.4_feedforward.ipynb"),
    ("06_neural_networks/02_intermediate/2.1_backprop.md", None),
    ("06_neural_networks/02_intermediate/2.2_optimizers.md", None),
    ("06_neural_networks/02_intermediate/2.3_pytorch.md", "06_neural_networks/02_intermediate/2.3_pytorch.ipynb"),
    ("06_neural_networks/02_intermediate/2.4_cnn.md", "06_neural_networks/02_intermediate/2.4_cnn.ipynb"),
    ("06_neural_networks/02_intermediate/2.5_regularization.md", None),
    ("06_neural_networks/03_advanced/3.1_transfer_learning.md", "06_neural_networks/03_advanced/3.1_transfer_learning.ipynb"),
    ("06_neural_networks/03_advanced/3.2_yolo.md", "06_neural_networks/03_advanced/3.2_yolo.ipynb"),
    ("06_neural_networks/03_advanced/3.3_transformers.md", None),
    ("06_neural_networks/03_advanced/3.4_gpu.md", None),
    ("06_neural_networks/03_advanced/3.5_deployment.md", None),
    # 07 Time series
    ("07_time_series/01_beginner/1.1_intro.md", None),
    ("07_time_series/01_beginner/1.2_components.md", "07_time_series/01_beginner/1.2_components.ipynb"),
    ("07_time_series/01_beginner/1.3_moving_average.md", None),
    ("07_time_series/01_beginner/1.4_metrics.md", None),
    ("07_time_series/02_intermediate/2.1_stationarity.md", None),
    ("07_time_series/02_intermediate/2.2_autocorrelation.md", None),
    ("07_time_series/02_intermediate/2.3_arima.md", "07_time_series/02_intermediate/2.3_arima.ipynb"),
    ("07_time_series/02_intermediate/2.4_sarima.md", "07_time_series/02_intermediate/2.4_sarima.ipynb"),
    ("07_time_series/02_intermediate/2.5_validation.md", None),
    ("07_time_series/03_advanced/3.1_ml_forecasting.md", None),
    ("07_time_series/03_advanced/3.2_lstm.md", None),
    ("07_time_series/03_advanced/3.3_multivariate.md", None),
    ("07_time_series/03_advanced/3.4_uncertainty.md", None),
    ("07_time_series/03_advanced/3.5_production.md", None),
    # 08 Association
    ("08_association/01_beginner/1.1_intro.md", None),
    ("08_association/01_beginner/1.2_transactions.md", None),
    ("08_association/01_beginner/1.3_metrics.md", "08_association/01_beginner/1.3_metrics.ipynb"),
    ("08_association/01_beginner/1.4_apriori.md", "08_association/01_beginner/1.4_apriori.ipynb"),
    ("08_association/02_intermediate/2.1_implementation.md", "08_association/02_intermediate/2.1_implementation.ipynb"),
    ("08_association/02_intermediate/2.2_fpgrowth.md", None),
    ("08_association/02_intermediate/2.3_filtering.md", None),
    ("08_association/02_intermediate/2.4_visualization.md", None),
    ("08_association/03_advanced/3.1_metrics.md", None),
    ("08_association/03_advanced/3.2_sequential.md", None),
    ("08_association/03_advanced/3.3_scaling.md", None),
    ("08_association/03_advanced/3.4_recommendations.md", None),
    ("08_association/03_advanced/3.5_production.md", None),
]

PROJECT_DIRS = [
    "01_property_tax_prediction",
    "02_complaint_classification",
    "03_tax_risk_prediction",
    "04_complaint_hotspots",
    "05_kpi_analysis",
    "06_asset_detection",
    "07_revenue_forecasting",
    "08_complaint_patterns",
]


def lesson_title(md_path: Path) -> str:
    stem = md_path.stem
    parts = stem.split("_", 1)
    label = parts[1].replace("_", " ").title() if len(parts) > 1 else stem
    return f"{parts[0]} {label}" if parts else stem


def exercise_link_from_lesson(lesson_rel: str, exercise_rel: str) -> str:
    n_up = len(Path(lesson_rel).parent.parts) + 2  # Learning/MachineLearning + category folders
    prefix = "../" * n_up
    return f"{prefix}Exercises/MachineLearning/{exercise_rel}"


def md_stub(rel: str) -> str:
    path = Path(rel)
    title = lesson_title(path)
    rel_exercise = None
    for lesson, ex in CURRICULUM:
        if lesson == rel and ex:
            rel_exercise = ex
            break
    exercise_line = ""
    if rel_exercise:
        link = exercise_link_from_lesson(rel, rel_exercise)
        exercise_line = f"\n**Exercise:** [{Path(rel_exercise).name}]({link})\n"
    return f"""# {title}

{exercise_line}
### Learning Objectives

- _Draft — fill in before publishing this lesson._

### Concept

_TBD_

### Mathematical Intuition

_TBD_

### How the Algorithm Works

_TBD_

### Python Implementation

_TBD_

### Evaluation

_TBD_

### Common Mistakes

_TBD_

### Real-World Use Cases

_TBD_

### Exercises

_See linked notebook above, or add guided questions here._

### Summary

_TBD_
"""


def notebook_stub(rel_lesson: str, rel_exercise: str) -> dict:
    lesson_link = f"../../../Learning/MachineLearning/{rel_lesson}"
    title = lesson_title(Path(rel_lesson))
    nb_title = Path(rel_exercise).stem.replace("_", " ").title()
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {nb_title}\n",
                    "\n",
                    f"**Learning:** [{title}]({lesson_link})\n",
                    "\n",
                    "**Goal:** _Complete the guided tasks, then the challenge exercise at the end._\n",
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Setup"],
            },
            {
                "cell_type": "code",
                "metadata": {},
                "source": [
                    "import sys\n",
                    "from pathlib import Path\n",
                    "\n",
                    "ROOT = Path.cwd().resolve()\n",
                    "while not (ROOT / \"src\").is_dir() and ROOT != ROOT.parent:\n",
                    "    ROOT = ROOT.parent\n",
                    "\n",
                    "if str(ROOT) not in sys.path:\n",
                    "    sys.path.insert(0, str(ROOT))\n",
                    "\n",
                    "print(f\"Project root: {ROOT}\")\n",
                ],
                "outputs": [],
                "execution_count": None,
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## 1. Guided practice\n", "\n", "_TBD_"],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## 2. Independent implementation\n", "\n", "_TBD_"],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## 3. Model evaluation\n", "\n", "_TBD_"],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## 4. Challenge\n", "\n", "_TBD_"],
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.11.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def main() -> None:
    created_md = 0
    created_nb = 0
    for lesson, exercise in CURRICULUM:
        md_path = LEARNING / lesson
        md_path.parent.mkdir(parents=True, exist_ok=True)
        if not md_path.exists():
            md_path.write_text(md_stub(lesson), encoding="utf-8")
            created_md += 1
        if exercise:
            nb_path = EXERCISES / exercise
            nb_path.parent.mkdir(parents=True, exist_ok=True)
            if not nb_path.exists():
                nb_path.write_text(
                    json.dumps(notebook_stub(lesson, exercise), indent=1) + "\n",
                    encoding="utf-8",
                )
                created_nb += 1

    for sub in ("raw", "processed", "sample"):
        (DATASETS / sub).mkdir(parents=True, exist_ok=True)
        gitkeep = DATASETS / sub / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.touch()

    for proj in PROJECT_DIRS:
        pdir = PROJECTS / proj
        pdir.mkdir(parents=True, exist_ok=True)
        readme = pdir / "README.md"
        if not readme.exists():
            name = proj.split("_", 1)[-1].replace("_", " ").title()
            readme.write_text(
                f"# Capstone: {name}\n\n"
                "_Project brief and deliverables — TBD. Align with the category capstone in "
                "[roadmap.md](../../Learning/MachineLearning/roadmap.md)._ \n",
                encoding="utf-8",
            )

    print(f"Created {created_md} lesson stubs, {created_nb} exercise notebooks.")


if __name__ == "__main__":
    main()
