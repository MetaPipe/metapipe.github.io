CPDIR =../
.PHONY: clean buildsite copy all

all: clean buildsite copy

clean:
	-rm -r build/*
	-rm ../*.html
	-rm -r ../contact
	-rm -r ../team
	-rm -r ../static

buildsite:
	virtualenv _venv
	. _venv/bin/activate
	python2 -m pip install -r requirements.txt
	python main.py build

copy:
	cp -r build/* $(CPDIR)
