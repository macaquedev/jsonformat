import setuptools


setuptools.setup(
    name='jsonformat',
    version='0.0.5',
    license="MIT",
    entry_points={
        'console_scripts': ['jsonformat=jsonformat:cli'],
    },
    author='Alex Pylypenko',
    description='A simple, small command line utility to format json files.',
    install_requires=[
        'setuptools',
        'pip'
    ],
    python_requires='>=3.3'
)