# This will automatically find out all the packages that are available in the entire ML application (in the directory)
from setuptools import find_packages,setup
from typing import List

# "-e ." is present in requirements.txt, this should not get read in this function, to ignore this we will do
HYPEN_E_DOT = '-e .'

# This function will return a list
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:

        # this will read the lines present in the requirements.txt but we have to replace the "\n" with the blank
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = "mlproject",
    version = "0.0.1",
    author = "Nakul",
    author_email = "kumar.nakul111@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)
