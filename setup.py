# -*- coding: utf-8 -*-

import codecs
import os
import re
import sys

from setuptools import find_packages, setup

name = "android-tv-remote"
package = "androidtvremote"
description = ""
url = "https://bitbucket.org/tsantor/python-android-tv-remote"
author = "Tim Santor"
author_email = "tsantor@xstudios.agency"
license = "MIT"
install_requires = []
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
]
entry_points = {
    "console_scripts": [
        # 'android-remote = androidtvremote.androidtvremote:main',
    ]
}


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = codecs.open(os.path.join(package, "__init__.py"), encoding="utf-8").read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(
        1
    )


if sys.argv[-1] == "build":
    os.system("python setup.py sdist bdist_wheel")

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    args = {"version": get_version(package)}
    print("You probably want to also tag the version now:")
    print(
        "    git tag -a %(version)s -m 'version %(version)s' && git push --tags" % args
    )
    sys.exit()

EXCLUDE_FROM_PACKAGES = []

setup(
    name=name,
    version=get_version(package),
    description=description,
    long_description=description,
    url=url,
    author=author,
    author_email=author_email,
    license=license,
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    install_requires=install_requires,
    classifiers=classifiers,
    entry_points=entry_points,
    zip_safe=False,
)
