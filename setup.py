from setuptools import setup, find_packages
from os import path


def read_lines(file_name):
    pth = path.join(path.dirname(__file__), file_name)
    with open(pth) as handle:
        return handle.readlines()

setup(
    name='Fattoush',
    package_data={'': ['*.txt']},
    author='Alistair Broomhead',
    version="0.0.0",
    author_email='alistair.broomhead@mindcandy.com',
    description="A delicious testing framework",
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=read_lines("requirements.txt"),
    include_package_data=True
)
