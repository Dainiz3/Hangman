# Flask-login with hangman game.

A simple flask-login combined with a hangman game using a database. You just need to register, then login. After logging in, the website will show no navigation with Home and Logout buttons. Then you'll see a Notes space to leave a tip for yourself in the future. You will also find user information (a simple dashboard) that shows your game score information.

## Installation

Clone project

```sh
$ git clone https://github.com/tpapic/flask-login.git
```

or download zip

If you don't have virtualenv installed

```sh
$ pip install --upgrade pip
$ pip install virtualenv
```

Once you have virtualenv installed, just fire up a shell and create your own environment.

```sh
$ cd Hangman
$ virtualenv -p python3 .venv
New python executable in .venv/Scripts/python
Installing setuptools, pip............done.
```

When you want to work on a project just activate your working environment

```sh
$ source .venv/Scripts/activate
```

After that you can make own env with packages

```sh
$ pip install -r requirements.txt
```

and etc...

Run server

```sh
python main.py
```

Then go to http://127.0.0.1:5000

When you want back to real world:

Press **Ctrl+c** to stop server

And

```sh
$ deactivate
```
