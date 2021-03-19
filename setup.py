from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

classifiers = ['Development Status :: 5 - Production/Stable',
               'Intended Audience :: Developers',
               'Topic :: Software Development :: Libraries',
               'Topic :: System :: Hardware',
               'License :: OSI Approved :: MIT License',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 3.5']

setup(
    name='MicroPython-sht1x',
    version=version,
    url='https://github.com/kapetan/MicroPython-sht1x',
    license='MIT',
    description='MicroPython library for Sensirion SHT1x series of temperature & humidity sensors.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    classifiers=classifiers,
    keywords='sht sensor sht1x sensirion T temperature humidity RH dew-point celsius measurement'
             ' gpio serial 2-wire crc crc-8 hardware driver ic',
    py_modules=find_packages()
)
