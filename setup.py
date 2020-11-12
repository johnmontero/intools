import os
import intools
from setuptools import setup, find_packages

current_dir = os.path.abspath(os.path.dirname(__file__))

with open(f'{current_dir}/requirements.txt') as f:
    install_requires = f.read().splitlines()

long_description = "InTools"

setup(
    name             = 'InTools',
    description      = 'InTools - Is a simple Infrastructure tool for task.',
    packages         = find_packages(),
    package_data     = {
        'intools': ['templates/*']
    },
    author           = 'intools',
    author_email     = 'intools [at] gmail.com',
    scripts          = ['bin/intools'],
    install_requires = install_requires,
    version          = intools.__version__,
    url              = 'https://github.com/johnmontero/intools',
    license          = "MIT",
    zip_safe         = False,
    keywords         = "task, tools, infra",
    long_description = long_description,
    classifiers      = [
                        'Development Status :: 4 - Beta',
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: MIT License',
                        'Topic :: Software Development :: Build Tools',
                        'Topic :: Software Development :: Libraries',
                        'Topic :: Software Development :: Testing',
                        'Topic :: Utilities',
                        'Operating System :: MacOS :: MacOS X',
                        'Operating System :: Microsoft :: Windows',
                        'Operating System :: POSIX',
                        'Programming Language :: Python :: 3.9',
                        'Programming Language :: Python :: 2.7',
    ]
)