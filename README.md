*Project Author*
Espi Madrazo


*Project Goal*
Automation and testing of basic main user flows for the website "https://www.saucedemo.com" integrating Pytest and Selenium.


*Required dependencies*
- pip (included in Python if downloaded from python.org)
- pytest: pip install pytest
- pytest-html: pip install pytest-html
- selenium: pip install selenium
- webdriver manager: pip install webdriver-manager (for installation configuration changes, check utils/helpers.py)


*Instructions for tests execution*
Terminal commands:
- Show help on command line and config file options: pytest -h
- Run tests in a module: pytest test_mod.py
- Run tests in a directory: pytest tests/
- Run tests with more detailed output: pytest -v
- Run tests and generate an html report: pytest /tests -v --html=report.html

For further commands check the official documentation: "https://docs.pytest.org".


Note: Some Firefox extensions may interfere with the correct execution of these tests; if you encounter any problems related to this, consider disabling any extensions in your browser before executing again. A webdriver configuration that lunches a clean Firefox profile will be included later on in the project.