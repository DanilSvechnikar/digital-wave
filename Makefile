#* Variables
SHELL := /usr/bin/env bash
PYTHON ?= python3

ifeq ($(OS),Windows_NT)
	detected_OS := Windows
	MKDIR_CMD := mkdir
else
	detected_OS := $(shell uname -s)
	MKDIR_CMD := mkdir -p
endif


#* Installation Not for development
.PHONY: project-init
project-init:
	poetry install --no-interaction --without dev


#* Pip tools
.PHONY: pip-install
pip-install: poetry-export
	pip3 install --no-cache-dir --upgrade pip && \
	pip3 install --no-cache-dir -r requirements.txt

.PHONY: poetry-export
poetry-export:
	poetry lock -n && poetry export --without-hashes > requirements.txt

.PHONY: poetry-export-dev
poetry-export-dev:
	poetry lock -n && poetry export --with dev --without-hashes > requirements.dev.txt
