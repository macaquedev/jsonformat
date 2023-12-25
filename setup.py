import setuptools


setuptools.setup(
    name='jsonformat',
    version='0.0.11',
    license="MIT",
    entry_points={
        'console_scripts': ['jsonformat=jsonformat.jsonformat:cli'],
    },
    packages=["jsonformat"],
    url="https://github.com/macaquedev/jsonformat",
    author='Alex Pylypenko',
    author_email="macaquedev@gmail.com",
    description='A simple, small command line utility to format json files.',
    long_description=open('README.md').read(),
    long_description_content_type="text/x-rst",
    install_requires=[
        'setuptools',
        'pip'
    ],
    python_requires='>=3.3'
)
