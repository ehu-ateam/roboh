# Roboh

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
asanchez asanchez-host = (root) NOPASSWD: /usr/bin/python


```

Create a script called python-sudo.sh, containing (with your correct full python path):
```sh
#!/bin/bash
sudo /usr/bin/python "$@"
```

Be sure to make the script executable:
```sh
chmod +x python-sudo.sh
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
rpi host and user ->
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
On your remote server (RPi) `mkdir /home/{user}/Robohend` before continue.
Pycharm:
```sh
Settings/Preferences ->
Find... ->
Deployment ->
Mappings ->
Local path: /home/{USER}/roboh/Robohend, Deployment path on server: /home/ateam/Robohend ->
Apply ->
OK
```

### PyCharm Edit project configurations...
Pycharm:
```sh
script: /Users/{USER}/roboh/Robohend
interpreter: Remote Python 2.7.9 (sftp://ateam@{RPI-HOST}:22/home/ateam/python-sudo.sh)
working directory: /home/ateam/Robohend
```
