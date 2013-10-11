{{ cookiecutter.project_name }}
===============================

{{ cookiecutter.project_short_description}}


Installation
---

	# install pip:
	$ sudo easy_install pip

	# install virtualenv:
	$ sudo easy_install virtualenv

	# inside your repo, create env and activate it:
	$ virtualenv env/ && . env/bin/activate

	# install required packages
	$ python setup.py install


Documentation
---
	# generate new static doc
	$ make doc


Testing
---
	# run all tests
	$ make test
	
	# check for tests coverage
	$ make cover

Start service
---

	$ ENV=dev python app.py
	
Deployment
---
Provide deployment instruction here