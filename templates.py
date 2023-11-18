import os
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO, format='[%(asctime)s: %(message)s:]')

project_name = 'cnnClassifier'
list_of_dir = [
    f'.guthub/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'config/config.yaml',
    f'params.yaml',
    f'requirements.txt',
    f'setup.py',
    'dvc.yaml',
    'research/trails.ipynb',
    'templates/index.html'
]


for filepath in list_of_dir:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Create a directory: {filedir} for: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) != 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Create a empty file in: {filepath}")
    
    else:
        logging.info(f"File is already exists {filepath}")
        


