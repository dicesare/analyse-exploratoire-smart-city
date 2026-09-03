"""Execute maintained portfolio notebooks without rewriting tracked artifacts."""

from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    for path in sorted((ROOT / "notebooks").glob("0[1-5]*.ipynb")):
        notebook = nbformat.read(path, as_version=4)
        NotebookClient(
            notebook,
            timeout=60,
            kernel_name="python3",
            resources={"metadata": {"path": ROOT}},
        ).execute()


if __name__ == "__main__":
    main()
