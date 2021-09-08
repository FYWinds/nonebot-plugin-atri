#!/usr/bin/python3
# coding: utf-8
from setuptools import setup


def get_dis():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


def main():
    dis = get_dis()
    setup(
        name="nonebot-plugin-atri",
        version="0.0.2",
        url="https://github.com/FYWinds/nonebot-plugin-atri",
        keywords=["nonebot"],
        description="A ATRI Voice plugin for nonebot2",
        long_description_content_type="text/markdown",
        long_description=dis,
        author="FYWinds",
        author_email="i@windis.cn",
        python_requires=">=3.8",
        install_requires=[""],
        license='AGPLv3',
        classifiers=[
            "Operating System :: OS Independent",
            "License :: OSI Approved :: GNU AFFERO GENERAL PUBLIC LICENSE v3 (AGPLv3)",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: Implementation :: CPython"
        ],
        include_package_data=True
    )


if __name__ == "__main__":
    main()
