# Naik - Nate like service
Naik mimics the Nate backend service, completes the ecommerce checkout flow on behalf of user.
## Technology and Tools
- Python
- Selenium - Browser Automation Framework
- Poetry - Python Dependency and Release Management
- Behave - Behavior Driven Development (BDD) Framework
## Environment Setup
- Install poetry from its [website] https://python-poetry.org/docs/#installation
- Add tab completion script for [shell](https://python-poetry.org/docs/#enable-tab-completion-for-bash-fish-or-zsh) if you want to
- Run `poetry install` in the root of project
## Poetry
### Add new package
-  Add package in poetry using `poetry add <package_name>`
## Behave
### Configuration file
- Add or update default configuration settings in `behave.ini` file
- Read the default configuration setting using `behave -v --dry-run`
- Configuration [options](https://behave.readthedocs.io/en/stable/behave.html#configuration-files)


## Run Project
- Entry poetry shell `poetry shell`
- Run project `behave -D url=<product_page_url>`



