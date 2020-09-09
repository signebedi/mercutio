python setup.py sdist bdist_wheel
twine upload dist/* --config-file .pypirc # uses project-scoped API token for mercutio