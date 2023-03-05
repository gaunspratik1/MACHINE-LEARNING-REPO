from setuptools import setup, find_packages
from typing import List


#declaring variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.4"
AUTHOR = "Pratik"
DESCRIPTION = "This is my first FSDS batch machione learning Project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()-> List[str]:
    """
    Discription: This function is going to return list of requirement
    mention in requirements.txt file

    return: this function is going to return a list which contains name 
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name= PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description= DESCRIPTION,
packages= find_packages(), #["housing"]
install_requires = get_requirements_list() 

)
