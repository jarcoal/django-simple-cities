from setuptools import setup

setup(
    name="simple-cities",
    version="0.0.1",
    description="Simple Alternative to GeoDjango",
    long_description="Simple Alternative to GeoDjango",
    keywords="django, cities, geo",
    author="Jared Morse <jarcoal@gmail.com>",
    author_email="jarcoal@gmail.com",
    url="https://github.com/jarcoal/django-simple-cities",
    license="BSD",
    packages=["cities"],
    zip_safe=False,
    install_requires=[],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)