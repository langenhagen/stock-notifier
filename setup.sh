#!/bin/bash
# Set up the python project or die in case of error.
#
# Usage:
#   bash setup.sh
#
# author: andreasl
set -e

python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install --upgrade -r requirements.txt
