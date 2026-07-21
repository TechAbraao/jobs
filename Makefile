.PHONY: install clean

VENV := .venv
PIP := $(VENV)/bin/pip

install:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e .

clean:
	rm -rf $(VENV) build dist *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +