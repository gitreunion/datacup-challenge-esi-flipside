# Installation Guide

## Data Collection

Indicate how to collect the data necessary for this project :
- Where and how to get the data ?
- Where and how to integrate the data in the repository ? (example : in the direcctory data/raw)

## Dependencies

List of the dependencies necessary to the project so that it can run locally :
- This project use principally python. The libraries used are python-venv, pandas, flask and others... (you can find them in the requirements directory)
- In order to install the dependencies you need first to install the python envirement:
```
sudo apt -y install python3 python3-pip python3-venv
```
- Then create an virtual python environement to avoid inconpatible libraries version:
```
mkdir venv
python3 -m venv ./venv
# Create a virtual Python environments in venv directory. 
```
Activate the virtual python environment
```
# In linux
source /venv/bin/activate
```
```
# In windows
venv\Scripts\activate
```
- Finaly install the libraries in your environment:
```
pip install -r requirements/requirements.txt
# install all the librairies on the right version
```

## Development

Once your python envirements setup and all the dependencies installed, you can lanch the app in your virtual python envirenment :
```
# If not in the virtual python environment you can activate it
# ---
# In linux
# source /venv/bin/activate
" ---
# In windows
# venv\Scripts\activate
# ---

# then simply run the following command
python3 app.py
```

You can now access the web app here : http://localhost:5000