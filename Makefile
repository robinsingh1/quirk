test:
	py.test tests

install:
	pip install -r requirements.txt

publish:
	python setup.py bdist_wheel --universal
	ls dist
	# twine upload dist/*
	rm -fr build dist quirk.egg-info
