
**Features**

- Simple [Flask](http://flask.pocoo.org/) API server
- Avoid any confusing and complex python or flask tricks
- Flexible API structure
- Good booster for researches

- Using MongoDB through [flask-mongoengine](https://github.com/MongoEngine/flask-mongoengine)
- Authentication and authorization through [flask-security](https://pythonhosted.org/Flask-Security/)

# Simple Flask Server Template
A very simple real life template using Flask and MongoDB.

![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?style=for-the-badge)  ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg?style=for-the-badge)

**Table of Contents**

# Directory tree

``` bash
├── server-flask-template/
│   ├── server/
│   │   ├── controllers/
│   │    │   ├── __init__.py
│   │    │   ├── auth.py
│   │    │   ├── test.py
│   │   ├── models/
│   │    │   ├── __init__.py
│   │    │   ├── models.py
│   │   ├── __init__.py
│   │   ├── config.cfg
│   │   ├── core.py
│   │   ├── server.py
├── README.md
├── MANIFEST.in
├── package.json
├── setup.cfg
└── .gitignore
```
# Installation

To install server package permanently write this in project's root:
``` bash
sudo python3 setup.py install
```
Or to install as development server write: 
``` bash
sudo python3 setup.py develop
```
Or if you want to use flask debug mode and just install dependencies try: 
``` bash
sudo pip install -e .
```
To learn more about deploying flask applications and debug servers read [here](http://flask.pocoo.org/docs/1.0/deploying/).
