# Intro

This is software was created by me in order to receive data from [WSJT-X](https://en.wikipedia.org/wiki/WSJT_(amateur_radio_software)) written in Python.
The main idea is to receive data from one or more WSJT-X instances and then place it to one source.
Here I use SQLite, but you can use any database you want. 

# How it works

In WSJT-X Settings -> Reporting you should setup UDP Server. 
[EW1MY](https://github.com/alex37529/mywsjt/blob/develop/doc/pic-01.jpg?raw=true)
Specify your UDP Server and port number.
Then in code setup
```
UDP_IP = "127.0.0.1"
UDP_PORT = 2237
```

# How to create a database

To create a database used already created models and alembic. Database server should be already installed.
Then setup connection in alembic.ini. For more information look in [this tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
```
sqlalchemy.url = sqlite:///wsjtx.db
```
Then just run first migration:

```
alembic upgrade head
```

If DB already created you should start WSJT-X and then 

```
python main.py
```
