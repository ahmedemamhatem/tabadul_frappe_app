from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tabadul_frappe_app/__init__.py
from tabadul_frappe_app import __version__ as version

setup(
	name="tabadul_frappe_app",
	version=version,
	description="tabadul_frappe_app",
	author="tabadul_frappe_app",
	author_email="tabadul_frappe_app",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
