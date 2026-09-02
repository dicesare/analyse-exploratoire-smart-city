# Historical Smart City analysis inventory

## Verified scope

The public narrative notebook contains 87 cells, 50 outputs and 11 embedded figures. It begins with 200,137 rows and 18 variables and examines missingness, semantics, duplicates, morphology, taxonomy, location and development stage.

## Data-quality decisions

- `numero` is entirely missing and `variete` is missing for 163,360 rows.
- genus is missing for only 16 initial records, but inspection shows a concentrated group of zero-measurement trees requiring contextual review.
- a value such as `Jardin` appears in inappropriate columns and is converted back to missing before analysis.
- duplicate coordinates reduce the inventory from 200,137 to 200,110 locations.
- physically implausible maxima—250,255 cm circumference and 881,818 m height—are treated as data errors, not urban-tree discoveries.
- circumference is constrained to 1–700 cm and height to 1–50 m for the principal morphology study, leaving 160,021 trees.

## Descriptive findings

In the final morphology sample:

- median circumference: 80 cm; mean: 92.45 cm;
- median height: 10 m; mean: 10.37 m;
- 146 genera are represented;
- Platanus is the most frequent genus;
- development stage is available for 130,100 trees, with adults the largest recorded group.

Before the final morphology filter, the cleaned inventory contains 175 genera and 539 species. Paris 15th is the most frequent administrative label in the displayed summary, and alignment trees are the dominant management domain.

## Relationship analysis

The verified Pearson correlation between height and circumference is **0.7973399802** on the final quantitative sample. The notebook then fits separate linear visualisations for young, young-adult, adult and mature trees instead of assuming one homogeneous relationship.

Correlation is not treated as age, health or causality. Operational use would require inventory-date checks, botanical expertise, uncertainty estimates and spatial exposure variables.

## Current portfolio value

The project demonstrates open-data ingestion, anomaly investigation, geospatial identifiers, reproducible filtering, descriptive statistics, biodiversity profiling, regression analysis and public-sector communication. The cleaned `src/` functions and tests show how the exploratory notebook can evolve into maintainable analytical software.

