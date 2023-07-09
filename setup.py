from setuptools import setup,find_packages
setup(name="census_income",
    version="0.0.1",
    author="Monika",
    author_email="saimonika01@gmail.com",
    package=find_packages(),
    install_requirements=["pandas,numpy,flask"]
)