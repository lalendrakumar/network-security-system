from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """This function returns a list of requirements"""
    requirements = []
    with open("requirements.txt") as file:
        for line in file:
            req = line.strip()
            if req and req != "-e .":
                requirements.append(req)
    return requirements

setup(
    name="network_security",
    version="0.0.1",
    author="Lalendra",   # Aapka naam yaha daaliye
    author_email="lalendrakumar4@example.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
