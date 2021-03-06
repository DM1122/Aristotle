[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)
![GitHub repo size](https://img.shields.io/github/repo-size/DM1122/Aristotle)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/DM1122/Aristotle)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/DM1122/Aristotle)


# Aristotle Digital
<img src="art/png/logo.png" height="256">
A next-generation online learning tool. Built for students, by students.

Developed by *Galaxy Heart Studios* :milky_way:

## Vision
In an era of social distancing, effective online learning is of paramount importance for the success of the next generation of students, and the continuity of humanity's ventures in every field of study. Aristotle Digital's mission is to provide students and educators alike a set of tools to facilitate and enrich the online learning experience. Join us as we build Humanity's smartest online learning tool. :book: :brain:

## High-Level V1.0 Objectives
* Intelligent video curation according to user learning style
* Augmented video player
* Aristotle Digital website

## Infinity and Beyond
* Engagement tools for educators with online content
* App for tracking student-level progress
* Automagic generation of curriculum
* Assessment generation
* Computer-generated learning content

## Pre-Flight Checklist
### Recommended Software
* [VSCode](https://code.visualstudio.com/)
* [Github Desktop](https://desktop.github.com/)

### Required Libraries
* [Python](https://www.python.org/) (3.7.6 x64)
* [git](https://git-scm.com/)
* [pip](https://pypi.org/project/pip/)
* [pipenv](https://pypi.org/project/pipenv/)

pipenv will take care of the rest.

## Getting Started
1. Download repo through github desktop
1. Install all packages specified in Pipfile using `pipenv install`
1. Profit

## Committing to Repository
This repo is configured to use pre-commit hooks. The pre-commit pipeline is configured as follows:
<p align="center"><img src="https://miro.medium.com/max/1400/1*zEyQac8rhvayY-2p5DeUHg.png"></p>

A successful commit therefore requires satisfying the syntactic rules put forth by isort, black, and flake8.

isort automatically orders import statements, while black automatically formats code according to PEP8. flake8 does not provide automatic correction, and must be dealt with manually. It is highly reccomended to install the flake8 linter for the code editor of your choice.

## Security
This repo makes use of decouple to manage API keys and other sensitive information.

## Upgrading Project's Python Version
1. Install new [python](https://www.python.org/) version
1. Remove virtualenv with `pipenv --rm`
   - In case of error, navigate to virtualenv directory and delete manually
1. Set new `python_version` in Pipfile and `language_version` in .pre-commit-config.yaml
1. Recreate virtualenv with `pipenv install`
1. Ensure VSCode python path is set to the virtualenv python install
1. Uninstall old python version if desired

## Shell Commands Reference

### Starting the Development Server
Open a terminal within the `arsite` folder, and run:
```
manage.py runserver
```
Click the link to visit the site.


### Using pre-commit
Runs on every git commit. Will not push code unless hooks pass.

#### Check all files
```
pre-commit run --all-files
```

#### Update hooks
```
pre-commit autoupdate
```

### Using pipenv
Automatically creates and manages a virtualenv for the project along will any required packages and dependencies. You no longer need to use pip and virtualenv separately. They work together.

#### Install new package into project
```
pipenv install [PACKAGE]
```

#### Install packages in production environment
```
pipenv install --ignore-pipfile
```

## The 5 Rules of A Great Git Commit Message
<img src="https://imgs.xkcd.com/comics/git_commit.png" width="256" align="center">

1. Write in the imperative
1. Capitalize first letter in the subject line 
1. Describe what was done and why, but not how
1. Limit subject line to 50 characters
1. End without a period

More [info](https://www.theserverside.com/video/Follow-these-git-commit-message-guidelines).

## Collaborative Code Best Practices
1. Ensure your Git client is configured with the correct email address and linked to your GitHub user.
1. Ensure no one works on the same file at the same time.
1. Git pull before beginning any new work.
1. Git push only when you're certain the code runs clean.
1. DO NOT put senstive keys or information in the source code. Use `.env` file along with decouple.
