# Automatically created by: scrapyd-deploy

import ast
import re
from setuptools import setup, find_packages
from os.path import dirname, join

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open(join(dirname(__file__), 'douban_movie/__init__.py'), 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode('utf-8')).group(1)))

with open(join(dirname(__file__), 'requirements.txt'), 'rb') as f:
    requires = []
    for line in f.readlines():
        line = line.strip()
        if not line.startswith('#'):
            requires.append(line)

setup(
    name='douban-movies',
    version=version,
    packages=find_packages(),
    zip_safe=False,
    entry_points={'scrapy': ['settings = douban_movie.settings']},
    description="Scrapy spider of Douban movies top250",
    keywords=("douban", "moives", "scrapy"),
    include_package_data=True,
    install_requires=requires,
    author="crazygit",
    author_email="craygit@foxmail.com",
    url="https://github.com/crazygit/scrapy_demo/tree/master/douban_movie"
)
