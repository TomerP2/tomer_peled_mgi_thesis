# Notebook reading order

| Order | Notebook | Purpose | Required inputs |
| --- | --- | --- | --- |
| 1 | [Getting started](0.01-tp-getting-started.ipynb) | Demonstrate the Pixi environment, package paths, pandas summary, and logging. | Installed Pixi environment; synthetic data are created in memory. |
| 2 | [Geo-Wiki 2015 download](geowiki/0.02-tp-geowiki-2015-download.ipynb) | Acquire or verify the full pinned CSV and unchanged Natural Earth boundary. | Installed Pixi environment; internet on first acquisition, approximately 2 GB free space for the CSV. |
| 3 | [Geo-Wiki 2015 exploration](geowiki/0.03-tp-geowiki-2015-exploration.ipynb) | Summarize whole sites, inspect coverage, select all African sites, and compare class pixel share with site presence. | Complete CSV and boundary from notebook 0.02; subsequent runs reuse summaries under `data/interim/geowiki/14871660/`. |
| 4 | [downloading_preprocessing_input: Sentinel-1](downloading_preprocessing_input/0.04-tp-test-site-sentinel1.ipynb) | Download and preprocess Sentinel-1 for one 300 m area (100 m site plus margin) (Galileo method, GEE), timing each step and measuring storage. | Installed environment; Earth Engine login and `EE_PROJECT` (see `.env.example`); site summary from notebook 0.03. |

Add notebooks here as the project grows. Group multiple notebooks about the same
topic in a descriptive subdirectory and link them in suggested reading/execution
order. State prerequisites and outputs from earlier notebooks in Required inputs.
Authored notebooks live here; executed copies and exports live in `runs/notebooks/`.
