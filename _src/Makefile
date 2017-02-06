SHELL = /usr/bin/env bash
CPDIR = ../
.PHONY: clean buildsite copy all

all: clean buildsite copy

clean:
	-rm -r build/*
	-rm $(CPDIR)*.html
	-rm -r $(CPDIR)contact
	-rm -r $(CPDIR)team
	-rm -r $(CPDIR)static

buildsite:
	virtualenv _venv
	source _venv/bin/activate
	python2 -m pip install -r requirements.txt
	python main.py build

copy:
	cp -r build/* $(CPDIR)
