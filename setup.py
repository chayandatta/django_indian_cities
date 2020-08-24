from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="django_indian_cities",
    version="0.0.1",
    description="Django Indian Cities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["dj-city"],
    package_dir={"": "src"},
    url="https://github.com/chayandatta/django_indian_cities",
    author="Chayan Datta",
    author_email="chayan.datta1996@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
