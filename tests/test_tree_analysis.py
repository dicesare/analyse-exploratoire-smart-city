import pandas as pd
import pytest

from tree_analysis import (
    MeasurementPolicy,
    measurement_summary,
    prepare_trees,
    prepare_trees_with_report,
)


def test_filters_missing_and_impossible_measurements() -> None:
    data = pd.DataFrame(
        {
            "circonference_cm": [120, 0, 1201, None],
            "hauteur_m": [12, 10, 10, 8],
        }
    )
    clean = prepare_trees(data)
    assert clean.to_dict("records") == [{"circonference_cm": 120.0, "hauteur_m": 12}]


def test_requires_expected_schema() -> None:
    with pytest.raises(ValueError, match="Missing columns"):
        measurement_summary(pd.DataFrame({"height": [10]}))


def test_default_policy_matches_documented_historical_bounds() -> None:
    data = pd.DataFrame(
        {
            "circonference_cm": [700, 701, 100],
            "hauteur_m": [50, 10, 51],
        }
    )
    clean, report = prepare_trees_with_report(data)
    assert clean.index.tolist() == [0]
    assert report.implausible_measurements == 2
    assert report.rejected_rows == 2


def test_numeric_coercion_is_reported_and_input_is_unchanged() -> None:
    data = pd.DataFrame({"circonference_cm": ["120", "bad"], "hauteur_m": [12, 8]})
    original = data.copy(deep=True)
    clean, report = prepare_trees_with_report(data)
    assert clean["circonference_cm"].tolist() == [120.0]
    assert report.missing_measurements == 1
    pd.testing.assert_frame_equal(data, original)


def test_custom_policy_and_empty_input() -> None:
    policy = MeasurementPolicy(maximum_height_m=80, maximum_circumference_cm=1000)
    data = pd.DataFrame({"circonference_cm": [900], "hauteur_m": [70]})
    assert prepare_trees(data, policy).shape == (1, 2)
    _, report = prepare_trees_with_report(pd.DataFrame(columns=data.columns))
    assert report.retention_rate == 1.0


def test_policy_rejects_inverted_bounds() -> None:
    with pytest.raises(ValueError, match="circumference"):
        MeasurementPolicy(minimum_circumference_cm=10, maximum_circumference_cm=1)
