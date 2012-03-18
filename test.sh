#!/usr/bin/env bash

find . -name '*.pyc' | xargs rm; nosetests -x --with-doctest --with-coverage --cover-html --cover-erase

