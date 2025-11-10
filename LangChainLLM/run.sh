#!/bin/bash
# Run Streamlit app using the local virtual environment

cd "$(dirname "$0")"
./venv/bin/python -m streamlit run main.py "$@"
