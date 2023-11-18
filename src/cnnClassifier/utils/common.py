import imp
import os
from sympy import content
from cnnClassifier import logger
from pathlib import Path
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
import json
from typing import Any
import joblib
import base64



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    
    try:
        with open(path_to_yaml) as file:
            content = yaml.safe_load(file)
            logger.info(f'Successfully loaded yaml file: {path_to_yaml}')
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError(f'yaml file is empty {path_to_yaml}')
    
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(list_of_dir: list, verbose=True):
    for path in list_of_dir:
        path = Path(path)
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Create direcory at: {path}')


@ensure_annotations
def load_json(json_file_path: Path) -> ConfigBox:
    with open(json_file_path) as f:
        content = json.load(f)
    
    logger.info(f'Loaded json file at: {json_file_path}')
    return ConfigBox(content)

@ensure_annotations
def save_json(json_file_path: Path, data: dict):
    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f'json file saved at: {json_file_path}')


@ensure_annotations
def load_bin(bin_file_path: Path) -> Any:
    data = joblib.load(bin_file_path)
    logger.info(f'loaded bin file at: {bin_file_path}')
    return data


@ensure_annotations
def save_bin(bin_file_path: Path, data: Any):
    joblib.dump(value=data, filename=bin_file_path)
    logger.info(f'Saved bin file at: {bin_file_path}')


def decodeImage(imgString, filename):
    imgdata = base64.b64decode(imgString)
    with open(filename, 'wb') as f:
        f.write(imgdata)


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        base64.b64encode(f.read())


