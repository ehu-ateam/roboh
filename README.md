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

## PyCharm Professional Interpreter remote interpreter configuration

> See how to create a [remote interpreter](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html)

```sh
Settings/Preferences --> Find... --> Project Interpreter --> Engine(icon) --> Add.. --> SSH Interpreter
```
> configuration example: Remote Python 2.7.9 (sftp://{USER}@{RPI-HOST}:22/home/{USER}/python-sudo.sh)

Edit project configurations...
```sh
script: /Users/{USER}/roboh/RPI-python
interpreter: Remote Python 2.7.9 (sftp://{USER}@{RPI-HOST}:22/home/{USER}/python-sudo.sh)
working directory: /home/ateam/roboh/RPI-python
```
