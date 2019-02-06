# (c) 2014 Mind Candy Ltd. All Rights Reserved.
# Licensed under the MIT License; you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://opensource.org/licenses/MIT.

from setuptools import setup, find_packages
from os import path
import sys


sys.path.insert(0, path.join(path.dirname(__file__), 'src'))
import fattoush


def read_lines(file_name):
    pth = path.join(path.dirname(__file__), file_name)
    with open(pth) as handle:
        return handle.readlines()

setup(
    name='Fattoush',
    package_data={'': ['*.txt']},
    author='Alistair Broomhead',
    version=str(fattoush.VERSION),
    author_email='alistair.broomhead+python@gmail.com',
    description="A delicious testing framework",
    license='MIT',
    url='https://github.com/alistair-broomhead/fattoush',
    #download_url='https://github.com/mindcandy/fattoush/zipball/master',
    long_description=fattoush.__doc__,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=read_lines("requirements.txt"),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'fattoush = fattoush.runner.bin:console']
    }
)
