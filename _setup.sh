#!/bin/bash

# This will initialize the Python environment needed for testing.

python3 -m venv venv-3.8
source venv-3.8/bin/activate
pip install -r requirements.txt

