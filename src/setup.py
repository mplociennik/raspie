from setuptools import setup, find_packages

setup (
       name='raspie',
       version='0.2',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['foo>=3'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='Cieniu',
       author_email='marcin@cieniu.pl',

       #summary = 'Just another Python package for the cheese shop',
       url='',
       license='',
       long_description='Description in progress... :)',

       # could also include long_description, download_url, classifiers, etc.

  
       )