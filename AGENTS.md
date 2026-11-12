# Agent entry point

Before doing any task work, read this file and [README.md](README.md), then read
the shared rules and relevant guides using the hosted-first policy and routing
table. Complete these steps before investigating project code/data, running other
task commands, planning implementation, or editing files. Follow links to related guides when the
task crosses topics; reading unrelated guides is not required. If the scope changes,
read any newly relevant guides before proceeding with that work. Do not rely on
the routing summaries as a substitute for reading the guides themselves.

## Shared guidance and project overrides

Hosted guide directory: https://raw.githubusercontent.com/TomerP2/Cookiecutter-Geospatial-Data-Science-Template/main/templates/shared-guides

At task start, first try to read `core.md` and the relevant topic guides from the
hosted directory above. Append each filename from the routing table to that URL;
follow related guide links against the hosted directory too. Read the actual guide
contents, not search snippets. If the URL is unconfigured, internet access is
unavailable, or any required guide cannot be read, use the local `guides/` backup
for all required guides and briefly report that fallback. Do not stop the task just
because hosted guides are unavailable. Use the guidance read at task start throughout
the task; read newly relevant guides if scope changes.
Read `core.md` for every task; its local backup is [shared working rules](guides/core.md).
User instructions and project-specific rules here take precedence over shared guides.
Keep overrides here. Reading hosted guides does not replace or update local files.

Project adapter: the package is `tomer_peled_mgi_thesis`, notebook initials
are `tp`, and the initial platform is
`win-64`. Shared examples use `project_package` and `ab`;
substitute these project values. The starter notebook is
`notebooks/0.01-tp-getting-started.ipynb`.

## Local overrides

- `.env` loading: unlike the shared data guide, this project loads a git-ignored
  `.env` in the project root from `src/tomer_peled_mgi_thesis/config.py` (python-dotenv,
  existing environment variables win). Keep secrets only in `.env` or the environment,
  list variable names in `.env.example`, and import `config` in notebooks instead of
  reading `os.environ` directly.
- LaTeX: do not compile LaTeX documents (e.g. with `latexmk` or `pdflatex`) in
  `reports/`. Edit the `.tex` sources only; the user compiles them.

## Task routing — conditional requirements

These guides apply only when doing the indicated work. Their examples and optional
tools are not a checklist of things to add to every project.

| Current work | Read |
| --- | --- |
| Starting/scoping a project, changing layout, handoff context | [Project setup](guides/project-setup.md) |
| Installing packages, kernels, tasks, lockfiles, platform changes | [Pixi environment](guides/pixi.md) |
| Exploring data or writing/executing notebooks | [Notebook conventions](guides/notebooks.md) |
| Adding or changing reusable Python code, package imports | [Source code](guides/source-code.md) |
| Acquiring data, storing outputs, parameters, provenance | [Data management](guides/data.md) |
| GIS, remote sensing, maps, QGIS exports/styles | [Geospatial work](guides/geospatial.md) |
| Predictive ML, splits, evaluation, experiment tracking | [Modeling](guides/modeling.md) |
| Writing/running pytest tests, choosing fixtures and regression cases | [Testing](guides/testing.md) |
| Logging execution, recording runs, organizing reports | [Run logging and reports](guides/run-reporting.md) |
| Choosing analytical checks, reviewing or delivering results | [Validation and delivery](guides/validation.md) |
