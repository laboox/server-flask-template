from setuptools import setup, find_packages
from distutils.core import setup

setup(
    name='Template Server',
    version='1.0',
    description='Template Flask Server with MongoDB',
    author='Sina Labbaf',
    author_email='slabbaf@uci.edu',
    url='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.4",
    install_requires=[
        'flask',
        'flask_security',
        'flask_mongoengine',
        'flask_cors'
        ],
    extras_require={
        'test': [
            'pytest'
        ]
    }
    )
