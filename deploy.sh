python setup.py sdist bdist_wheel
twine upload dist/* --repository pypi --config-file .pypirc # uses project-scoped API token for mercutio

# TO DO: 
## ADD support for version specification (eg. passing version number to setup.py)
## ADD support for automatic (simultaneous) Github releases