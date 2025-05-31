from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """This function will return List of requirements"""
    requirements=[]
    HYPEN_E_DOT = "-e ."
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements

setup(
    name='ML_end_to_end_project',
    version='0.0.1',
    author='Rushikesh',
    author_email='rushi2001bobade@gmail.com',
    install_requires =get_requirements('requirements.txt'),
    packages=find_packages()
)