import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctimate)s]: %(message)s: ')

project_name = "textsummarizer"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/logging/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utiles/__init__.py",
    f"{project_name}/utiles/common.py",
    "app.py",
    "main.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "params.yaml",
    "config/config.yaml",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'creating directory: {filedir} for file {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): 
        with open(filepath,'w') as f: 
            pass 
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")