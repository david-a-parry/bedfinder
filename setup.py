try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(
    name = "bedfinder",
    packages = [""],
    version = "0.1.1",
    description = "Read BED genomic interval files into memory and search.",
    author = "David A. Parry",
    author_email = "david.parry@ed.ac.uk",
    url = "https://github.com/david-a-parry/bedfinder",
    download_url = 'https://github.com/david-a-parry/bedfinder/archive/0.1.1.tar.gz',
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=[],
    python_requires='>=3',
    classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        ],
)
