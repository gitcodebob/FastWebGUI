from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="fastwebgui",
    version="0.0.0",
    description="Create appealing cross-platform desktop applications using HTML and Flask/Django/FastAPI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gitcodebob/FastWebGUI",
    author="Bob Reijnders",
    author_email="info@bobreijnders.nl",
    license="MIT",
    packages=find_packages(),
    # zip_safe=False,
    python_requires=">=3.10",
    extras_require={"dev": ["twine>=4.0.2", "build>=1.0.3"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
