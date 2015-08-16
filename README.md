# parse_setup.py

Simple script, which parse `setup.py` file in secure docker container in order to extract requirements.

Malicious `setup.py` like this:

    from setuptools import setup
    import shutil

    setup(
        install_requires=[
            shutil.rmtree('/'),  # very dangerous!
            'django',
        ],
    )

should not be pass to `exec` function. Regular expressions are also not a solution for every kind of `setup.py` file.
Fortunately there is docker! :)

# Usage

    $ docker build -t parse .
    $ ./parse.sh ./example_files/setup.py
    #[OK]
    lxml==3.4.4
    termcolor==1.1.0

    $ ./parse.sh ./example_files/dangerous_setup.py
    [Errno 39] Directory not empty: '/usr/local/lib'
    #nothing bad happend :)
