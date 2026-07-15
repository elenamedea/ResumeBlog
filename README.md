---
title: ResumeBlog
emoji: 🪴
colorFrom: red
colorTo: pink
sdk: docker
app_port: 7860
pinned: true
---

# Your resume website as a Streamlit multipage app

🪴 **Welcome to ResumeBlog, a resume website template** 🪴

This repository implements a Curriculum Vitae Streamlit multipage app with an English and a German version, packaged as a Docker image that deploys to a [Hugging Face Space](https://huggingface.co/spaces) via GitHub Actions — every push to `main` rebuilds and redeploys the site.

To create your own website, fork this repo and fill the [dictionaries](utils/context_dictionaries.py) and [strings](utils/context_strings.py) files with your personal information.

> The YAML block at the very top of this file is the [Space configuration](https://huggingface.co/docs/hub/spaces-config-reference); GitHub renders it as a small table, so it does not hurt the repo's README.

---

## Local development with uv

[uv](https://docs.astral.sh/uv/) manages the environment; `pyproject.toml` + `uv.lock` are the source of truth.

- [Install uv](https://docs.astral.sh/uv/getting-started/installation/) 🔗
- `uv sync` — creates `.venv/` with locked dependencies
- `uv run streamlit run app.py` — starts the app on http://localhost:8501
- In VS Code: Command Palette → `Python: Select Interpreter` → pick `.venv`

Adding or removing a package:

- `uv add <package>` / `uv remove <package>` — updates `pyproject.toml` and `uv.lock` together
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

## Deploying to a Hugging Face Space

1. [Create a Space](https://huggingface.co/new-space) → SDK **Docker**.
2. Create a **write** token: HF Settings → Access Tokens.
3. In your GitHub repo (Settings → Secrets and variables → Actions) set:
   - secret `HF_TOKEN` — the write token,
   - variables `HF_USERNAME` and `HF_SPACE_NAME` — your Space coordinates.
4. Push to `main`: the [sync workflow](.github/workflows/sync-to-hf.yml) force-pushes to the Space, which builds the Dockerfile and serves the app on port 7860. Watch the first build in the Space's **Logs** tab.

Reference on the GitHub ↔ Space sync: [Hugging Face docs](https://huggingface.co/docs/hub/en/spaces-github-actions) 🔗

---

## Observability (optional)

The app is instrumented with [Pydantic Logfire](https://logfire.pydantic.dev/): page views are traced with the page title as a span attribute. It activates only when a `LOGFIRE_TOKEN` environment variable is present (set it as a Space secret on HF, or in `.env` when self-hosting). Without the token the instrumentation is a silent no-op — no Logfire account required.
