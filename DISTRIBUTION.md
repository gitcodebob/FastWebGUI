# Distribution cheat sheet

## Check if the package is installable
```console
pip install .[dev]
```
add `[dev]` to install the  `extras_require` packages, required to build a release, if you have defined them in your setup.py. Example:
```python
extras_require={"dev": ["twine>=4.0.2", "build>=1.0.3"]},
```

## Old way (binairy and wheel)
Create binairies
```console
python setup.py bdist
```
Create whl
```console
python setup.py bdist_wheel
```

## New way (binairy and wheel)
```console
python -m build
```

## Uploading
Using twine, check if everything is ok
```console
twine check dist/*
```
Then upload to PyPi test or production
```console
twine upload -r testpypi dist/*
twine upload dist/*
```