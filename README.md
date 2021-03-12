# Data analysis
- Document here the project: delphes
- Description: Project Description
- Data Source:
- Type of analysis:

Please document the project the better you can.

# Stratup the project

The initial setup.

Create virtualenv and install the project:
```bash
  $ sudo apt-get install virtualenv python-pip python-dev
  $ deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
  $ make clean install test
```

Check for delphes in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/delphes`
- Then populate it:

```bash
  $ ##   e.g. if group is "{group}" and project_name is "delphes"
  $ git remote add origin git@gitlab.com:{group}/delphes.git
  $ git push -u origin master
  $ git push -u origin --tags
```

Functionnal test with a script:
```bash
  $ cd /tmp
  $ delphes-run
```
# Install
Go to `gitlab.com/{group}/delphes` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:
```bash
  $ sudo apt-get install virtualenv python-pip python-dev
  $ deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:
```bash
  $ git clone gitlab.com/{group}/delphes
  $ cd delphes
  $ pip install -r requirements.txt
  $ make clean install test                # install and test
```
Functionnal test with a script:
```bash
  $ cd /tmp
  $ delphes-run
``` 

# Continus integration
## Github 
Every push of `master` branch will execute `.github/workflows/pythonpackages.yml` docker jobs.
## Gitlab
Every push of `master` branch will execute `.gitlab-ci.yml` docker jobs.

# Screenshots from the Website

<img width="1287" alt="Screenshot 2020-10-07 at 11 22 59" src="https://user-images.githubusercontent.com/68235075/110930419-610be780-8329-11eb-8090-e93c5ccac9b0.png">
<img width="1300" alt="Screenshot 2020-10-07 at 11 24 02" src="https://user-images.githubusercontent.com/68235075/110930441-65d09b80-8329-11eb-94c3-e92b267a28a0.png">
<img width="1255" alt="Screenshot 2020-10-07 at 11 25 32" src="https://user-images.githubusercontent.com/68235075/110930458-6c5f1300-8329-11eb-990c-ce14294d48b7.png">
