#!/usr/bin/env bash
virtualenv _venv
source _venv/bin/activate
python2 -m pip install -r requirements.txt
python main.py build
mv build/404.xhtml build/404.html
cp -r build/* ../
