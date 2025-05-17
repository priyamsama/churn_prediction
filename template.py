import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_of_files = [
    "data/",
    "notebooks/",
    "models/",
    "churn_model.py",
    "requirements.txt",
    ".gitignore",
    "README.md",
]

for filepath_str in list_of_files:
    filepath = Path(filepath_str)
    
    if filepath_str.endswith('/'):  # Folder path
        os.makedirs(filepath, exist_ok=True)
        logging.info(f"Created directory: {filepath}")
    else:  # File path
        filedir = filepath.parent
        if filedir != Path('.'):
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Created directory: {filedir} for file: {filepath.name}")
        
        if not filepath.exists():
            filepath.touch()
            logging.info(f"Created empty file: {filepath}")
        else:
            logging.info(f"File already exists: {filepath}")
