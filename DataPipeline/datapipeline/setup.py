from setuptools import setup, find_packages

setup(
    name='datapipeline',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A data pipeline package for ingesting and cleaning agricultural data from a sqlite db',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas', 'pytest'],  
    url='https://github.com/BlackIG/datapipeline',
    author='Ikechukwu Chilaka',
    author_email='chilax93@gmail.com'
)
