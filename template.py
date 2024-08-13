import os
import logging
from pathlib import Path

list_of_files = [
                  "SRC/Components/__init__.py",
                  "SRC/Components/Data_Ingestion.py",
                  "SRC/Components/Model_Train.py",
                  "SRC/Components/Evaluation.py",
                  "app.py",
                  "logger.py",
                  "Exception.py",
                  "setup.py",
                ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Created directory : {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created file : {filepath}")
    else:
        logging.info(f"File already exists : {filepath}")