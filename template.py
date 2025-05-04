import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s}:%(message)s]')

list_of_files = [
    "src/__init__.py",
    "src/__helper__.py",
    "src/prompt.py",
    "setup.py",
    "research/trial.py",
    "app.py",
    "store_index.py",
    "static",
    "templates/chat.html"
]
for filepath in list_of_files:

    filepath= Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filename) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty files : {filepath}")
    else:
        logging.info(f"{filename} is already created")