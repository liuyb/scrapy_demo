clean:
	find . -name "*.pyc" -exec rm -rf {} \;

build: clean
	python setup.py bdist_egg

install: clean
	python setup.py install


.PHONY: clean, build, install
