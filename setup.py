from glob import glob
import setuptools, re, os
from src.mercutio import __author__ as AUTHOR
from src.mercutio import __license__ as LICENSE
from src.mercutio import __email__ as EMAIL
from src.mercutio._version import __version__ as VERSION

with open("README.md", "r") as f:
    LONG_DESCRIPTION = re.sub(r'\!\[cropped dragon gif\]\(docs\/cropped.gif\)', '', f.read()) # substitute out the gif image

with open('requirements.txt') as f:
    REQUIRED = f.read().splitlines()

setuptools.setup(
    name="mercutio",
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    description="yet another character creation engine",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/signebedi/mercutio",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIRED,
    python_requires='>=3.6',
)
