
from setuptools import find_packages, setup 

from typing import List 


def get_requirements() -> List[str]: 
    
    requirements_lst: List[str] = []
    try:
        with open('requirements.txt') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("-e ."):
                    requirements_lst.append(line)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")
    
    return requirements_lst

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Ashrafhusen Raj",
    author_email = "araj11@hawk.illinoistech.edu",
    packages = find_packages(),
    install_requires = get_requirements(),
    description = "End to end Network Security Project",
)



