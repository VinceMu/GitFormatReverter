# GIT FORMAT REVERTER (WIP)
Find a list of files which have ONLY had their formatting changed between 2 different commits.

### Current Usage
usage: python app.py PATH_TO_COMPARE_FROM_REPO REPO_1_PATH REPO_2_PATH
PATH_TO_COMPARE_FROM_REPO: path to start the comparison relative to the repo root. 
REPO_1_PATH: path to 1st repo relative from where script is exectuted. 
REPO_2_PATH: path to 2nd repo relative from where script is executed.

### TODO
- incorporate usage of git so that command can ideally operate with the following params "PATH_TO_COMPARE_FROM_REPO" 
- refactor into classes and helper classes. 
