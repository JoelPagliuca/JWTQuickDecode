from setuptools import setup
from jwt_quick import __version__
import jwt_quick

dependencies = [
]

setup(
	name='JWTQuickDecoder',
	version=__version__,
	url='None',
	description='Quick JWT Claims Decoder - just pass in your jwt claims',
	author='Joel Pagliuca',
	author_email='pagliucajoel@gmail.com',
	py_modules=['jwt_quick'],
	install_requires=dependencies,
	entry_points={
		'console_scripts': ['jwt_quick=jwt_quick:main'],
	},
	include_package_data=True
)
