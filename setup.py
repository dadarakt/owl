try: 
	from setuptools import setup
except ImportError:
	from distutils.core import setup

confg = {
	'description': 'Owl project',
	'author': 'dadarakt',
	'url' : 'http://github.com/dadarakt/owl',
	'author_email' : 'janniseichborn@gmail.com',
	'version' : '0.1',
	'packages' ['owl'],
    	'scripts' :[],
	'name' : 'owl-project'
}

setup(**config)
