from setuptools import setup, find_packages

setup(
    name='wilayati',  # Replace with your package name
    version='1.0.0',  # Initial release version
    packages=find_packages(),  # Automatically find packages in the current directory
    install_requires=[],  # List of dependencies
    author='Rabah Djebbes',  # Replace with your name
    author_email='rabahwork@gmail.com',  # Replace with your email
    description='This Python module provides functionality for searching and retrieving information about Algerian Wilayas (provinces) and their respective Communes (municipalities).',  # Short description of the package
    long_description=open('README.md').read(),  # Read long description from README file
    long_description_content_type='text/markdown',  # Type of long description content
    url='https://github.com/rabahdj2002/Wilayas-of-Algeria',  # URL of the project (GitHub, etc.)
    classifiers=[  # List of classifiers that describe the package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum version requirement of Python
)
