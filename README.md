# MLOps Demo

[![model-training-evaluate](https://github.com/lucasmelin/mlops-demo/actions/workflows/train_evaluate.yaml/badge.svg)](https://github.com/lucasmelin/mlops-demo/actions/workflows/train_evaluate.yaml) [![Python Package and Test](https://github.com/lucasmelin/mlops-demo/actions/workflows/test_on_push.yaml/badge.svg)](https://github.com/lucasmelin/mlops-demo/actions/workflows/test_on_push.yaml)

This demo shows some of the principles of MLOps:

- **Versioning**
  - Data is versioned using [DVC](https://dvc.org/).
  - Model is versioned using [GitHub](https://github.com/).
- **Automated data pipelines**
  - Reproducible data pipelines are setup using DVC, which is language and framework agnostic.
- **CI/CD for Machine learning**
  - [CML (Continuous Machine Learning)](https://cml.dev/) is used along with GitHub Actions to manage ML experiments, track who trained the models or modified the data and when.
- **Automated Testing**
  - [Pytest](https://docs.pytest.org/) is used to test the pipelines and models, which are then run on every push using GitHub Actions.

## 📋 Requirements

* Python 3 and [poetry](https://python-poetry.org/)

## 🏃🏻 Running the Project

```
poetry install

# Download the data
dvc pull
# Check the project pipelines
dvc dag
# Reproduce the main experiment
dvc repro
# See current metrics
dvc metrics show
```

### ⚗️ Using DVC

Download data from the DVC repository (analogous to `git pull`)

```
dvc pull
```

Reproduce the pipeline using DVC
```
dvc repro
```
