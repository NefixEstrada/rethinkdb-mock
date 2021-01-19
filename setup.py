from setuptools import setup

version_path = 'rethinkdb_mock/version.py'

exec(open(version_path).read())


setup(
    name="rethinkdb_mock",
    zip_safe=True,
    version=VERSION,
    description="A pure-python in-memory mock of rethinkdb (formerly MockThink)",
    url="http://github.com/scivey/rethinkdb_mock",
    maintainer="Christopher Baklid",
    maintainer_email="cbaklid@gmail.com",
    packages=['rethinkdb_mock'],
    package_dir={'rethinkdb_mock': 'rethinkdb_mock'},
    install_requires=['rethinkdb>=2.4.8', 'python-dateutil', 'future'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Topic :: Database",
        "Topic :: Software Development :: Testing :: Mocking",
    ],
    python_requires='>=3.9',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
