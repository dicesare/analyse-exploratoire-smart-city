"""Reusable preparation helpers for the Paris trees analysis."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

REQUIRED_COLUMNS = ("circonference_cm", "hauteur_m")


@dataclass(frozen=True, slots=True)
class MeasurementPolicy:
    """Documented bounds used by the historical morphology study."""

    minimum_circumference_cm: float = 1
    maximum_circumference_cm: float = 700
    minimum_height_m: float = 1
    maximum_height_m: float = 50

    def __post_init__(self) -> None:
        if self.minimum_circumference_cm > self.maximum_circumference_cm:
            raise ValueError("minimum circumference cannot exceed maximum circumference")
        if self.minimum_height_m > self.maximum_height_m:
            raise ValueError("minimum height cannot exceed maximum height")


@dataclass(frozen=True, slots=True)
class PreparationReport:
    input_rows: int
    output_rows: int
    missing_measurements: int
    implausible_measurements: int

    @property
    def rejected_rows(self) -> int:
        return self.input_rows - self.output_rows

    @property
    def retention_rate(self) -> float:
        return self.output_rows / self.input_rows if self.input_rows else 1.0


def prepare_trees(
    data: pd.DataFrame, policy: MeasurementPolicy | None = None
) -> pd.DataFrame:
    """Return valid measurements without mutating the input frame."""
    clean, _ = prepare_trees_with_report(data, policy)
    return clean


def prepare_trees_with_report(
    data: pd.DataFrame, policy: MeasurementPolicy | None = None
) -> tuple[pd.DataFrame, PreparationReport]:
    """Apply explicit morphology rules and report their population impact."""
    missing = set(REQUIRED_COLUMNS).difference(data.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    active_policy = policy or MeasurementPolicy()
    clean = data.copy()
    for column in REQUIRED_COLUMNS:
        clean[column] = pd.to_numeric(clean[column], errors="coerce")
    complete = clean.loc[:, list(REQUIRED_COLUMNS)].notna().all(axis="columns")
    plausible = (
        clean["circonference_cm"].between(
            active_policy.minimum_circumference_cm,
            active_policy.maximum_circumference_cm,
        )
        & clean["hauteur_m"].between(
            active_policy.minimum_height_m,
            active_policy.maximum_height_m,
        )
    )
    result = clean.loc[complete & plausible].reset_index(drop=True)
    report = PreparationReport(
        input_rows=len(data),
        output_rows=len(result),
        missing_measurements=int((~complete).sum()),
        implausible_measurements=int((complete & ~plausible).sum()),
    )
    return result, report


def measurement_summary(data: pd.DataFrame) -> pd.DataFrame:
    """Summarize the two principal physical measurements."""
    return prepare_trees(data)[list(REQUIRED_COLUMNS)].describe().round(2)
