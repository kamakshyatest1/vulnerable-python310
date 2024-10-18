
from setuptools import setup, find_packages

setup(
    name="vulnerable_python310_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Flask==1.0",  # Flask 1.0 has known vulnerabilities
        "requests==2.19.1",  # Older version of requests has security vulnerabilities
        "PyYAML==3.13"  # PyYAML versions before 4.2b1 have security issues
    ],
    python_requires='==3.10.*',  # Restrict the project to only Python 3.10.x versions
    entry_points={
        'console_scripts': [
            'vulnerable_app = main:app'
        ]
    }
)
