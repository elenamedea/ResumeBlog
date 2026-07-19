# Your resume website as a Streamlit multipage app

🪴 **Welcome to ResumeBlog, a resume website template** 🪴

This repository implements a Curriculum Vitae Streamlit multipage app with an English and a German version, packaged as a Docker image you can run locally or deploy to any container host.

To create your own website, fork this repo and fill the [dictionaries](utils/context_dictionaries.py) and [strings](utils/context_strings.py) files with your personal information.

---

## Local development with uv

[uv](https://docs.astral.sh/uv/) manages the environment; `pyproject.toml` + `uv.lock` are the source of truth.

- [Install uv](https://docs.astral.sh/uv/getting-started/installation/) 🔗
- `uv sync` — creates `.venv/` with locked dependencies
- `uv run streamlit run app.py` - starts the app on http://localhost:8501
- In VS Code: Command Palette → `Python: Select Interpreter` → pick `.venv`

Adding or removing a package:

- `uv add <package>` / `uv remove <package>` - updates `pyproject.toml` and `uv.lock` together
- Commit both files; never edit `uv.lock` by hand

---

## Running with Docker

Two compose files, one image:

- **Development** (hot reload, source mounted):
  `docker compose -f docker-compose.dev.yml up --build`
- **Production parity** (immutable image, restart policy):
  `docker compose -f docker-compose.prod.yml up --build -d`

Both serve on http://localhost:7860. Copy `.env.example` to `.env` for optional settings; `.env` is git-ignored and never committed.

---

## Deployment

The image is host-agnostic: non-root, port 7860, health-checked on `/_stcore/health` - it runs on any platform that builds or pulls Docker images. A free option is a [Render](https://render.com) Docker web service connected to your GitHub fork with auto-deploy on `main`; see [ResumeBlog-ES](https://github.com/elenamedea/ResumeBlog-ES) for a live deployment of this template, including its `render.yaml` blueprint. (Note: free-tier instances typically sleep after idle and cold-start on the next visit.)

---

## Observability (optional)

The app is instrumented with [Pydantic Logfire](https://logfire.pydantic.dev/): page views are traced with the page title as a span attribute. It activates only when a `LOGFIRE_TOKEN` environment variable is present - set it in your hosting platform's environment/secret settings, or in `.env` when self-hosting. Without the token the instrumentation is a silent no-op - no Logfire account required.
