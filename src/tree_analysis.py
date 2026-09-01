"""Reusable preparation helpers for the Paris trees analysis."""

from __future__ import annotations

import pandas as pd

REQUIRED_COLUMNS = {"circonference_cm", "hauteur_m"}


def prepare_trees(data: pd.DataFrame) -> pd.DataFrame:
    """Return valid measurements without mutating the input frame."""
    missing = REQUIRED_COLUMNS - set(data.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    clean = data.copy()
    for column in REQUIRED_COLUMNS:
        clean[column] = pd.to_numeric(clean[column], errors="coerce")
    clean = clean.dropna(subset=list(REQUIRED_COLUMNS))
    return clean[
        clean["circonference_cm"].between(1, 1000)
        & clean["hauteur_m"].between(1, 80)
    ].reset_index(drop=True)


def measurement_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Summarize the two principal physical measurements."""
    return prepare_trees(data)[sorted(REQUIRED_COLUMNS)].describe().round(2)
