PATH:=bin/:${PATH}
.PHONY: all clean cover doc test

help:
	@echo "Available commands:"
	@echo "  clean			remove temp files and static generated docs"
	@echo "  cover			generate test coverage"
	@echo "  doc			generate internal doc"
	@echo "  test			run all tests"

clean:
	find ./ -type f -name '*.pyc' -exec rm -f {} \;
	rm -rf cover .coverage
	rm -rf docs/build

cover:
	ENV=test ./bin/nosetests -s -v --with-coverage --cover-html --cover-html-dir ./coverage

test:
	ENV=test ./bin/nosetests -s --nologcapture

all: clean

doc: clean
	sphinx-build -b html docs/source docs/build/html
