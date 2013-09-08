#!/usr/bin/env python

__author__ = 'Yuta Hayashibe' 
__version__ = ""
__copyright__ = ""
__license__ = "GPL v3"


import os
import sys 
if len(sys.argv) >=2:
    cmd1 = sys.argv[1]
else:
    cmd1 = ""

import subprocess

if cmd1 in ["build", "install"]:
    subprocess.check_call(["make"])
    os.rename("train", "liblinear-train")
    os.rename("predict", "liblinear-predict")

    subprocess.check_call(["make", "lib"])

elif cmd1 == "clean":
    try:
        os.remove("liblinear-train")
    except OSError:
        pass

    try:
        os.remove("liblinear-predict")
    except OSError:
        pass
    subprocess.check_call(["make", "clean"])


version_file = os.path.join(os.path.dirname(__file__), 'VERSION')
with open(version_file) as fh:
    ll_version = fh.read().strip()


from setuptools import setup, find_packages, Extension
setup(
    name = "ll",
    version = ll_version,
    author = "Yuta Hayashibe",
    description = "This is liblinear buindings for Python.",
    license = "The modified BSD license",
    url = "https://github.com/shirayu/liblinear-unofficial",
    package_dir={'ll': 'python'},
    package_data = { "": [ "../liblinear.so.1", "../VERSION"] },
    scripts = ["./liblinear-train", "./liblinear-predict"],
    packages=['ll'],
#    packages = find_packages(),
#    py_modules = ['python/liblinear','python/liblinearutil'],
#    packages = ['python/liblinear', 'python/liblinearutil', 'python/__init__'],

)

