# Installation Guide

## Data Collection

Indicate how to collect the necessary data for this project :
- Where and how to get the data ?
- Where and how to integrate the data in the repository ? (example : in the direcctory data/raw)

## Dependencies

We'll need a list of the necessary dependencies to the project so that it can run locally :
- This project mainly uses python. The libraries used are python-venv, pandas, flask and more... (you can find them in the requirements directory)
- First and foremost, in order to install the dependencies, you need to install the python environment with the following command:
```
sudo apt -y install python3 python3-pip python3-venv
```
- Then create a virtual python environement to avoid incompatible libraries versions with the rest of your computer :
```
mkdir venv
python3 -m venv ./venv
# Create a virtual Python environments in venv directory. 
```
- Activate the virtual python environment
```
# In linux
source /venv/bin/activate
```
```
# In windows
venv\Scripts\activate
```
- And finaly, install the dependencies in your environment:
```
pip install -r requirements/requirements.txt
# install the right version of all packages from the file "requirements.txt"
```

## Development

Once your python environment setup and all the dependencies installed, you can launch the app in your virtual python environment :
```bash
# If not in the virtual python environment, activate it
# ---
# In linux
source /venv/bin/activate
#---
# In windows
venv\Scripts\activate
# ---

# then simply run the following command
python3 app.py
```

You can now access the web app here : http://localhost:5000