"""Project paths for the editable checkout; no filesystem changes on import.

This research package is intended to be installed editable from its project folder.
Relocating a built wheel alone does not relocate the project's datasets.
"""

from datetime import date
import os
from pathlib import Path

from dotenv import load_dotenv

# Test site for the data-acquisition feasibility notebooks (Geo-Wiki sample id).
TEST_SITE_ID = 1151194
# Data window and temporal binning, as in the thesis proposal and Galileo's config.
DATA_START_DATE = date(2015, 7, 1)
DATA_END_DATE = date(2016, 7, 1)
DAYS_PER_TIMESTEP = 30
# Exported area per site: the 100 x 100 m Geo-Wiki site plus a 100 m margin on each side.
SITE_SIZE_METRES = 300

# Secrets and local settings: read <project root>/.env (ignored by Git) without
# overriding variables already set in the environment.
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

# Google Earth Engine login. Values come from the environment/.env (never committed);
# see .env.example. Unset EE_PROJECT falls back to the project stored by
# `earthengine authenticate`. A service account is used only if a key file is given.
EE_PROJECT = os.environ.get("EE_PROJECT")
EE_SERVICE_ACCOUNT_EMAIL = os.environ.get("EE_SERVICE_ACCOUNT_EMAIL")
EE_SERVICE_ACCOUNT_KEY_FILE = os.environ.get("EE_SERVICE_ACCOUNT_KEY_FILE")

# Resolve relative to this source file, not the notebook's working directory.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
REPORTS_DIR = PROJECT_ROOT / "reports"
RUNS_DIR = PROJECT_ROOT / "runs"
FIGURES_DIR = RUNS_DIR / "figures"
TABLES_DIR = RUNS_DIR / "tables"
REFERENCES_DIR = PROJECT_ROOT / "references"
QGIS_DIR = PROJECT_ROOT / "qgis"
QGIS_PROJECTS_DIR = QGIS_DIR / "projects"
QGIS_STYLES_DIR = QGIS_DIR / "styles"


def project_path(*parts: str | Path) -> Path:
    """Join relative path components to this checkout's root.

    Uses normal pathlib semantics; this is not a sandbox or path validator.

    Args:
        *parts: Path components to join. An absolute component replaces the root.

    Returns:
        A path anchored to the project root unless an absolute path was supplied.

    Examples:
        >>> project_path("data", "raw") == RAW_DATA_DIR
        True
    """
    return PROJECT_ROOT.joinpath(*parts)


def ensure_output_dir(path: str | Path) -> Path:
    """Create an output directory and return it; relative paths use PROJECT_ROOT.

    Pass a directory, not a filename. Existing directory contents are preserved.
    """
    output_dir = Path(path)
    if not output_dir.is_absolute():
        output_dir = PROJECT_ROOT / output_dir

    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir
