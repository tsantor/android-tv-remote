# History
All notable changes to this project will be documented in this file. This project adheres to [Semantic Versioning](http://semver.org/).

## 0.1.6 (2023-06-22)
* New packaging method using `pyproject.toml`
* Added new tests

## 0.1.5 (2022-01-04)
* Ensure the ADB server is started as a background process during init.

## 0.1.4 (2021-12-12)
* Removed ADB `connect` params for `max_retries` and `retry_delay`.

## 0.1.3 (2021-12-10)
* Added ADB `connect` params for `max_retries` and `retry_delay`.

## 0.1.2 (2021-12-09)
* Added ADB disconnect method.
* Removed keycode constants from remote.py.  Can pass actual string constants to ADB.

## 0.1.1 (2021-12-08)
* Added KEYCODE_SOFT_SLEEP

## 0.1.0 (2019-04-25)
* First release on PyPI.
