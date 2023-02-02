from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tubsan/__init__.py
from tubsan import __version__ as version

setup(
	name="tubsan",
	version=version,
	description="Customizations for Tubsan requirements",
	author="Geoffrey Karani",
	author_email="karani@upeosoft.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
