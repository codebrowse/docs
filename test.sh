#!/usr/bin/env bash

find . -name '*.pyc' | xargs rm; nosetests -x --pdb --with-doctest --with-coverage --cover-html --cover-erase
