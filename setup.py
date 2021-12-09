#!/usr/bin/env python

"""The setup script."""

import os
import re
import sys

from setuptools import find_packages, setup


def get_version(*file_paths):
    """Retrieves the version from androidtvremote/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    )  # noqa
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


version = get_version("androidtvremote", "__init__.py")

readme = open("README.md").read()
history = open("HISTORY.md").read()
requirements = open("requirements.txt").readlines()
# if sys.platform == "win32":
#     requirements += open("requirements_windows.txt").readlines()
test_requirements = open("requirements_test.txt").readlines()

setup(
    author="Tim Santor",
    author_email="tsantor@xstudios.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="Android TV remote for Python.",
    entry_points={
        # "console_scripts": [
        #     "air-methods=androidtvremote.cli:run",
        #     "air-methods-udp=androidtvremote.cli:run_udp",
        # ],
    },
    install_requires=requirements,
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    # data_files=[
    #     (
    #         "androidtvremote",
    #         [
    #             "androidtvremote/data/filename.ext",
    #         ],
    #     )
    # ],
    include_package_data=True,
    keywords="remote android python",
    name="android-tv-remote",
    packages=find_packages(include=["androidtvremote", "androidtvremote.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://bitbucket.org/xstudios/air-methods-middleman",
    version=version,
    zip_safe=False,
)
