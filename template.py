# importing dependency
import os
import logging
from pathlib import Path

# defining the project name
project_name = "student"

# defining the project path
list_of_file = [
    f"github/workflows/main.yaml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_preprocessing.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/model_trainner.py",
    f"src/{project_name}/components/model_evaluator.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/constants.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/pipeline/trainnig_pipeline.py",
    f"src/{project_name}/pipeline/stage_1_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_2_data_preprocessing.py",
    f"src/{project_name}/pipeline/stage_3_data_validation.py",
    f"src/{project_name}/pipeline/stage_4_model_trainning.py",
    f"src/{project_name}/pipeline/stage_5_model_evaluation.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/useable_function.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/logger/loggers.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/exception/exceptions.py",
    f"notebook/resource.ipynb",
    f"config/config.yaml",
    f"config/schema.yaml",
    f"config/params_schema.yaml",
    f"app.py",
    f"main.py",
    f"setup.py",
    f"requirements.txt",
    f".dockerignore",
    f"Dockerfile",
]

# building file and folder creating logic
for file in list_of_file:
    file_path = Path(file)
    file_dir,file_name = os.path.split(file_path)
    
    # creating the file if it does not exist
    if file_dir != "" :
        os.makedirs(file_dir,exist_ok=True)
        
    # creating the directory if it does not exist
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0 ) :
        with open(file_path, 'w') as f :
            pass
        
    else:
        logging.info(f"{file_name} is already exists")
        
print("OK")    