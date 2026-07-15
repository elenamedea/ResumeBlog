# ResumeBlog — Hugging Face Docker Space image
#
# Multi-stage: uv resolves the locked environment in the builder; the
# runtime stage carries only the venv and the app code.
# HF Spaces constraints honoured: port 7860, non-root UID 1000 with a
# writable HOME, XSRF/CORS disabled so Streamlit renders in the HF iframe.

FROM python:3.13-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:0.9 /uv /bin/uv

# Compile bytecode at build time; venv is built at its final runtime path
# so the interpreter references inside it stay valid after the copy.
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

WORKDIR /home/user/app

# Dependency layer only — code edits don't bust this cache
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev


FROM python:3.13-slim

# HF Spaces runs containers as user 1000; create it explicitly so
# local `docker run` behaves identically.
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/app/.venv/bin:$PATH

WORKDIR $HOME/app

COPY --from=builder --chown=user /home/user/app/.venv .venv

# App code — style.css and .streamlit are part of the image
COPY --chown=user app.py style.css ./
COPY --chown=user pages/ pages/
COPY --chown=user utils/ utils/
COPY --chown=user .streamlit/ .streamlit/

EXPOSE 7860

HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:7860/_stcore/health')"

CMD ["streamlit", "run", "app.py", \
     "--server.port=7860", \
     "--server.address=0.0.0.0", \
     "--server.enableXsrfProtection=false", \
     "--server.enableCORS=false"]
