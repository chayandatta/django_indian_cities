[![PyPI version](https://badge.fury.io/py/indian-cities.svg)](https://badge.fury.io/py/indian-cities)
![PyPI - License](https://img.shields.io/pypi/l/indian-cities)
[![Downloads](https://pepy.tech/badge/django-indian-cities)](https://pepy.tech/project/django-indian-cities)

# django_indian_cities -- states & cities for india

## How to use this

> To import

```
from dj_city import CITIES

class myModel(models.Model):

    city = models.CharField(choices=CITIES, null=False, max_length=20)

```

Requirements:

Any version of Python, Django

## Installation

To install this

> pip install indian_cities

---

### issues

- [ ] pipenv install indian_cities not working
