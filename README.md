# Roboh

# Robohend

##Virtualenv interpreter

### Install virtualenv

```sh
$ sudo apt-get install python
# $ sudo apt-get install memcached
$ sudo apt-get install virtualenv
```

### Create a virtualenv

```sh
$ cd
$ mkdir ~/virtualenvs
$ virtualenv -p /usr/bin/python virtualenvs/veroboh
$ source ~/virtualenvs/veroboh/bin/activate
$ pip install -r ~/Robohend/roboh_deps.txt
$ deactivate
```

## RPI Python interpreter configuration

### Raspberry python interpreter as sudo

> On the raspberry pi [source](http://installfights.blogspot.com.es/2017/03/how-to-run-root-python-scripts-on.html)

To enable root privileges, you need create a new interpreter as follows:
```sh
sudo visudo -f /etc/sudoers.d/python
```

Add the following information:
```sh
<user> <host> = (root) NOPASSWD: <full path to python>
```

For example:
```sh
asanchez asanchez-host = (root) NOPASSWD: /home/{USER}/virtualenvs/veroboh/bin/python
```


Create a script called python-sudo.sh, containing (with your correct full python path) in order to use its interpreter from a remote client:
```sh
#!/bin/bash
sudo /home/{USER}/virtualenvs/veroboh/bin/python "$@"
```

Be sure to make the script executable:
```sh
sudo chmod +x python-sudo.sh
```


## PyCharm Professional Configuration
### PyCharm Professional Interpreter remote interpreter configuration

> See how to create a [remote interpreter](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html)

Pycharm:
```sh
Settings/Preferences ->
Find... ->
Project Interpreter ->
Engine(icon) ->
Add.. ->
rpi {HOST} and {USER} ->
password or ssh key* ->
SSH Interpreter: /home/ateam/python-sudo.sh
```
> configuration example: Remote Python 2.7.9 (sftp://ateam@{RPI-HOST}:22/home/ateam/python-sudo.sh)
> * sshkey: first you have to and your public key to /home/ateam/.ssh/authorized_keys

### Generating sh key
Create ssh key
```sh
ssh-keygen # follow the instructions
```

Copy to remote host-rpi (authorized_keys)
```sh
ssh-copy-id ateam@{RPI_HOST}
```

### PyCharm Edit project deployment...
On your remote server (RPi) `mkdir /home/{USER}/Robohend` before continue.

Pycharm:
```sh
Settings/Preferences ->
Find... ->
Deployment ->
Mappings ->
Local path: /home/{USER}/roboh/Robohend, Deployment path on server: /home/{USER}/Robohend ->
Apply ->
OK
```

### PyCharm Edit project configurations...
Pycharm:
```sh
script: /home/{USER}/virtualenvs/veroboh/bin/gunicorn
interpreter: Remote Python 2.7.9 (sftp://ateam@{RPI-HOST}:22/home/ateam/python-sudo.sh)
working directory: /home/ateam/Robohend
```

# Robohapp

## Install
> TODO: Ionic install documentation
```sh
npm install
```

## Run
```sh
ionic serve
```
