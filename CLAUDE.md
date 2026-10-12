# LDI Lab manual

Jupyter Book 1.x site (`_config.yml`, `_toc.yml`), deployed by `.github/workflows/main.yml`.

## Building
- Always build inside the project venv, never with a globally installed `jb`/`jupyter-book`/`myst`.
- `./_test.sh` creates `venv-3.13` from `requirements.txt` on first run (via `_setup.sh`) and runs `jupyter-book build .`. Output goes to `_build/html` (git-ignored, as is `venv*`).
- To run a single tool in the env: `venv-3.13/bin/jupyter-book ...`.
- Keep the Python version in `_setup.sh`, `_test.sh`, `run-docker.sh`, `run-apptainer.sh` and the CI workflow in sync.
