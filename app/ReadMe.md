# ReadMe

## Run locally

- pre-requisite: python, pip and venv need to be installed
- install python 3.10, update pip: `python -m pip install --upgrade pip`
- create venv: `python -m venv venv310`
- activate venv: (windows) `. venv310/Scripts/Activate.ps1` or (linux) `. venv310/bin/activate`
- install requirements: `pip install -r requirements.txt`
- run app: `python app.py` for all interfaces

## Generate a docker image

`docker build --tag demo-app .`
`docker run -d -p 5000:5000 demo-app`
