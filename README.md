# Wikimedia NSFW Classifier Reports

This repository contains the micro-tasks submitted by applicants for Outreachy Round 21.
For detailed description about the project and micro-tasks, click [here](https://phabricator.wikimedia.org/T264045).

Applicants are adviced to use Jupyter Notebooks for the reports. Since the project will be developed using python, applicants are advised to use Python in the notebooks!

Survey Reports should be well documented.

## How to add your survey reports

### Setup

1. Clone the repository
    ```shell
    git clone https://github.com/abbasidaniyal/Wikimedia-NSFW-Classifier-Reports.git 
    cd Wikimedia-NSFW-Classifier-Reports
    ```

2. Create a Virtual Environment and activate it
    Virtual environment isolates the entire project. The packages used by different projects will be different and few packages used in a project might not be compatible with another one. So, using a virtual environment sets up packages individually for each project.
    ```shell
    python3 -m venv env
    source env/bin/activate
    ```

3. Create a directory in the `reports` directory with you name.
    ```shell
    cd reports
    mkdir <NAME>
    cd <NAME>
    ```

4. Use this directory to upload all your work. This can contain Jupyter Notebooks and dependant files, if any.

### Contributing
1. Create a seperate branch and switch to it.
    ```shell
    git branch <BRANCH-NAME>
    git switch <BRANCH-NAME>
    ```

2. Add the files you modified/added and commit the changes.
    ```shell
    git add file1 file2 
    git commit -m "MESSAGE"
    ```

3. Get a local fork of this repository in your username-space [Link](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/working-with-forks). 
4. Push to your fork and create a pull request. [Link](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests).


## Code of Conduct
[Wikimedia Code of Conduct](https://meta.wikimedia.org/wiki/Wikimedia_community_code_of_conduct)


