from setuptools import setup
from setuptools import find_packages


VERSION = '1.2.0'

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='comcloudbusinessmod',  # package name
    version=VERSION,  # package version
    description='平台型企业收益测算模型',  # package description
    long_description=LONG_DESCRIPTION,
    author='Near',  # 作者
    author_email='chenyang582@hotmail.com',  # 作者邮箱
    long_description_content_type='text/markdown',
    packages=find_packages(),
    zip_safe=False,
)
