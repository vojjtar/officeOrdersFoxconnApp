from setuptools import setup

# setting basic info about the web app and specifying required libraries (flask, ...)
setup(
    name='foxconnApp',
    packages=['foxconnApp'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
