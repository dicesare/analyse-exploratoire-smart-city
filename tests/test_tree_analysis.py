import pandas as pd
import pytest

from src.tree_analysis import measurement_summary, prepare_trees


def test_filters_missing_and_impossible_measurements():
    data = pd.DataFrame({
        "circonference_cm": [120, 0, 1201, None],
        "hauteur_m": [12, 10, 10, 8],
    })
    clean = prepare_trees(data)
    assert clean.to_dict("records") == [{"circonference_cm": 120.0, "hauteur_m": 12}]


def test_requires_expected_schema():
    with pytest.raises(ValueError, match="Missing columns"):
        measurement_summary(pd.DataFrame({"height": [10]}))
