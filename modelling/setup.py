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
    install_requires=["transformers==4.5"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
