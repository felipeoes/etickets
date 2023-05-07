# etickets

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/felipeoes/etickets.git
$ cd etickets
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ source env/bin/activate
```

*OR*

```bash
venv\Scripts\activate
````

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
