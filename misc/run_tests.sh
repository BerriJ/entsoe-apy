#!/bin/sh

# Run pytest for the entsoe-api-py project
# This script activates the virtual environment and runs all tests

set -e

# Run tests with the virtual environment Python
./.venv/bin/python -m pytest -v

echo "All tests completed!"
