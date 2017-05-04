build:
	python setup.py sdist

release:
	python setup.py sdist -d release

environment:
	virtualenv --no-site-packages venv # remember to source the venv/bin/activate

install: build
	pip install `ls -t dist/* | tail -n 1`

uninstall:
	pip uninstall JWTQuickDecoder -y

test:
	python -m unittest discover

clean:
	rm -f **/*.pyc

clobber: clean
	rm -f dist/*
	rm -rf *.egg-info