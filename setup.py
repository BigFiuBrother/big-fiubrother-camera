from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='big-fiubrother-camera',
   version='0.1',
   description='Big Fiubrother Camera application',
   license="GPLv3",
   long_description=long_description,
   author='Eduardo Neira',
   author_email='aneira@fi.uba.ar',
   packages=['big-fiubrother-camera']
)