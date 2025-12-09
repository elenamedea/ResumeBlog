FROM continuumio/miniconda3:23.10.0-1

WORKDIR /app

COPY ./pages pages
COPY ./utils utils
COPY ./app.py app.py
COPY ./environment.yml environment.yml

RUN conda env create -f ./environment.yml

COPY ./.streamlit .streamlit

CMD [ "conda", "run", \
      "--no-capture-output", \
      "-n", "elenamedea.github.io", \
      "python", "-m", "streamlit", "run", "./app.py", \
      "--server.port", "80" \
    ]
