#!/usr/bin/env bash

find . -name '*.pyc' | xargs rm; nosetests -x --with-doctest
