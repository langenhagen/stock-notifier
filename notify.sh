#!/bin/bash
# Load the stock-notifier's venve, run the stock notifier.
#
# author: andreasl
set -e

cd "$(dirname "${BASH_SOURCE[0]}")"

source .venv/bin/activate

python notify.py
