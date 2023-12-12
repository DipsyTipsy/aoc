#!/bin/bash
PYTHONDONTWRITEBYTECODE=1 poetry run ptw -c -v --ignore .venv --ext .txt,.py -- -- -s -raFP -W ignore::pytest.PytestReturnNotNoneWarning -p no:cacheprovider
