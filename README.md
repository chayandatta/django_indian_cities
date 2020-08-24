[![PyPI version](https://badge.fury.io/py/indian-cities.svg)](https://badge.fury.io/py/indian-cities)

# django_indian_cities -- Simple django states cities for india

## How to use this

> To import

```
from dj_city import CITY_CHOICES, STATE_CHOICES

class myModel(models.Model):
    state = models.CharField(choices=STATE_CHOICES, null=False, max_length=20)
    city = models.CharField(choices=CITY_CHOICES, null=False, max_length=20)
```

Requirements:

Any version of Python, Django

## Installation

Install django-indian-cities:

> pip install indian_cities
