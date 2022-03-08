# MLOps Demo

## 📋 Requirements

* DVC
* Python3 and poetry

## 🏃🏻 Running Project

```
poetry install

dvc run -n preprocess -d ./src/preprocess_data.py -d data/weatherAUS.csv -o ./data/weatherAUS_processed.csv python3 ./src/preprocess_data.py


```


### ✅ Pre-commit Tests

In order to activate pre-commit testing you need ```pre-commit```

Installing pre-commit with poetry
```
poetry add pre-commit --dev
```

Setup pre-commit on your local repository. Keep in mind this creates a git hook.
```
poetry shell
pre-commit install
```

Now everytime you make a commit, the tests defined in ```.pre-commit-config.yaml``` will be run before allowing your commit.

**Example**
```
$ git commit -m "Example commit"

black....................................................................Passed
pytest-check.............................................................Passed
```


### ⚗️ Using DVC

Download data from the DVC repository(analog to ```git pull```)
```
dvc pull
```

Reproduce the pipeline using DVC
```
dvc repro
```
