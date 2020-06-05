[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Aristotle
A digital Aristotle implementation.
<img src="art/png/logo.png" height="32">

## Pre-Flight Checklist
* Update [pip](https://pypi.org/project/pip/)
* Update [git](https://git-scm.com/)
* Update [Python](https://www.python.org/) (3.7.6 x64)
* Install [VSCode](https://code.visualstudio.com/)
* Install [Github Desktop](https://desktop.github.com/)
* Install [Django](https://www.djangoproject.com/) (3.0.6)

## Shell Commands Reference
### Install a package
```
pip install [package] 
```

### List all installed pip packages
```
pip list
```

### Check package version
```
pip show [package]
```
or
```
[package] --version
```

### Update pip package
```
pip install --upgrade [package]
```

### Uninstall pip package
```
pip uninstall [package]
```

### Uninstall all packages
```
pip freeze > requirements.txt && pip uninstall -r requirements.txt -y
```

## Using pipenv

###
Install all packages specified in Pipfile
```
pipenv install
```

###
Install new package and add to Pipfile
```
pipenv install [PACKAGE]
```

###
Install packages in production environment
```
pipenv install --ignore-pipfile
```

## Using pre-commit

###
Install hooks
```
pre-commit install
```

###
Format all files
```
pre-commit run --all-files
```


## The 5 Rules of A Great Git Commit Message
<p align="center">
  <img src="https://imgs.xkcd.com/comics/git_commit.png" width="256">
</p>

1. Write in the imperative
2. Capitalize first letter in the subject line 
3. Describe what was done and why, but not how
4. Limit subject line to 50 characters
5. End without a period

More [info](https://www.theserverside.com/video/Follow-these-git-commit-message-guidelines)

## Collaborative Code Best Practices

1. Ensure your Git client is configured with the correct email address and linked to your GitHub user.
2. Ensure no one works on the same file at the same time.
3. Git pull before beginning any new work.
4. Git push only when you're certain the code runs clean. Valgrind clean.

## Resources
* Python Package Index: https://pypi.org/
* Tensorflow Documentation: https://www.tensorflow.org/
