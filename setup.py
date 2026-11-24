from setuptools import find_packages, setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wilayati',
    version='1.0.1',
    packages=find_packages(),
    package_data={'wilayati': ['*.json']},  # Ship the data files inside the package
    include_package_data=True,
    install_requires=[],
    author='Rabah Djebbes',
    author_email='rabahwork@gmail.com',
    description='This Python module provides functionality for searching and retrieving information about Algerian Wilayas (provinces) and their respective Communes (municipalities).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rabahdj2002/Wilayas-of-Algeria',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
