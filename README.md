# Paris Trees — Exploratory Data Analysis

Exploratory analysis of nearly 200,000 trees from the City of Paris open-data portal. The project demonstrates data-quality checks, outlier handling, spatial and biodiversity exploration, descriptive statistics and the relationship between tree height and circumference.

## Highlights

- reproducible analysis based on an official open dataset;
- explicit cleaning rules for impossible measurements and missing values;
- visual comparison of height and circumference distributions;
- spatial and taxonomic views supporting a Smart City narrative;
- linear-regression exploration;
- documented notebooks plus testable preparation functions.

![Height and circumference regression](images/Analyse_regression_lineaire.png)

## Case-study gallery

| Study | Focus |
|---|---|
| [01 — Data quality](notebooks/01_data_quality.ipynb) | schema, missingness, duplicates and physically implausible measurements |
| [02 — Urban distribution](notebooks/02_urban_distribution.ipynb) | arrondissement and site-level distribution with exposure-aware interpretation |
| [03 — Biodiversity](notebooks/03_biodiversity.ipynb) | genus/species diversity and concentration |
| [04 — Tree morphology](notebooks/04_tree_morphology.ipynb) | height, circumference, outliers and regression limits |
| [Original narrative analysis](notebooks/P2_01_notebook.ipynb) | complete historical analysis retained on the refreshed branch |

`main` and `portfolio-refresh` currently contain the same cleaned implementation. The gallery makes the different analytical questions visible without duplicating raw data.

## Repository structure

```text
notebooks/          narrative analysis and focused case studies
src/                reusable data preparation
tests/              fast unit tests on synthetic data
images/             exported results
synthese/           short project summary
```

## Reproduce the analysis

```bash
python -m venv .venv
pip install -r requirements.txt
jupyter lab notebooks/P2_01_notebook.ipynb
```

The raw dataset is not committed. Download the current tree inventory from the [Paris Open Data portal](https://opendata.paris.fr/) and record the dataset version/date used.

## Selected results

### Circumference distribution

![Circumference distribution](images/distribution_circonference.png)

### Height distribution

![Height distribution](images/distribution_hauteur.png)

## Data responsibility

The source is public municipal data. Generated results should be interpreted as an exploratory snapshot, not as an operational diagnosis of individual trees.

## License

Released under the [MIT License](LICENSE).

