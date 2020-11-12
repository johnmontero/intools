InTools - Is a simple Infrastructure tool for task
===================================================


Installation
------------
```console
❯❯❯ mkdir -r $HOME/opt/intools
❯❯❯ git clone https://github.com/johnmontero/intools.git $HOME/opt/intools/src
❯❯❯ python3 -m venv $HOME/opt/intools/venv
❯❯❯ $HOME/opt/intools/venv/bin/python $HOME/opt/intools/src/setup.py install
❯❯❯ sudo ln -s $HOME/opt/intools/venv/bin/intools /usr/local/bin/intools
❯❯❯ intools --help

Usage: intools [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create-accesskey  Create Access Key for User.
  delete-accesskey  Delete Access Key for User.
  list-accesskeys   List Access Keys for User.
  version           Show version of InTools.
```

Upgrade
-------
```console
❯❯❯ export cwd=`pwd` && cd $HOME/opt/intools/src && git pull origin master && cd $cwd && unset cwd
❯❯❯ $HOME/opt/intools/venv/bin/python $HOME/opt/intools/src/setup.py install
```

List Access Keys
----------------
```console
❯❯❯ intools list-accesskeys --username juan.perez
InTools - Is a simple Infrastructure tool for task.

List access keys for Username: juan.perez

+----------------------+---------------------------+--------+
|     AccessKeyId      |        CreateDate         | Status |
+======================+===========================+========+
| AKIA5QWRRGNXISUDNQPT | 2020-11-05 16:43:23+00:00 | Active |
+----------------------+---------------------------+--------+
```

Delete Access Key
-----------------
```console
❯❯❯ intools delete-accesskey --username juan.perez --access-key-id=AKIA5QWRRGNXISUDNQPT
InTools - Is a simple Infrastructure tool for task.

Delete access key for Username: antonio.santin
Access key ID: AKIA5QWRRGNXISUDNQPT

Deletion the access key was successful
```

Create Access Key
-----------------
```console
❯❯❯ intools create-accesskey --username juan.perez --email=jmonteroc@gmail.com
InTools - Is a simple Infrastructure tool for task.

Create access key for Username: juan.perez
Send notification to email: jmonteroc@gmail.com

+----------------------+------------------------------------------+---------------------------+--------+
|     AccessKeyId      |             SecretAccessKey              |        CreateDate         | Status |
+======================+==========================================+===========================+========+
| AKIA7QWRRGBXC6NXH5NP | DISkZTt5qVnslJGJTVwhwML8WJksXJajHD5EUQIX | 2020-11-05 17:24:35+00:00 | Active |
+----------------------+------------------------------------------+---------------------------+--------+
```

Create Access Key with flag --force
-----------------------------------
```console
❯❯❯ intools create-accesskey --username juan.perez --email=jmonteroc@gmail.com --force
InTools - Is a simple Infrastructure tool for task.

Force deletion of access keys for Username: juan.perez
Deletion the access key id AKIA7QWRRGBXC6NXH5NP was successful

Create access key for Username: juan.perez
Send notification to email: jmonteroc@gmail.com

+----------------------+------------------------------------------+---------------------------+--------+
|     AccessKeyId      |             SecretAccessKey              |        CreateDate         | Status |
+======================+==========================================+===========================+========+
| AKIA7QWRRGBXC6NXH5TP | FISkZTt5qVnslJGJTVwhwML8WJksXJajHD5EUQIX | 2020-11-05 17:31:23+00:00 | Active |
+----------------------+------------------------------------------+---------------------------+--------+
```

Config file
-----------
```console
vim $HOME/.config/intools/config.yaml

---
smtp:
 host: localhost
 port: 25

email:
  email_from: InTools <team@intools.com>
```

Add/Delete libraries
--------------------
This is done in the requirements.txt file.

How to add commands
-------------------
To add commands you must follow the following steps:
* Create a file inside the "commands" folder
* Write the code following the definition of the library: https://click.palletsprojects.com/en/7.x/

Example code
------------

```console
import click

from intools.main import pass_context

@click.command()
@pass_context
def command(ctx, **kwargs):
    """Process task ... and exit."""
    print("Starting Process task...")
    ...
    ...
    ...
    print("Finishing Process task...")
```

