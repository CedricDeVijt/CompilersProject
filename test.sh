#!/bin/bash

python3 -m venv venv > /dev/null
source venv/bin/activate
pip install -r requirements.txt > /dev/null

python -m pytest src/tests/MIPS_tests