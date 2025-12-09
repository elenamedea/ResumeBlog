# Your resume website multipage streamlit app

🪴 **Welcome to ResumeBlog, a resume website template** 🪴

The current repository is an implementation of a Curriculum Vitae Streamlit multipage app, containing an English and a German version.

In order to create your website, you can fork the current repo and fill the [dictionaries](utils/context_dictionaries.py) and [strings](utils/context_strings.py) files with your personal information.

📌 For hosting the Streamlit multipage app, you can sync your GitHub repository with a Hugging Face Space. For this process, check [here](https://huggingface.co/docs/hub/en/spaces-github-actions) the original source. 🔗

---

## Hugging Face Spaces

You can visit Hugging Face Spaces and create an account, by clicking on [here](https://huggingface.co/spaces). 🔗

---

Except for Hugging Face Spaces, Docker is utilized for containerization and app deployment.

## How to setup the ResumeBlog environment with Conda and VsCode

### Prerequisites

- Install [miniconda](https://docs.conda.io/projects/miniconda/en/latest/) 🔗
- `conda init --all`
- `conda env create -f environment.yml`
- `conda activate ResumeBlog` (on OSX you need to `conda deactivate` before this command)
- Set python interpreter for the VsCode Workspace
    - Open VsCode View Menu > Command Palette (Cmd/Ctrl + Shift + P)
    - Search and select `Python: Select Interpreter`
    - Select the options that contains `ResumeBlog`
- Add [Jupyter extention](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) 🔗 to VsCode

### Common tasks

When working in the terminal, use `conda activate ResumeBlog` (on OSX you need to `conda deactivate` before this command).

When working in a Jupyter Notebook, do the following once per Notebook (in case you don't, possibly you will be asked about it on the first attempt to run any code block in that Nodebook)
- Open VsCode View Menu > Command Palette (Cmd/Ctrl + Shift + P)
- Search and select `Notebook: Select Notebook Kernel`
- Select the options that contains `ResumeBlog`

When [adding](https://anaconda.org/search?q=jupyter) 🔗 or removing a package
- Modify `environment.yml` accordingly (don't forget to update channels as needed)
- `conda env update --file environment.yml --prune`
- Also `conda env export --from-history` can be used to get a partially incorrect `environment.yml` of the current environment 
    - Beware that this command does not include `channels` in the generated `environment.yml`
    - Beware that this command includes `prefix` which should not be stored in `environment.yml`, as it changes from one machine to another
    - [Here is the related issue](https://github.com/conda/conda/issues/12842) 🔗 on the official repo

---

### Running with local services

- Code execution in Jupyter Notebooks should work as expected
- Start Streamlit with `python -m streamlit run ./app.py` (don't forget to deactivate conda base env before activating conda `ResumeBlog`)

---

### Deploying Streamlit using Docker

####  Docker Prerequisites

- [Install Docker Engine](https://docs.streamlit.io/deploy/tutorials/docker#install-docker-engine) 🔗
- [Check network port accessibility](https://docs.streamlit.io/deploy/tutorials/docker#check-network-port-accessibility) 🔗

#### Running with docker compose

- `docker compose build`
- `docker compose up -d`
- Visit http://localhost for Streamlit multipage app

