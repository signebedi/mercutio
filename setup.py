from glob import glob
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="mercutio",
    version="0.7.1",
    author="Sig Janoska-Bedi",
    author_email="signe@siftingwinnowing.com",
    description="yet another character creation engine",
    long_description=long_description,
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
    install_requires=required,
    python_requires='>=3.6',
)
