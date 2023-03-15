# build the packagae as a package or an api using distutils
from setuptools import find_packages, setup
from typing import List


# make a fn that takes string input and outputs a list
def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements ]

        if "-e ." in requirements:
            requirements.remove("-e .")
setup (
name ="mlproject",
version="0.0.1", 
author="prateek",
author_email="prateek.gsharma@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')




)