[![PyPI version](https://badge.fury.io/py/indian-cities.svg)](https://badge.fury.io/py/indian-cities)
![PyPI - License](https://img.shields.io/pypi/l/indian-cities)
[![Downloads](https://pepy.tech/badge/indian-cities)](https://pepy.tech/project/indian-cities)

# indian-cities  -- states & cities for india 🇮🇳

## Why?

If there was something plug 🔌 and play
which can be just imported and it'll fill the choices fields with Indian cities or states.
How good it'll be.


## How to use this

> To import just add this line

```
from indian_cities.dj_city import cities
```
> Test it

```
print(cities[0])
```
Now if the output looks like this
```
('Andaman and Nicobar Islands', (('Port Blair', 'Port Blair'),))
```
Then awesome, it did work 👍
```
class myModel(models.Model):

    city = models.CharField(choices=cities, null=False, max_length=20)

```

### Requirements:

Any version of Python, Django

## Installation

To install this

> pip install indian-cities

---
## Connect with me:

LinkedIn: https://www.linkedin.com/in/chayandatta/

github: https://github.com/chayandatta

---

made with ❤️ and 🐍