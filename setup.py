from setuptools import setup

setup(
    name='rgkit',
    version='0.1',
    packages=['rgkit',],
    package_data={'rgkit': ['maps/*.py']},
    license='Unlicense',
    long_description=open('README.md').read(),
    entry_points = {
        'console_scripts': [
        'run = rgkit.run:main',
        'mapeditor = rgkit.mapeditor:main'
        ]
    },
)