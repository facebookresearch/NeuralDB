#
# Copyright (c) 2021 Facebook, Inc. and its affiliates.
#
# This file is part of NeuralDB.
# See https://github.com/facebookresearch/NeuralDB for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import shutil
from pathlib import Path
from setuptools import find_packages, setup

stale_egg_info = Path(__file__).parent / "neuraldb.egg-info"
if stale_egg_info.exists():
    shutil.rmtree(stale_egg_info)

setup(
    name="neuraldb",
    version="0.0.0",
    author="",
    author_email="jt719@cam.ac.uk",
    description="NeuralDB Baseline implementation",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="NLP neuraldb neural database deep learning transformer",
    license="Apache",
    url="",
    package_dir={"": "src"},
    packages=find_packages("src"),
    extras_require=[],
    entry_points={"console_scripts": [""]},
    python_requires=">=3.6.0",
    install_requires=["transformers==4.6.0","torch","datasets","fever-drqa"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
