#!/usr/bin/env bash

echo "starting nosetests"
nosetests
echo "finished nosetests"

echo "starting pep8 test"
echo "checking files under root directory"
pep8 *.py

echo "checking files under ela/"
cd ela
pep8 *.py

echo "checking files under test/"
cd ../test
pep8 *.py

echo "finished nosetests"