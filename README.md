![screenshot](https://github.com/RGGH/mok/blob/main/screenshot.png)

```
❯ tree -L 3
.
├── app
│   ├── fetch_www.py
│   ├── __init__.py
│   └── __pycache__
│       ├── fetch_www.cpython-310.pyc
│       └── __init__.cpython-310.pyc
├── pytest.ini
└── tests
    ├── __pycache__
    │   ├── test_bcd.cpython-310-pytest-7.2.2.pyc
    │   └── test_bcd.cpython-310-pytest-7.4.3.pyc
    └── test_bcd.py

4 directories, 8 files```

---

if pytest is still unable to find the app module. To fix this issue, we can try a few different approaches:

Check Project Structure: Ensure that the app package is structured correctly within your project directory. It should have an __init__.py file to be recognized as a Python package.

PYTHONPATH: Set the PYTHONPATH environment variable to include the root directory of your project. This ensures that Python can find modules and packages located within your project directory.

Update pytest.ini: Update your pytest.ini file to include the root directory of your project in the python_paths option. This tells pytest where to look for modules and packages when running tests.





