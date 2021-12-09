.PHONY: clean clean-pyc clean-build help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

python_version=3.9.4
venv=androidtvremote_env
aws_profile=
s3_bucket=

env: ## create pyenv virtualenv
	mkdir -p ~/.venvs
	python3.9 -m venv ~/.venvs/${venv}
	source ~/.venvs/${venv}/bin/activate

pyenv:  ## create pyenv virtualenv
	pyenv virtualenv ${python_version} ${venv} && pyenv local ${venv}

reqs:  ## install development requirements
	python -m pip install -U pip wheel \
	&& python -m pip install -r requirements.txt \
	&& python -m pip install -r requirements_dev.txt

clean: clean-build clean-pyc ## remove all build, test, coverage and Python artifacts

destroy_penv:  ## destroy pyenv virtualenv
	pyenv uninstall ${venv}

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

# release: dist ## package and upload a release
# 	twine upload dist/*

dist: clean ## builds source and wheel package
	# python -m build
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install_edtiable: clean ## install the package to the active Python's site-packages
	pip install -e .

push_to_s3:  # push distro to S3 bucket
	aws s3 sync --profile=${aws_profile} --acl public-read ./dist/ s3://${s3_bucket}/dist/ \
        --exclude "*" --include "*.whl"

# pull_from_s3:  # pull distros from S3 bucket
# 	aws s3 sync --profile=${aws_profile} s3://${s3_bucket}/dist/ . \
#         --exclude "*" --include "*.whl"
