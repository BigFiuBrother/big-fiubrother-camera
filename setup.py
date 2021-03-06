from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='big-fiubrother-camera',
   version='0.6.0',
   description='Big Fiubrother Camera application',
   license="GPLv3",
   long_description=long_description,
   long_description_content_type='text/markdown',
   author='Eduardo Neira, Gabriel Gayoso',
   author_email='aneira@fi.uba.ar',
   packages=['big_fiubrother_camera'],
   url= 'https://github.com/BigFiuBrother/big-fiubrother-camera'
)