# importing dependency
from typing import List
from setuptools import setup, find_packages

# defining the HYPEN_E_DOT to setup file is call as a local packages
HYPEN_E_DOT = "-e ."

# defining the function to read line by line and install all requirements file also add this project setup pachages
def get_install_requirements() -> List[str]:
    with open('requirements.txt','r') as r:
        require_list = [line.split() for line in r.readlines()]
        # creating the condition to check the HYPEN_E_DOT in the requirements file to remove and run it
        if HYPEN_E_DOT in require_list:
            require_list.remove(HYPEN_E_DOT)
            
            return require_list
        
# definig the project detail
PROJECT_NAME = "student"
PROJECT_VERSION = "1.0.0"
PROJECT_DESCRIPTION = "Student Performence Check and Prediction Pass or Fail System"
AUTHOR = "HRIDOY KHAN"
AUTHOR_EMAIL = "rkhridoyinfo@gmail.com"
PROJECT_URI = "https://github.com/hridoy1335/End-to-End-Student-Performance-ML-Project"
# setup the setup details
setup(
    name=PROJECT_NAME,
    version=PROJECT_VERSION,
    description=PROJECT_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=PROJECT_URI,
    packages=find_packages(),
    install_requires = get_install_requirements()
)