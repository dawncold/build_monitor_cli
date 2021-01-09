from setuptools import setup

setup(
    name = "build_monitor_cli",
    version = "1.0.0",
    author = "Zhen Tian",
    author_email = "zhen.tian@thoughtworks.com",
    description = 'Azure devops builds commandline monitor',
    license = "BSD",
    keywords = "azure devops",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)