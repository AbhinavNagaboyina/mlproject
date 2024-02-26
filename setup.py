from setuptools import find_packages, setup
from typing import List

# Your original code for handling dependencies seems fine,
# but ensure that the '-e .' is correctly handled if it's not needed.

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        # If '-e .' is in requirements, it's removed as you've done.
        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements

setup(
    name="ML_project",
    version='0.0.1',
    author='Abhi',
    author_email='abhinavumkc@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),  # Corrected line
)
