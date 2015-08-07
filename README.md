# sqlalchemy-example
Demonstration of python ORM sqlalchemy
## Preparation
```BASH
pip install SQLAlchemy
```
## Play with sqlite
* Set engine to sqlite in db_session.py
* python db_table_creation.py
* python db_insert.py
* python db_query.py
* python db_update.py
* python db_delete.py

## Play with marialdb
* apt-get install libmysqlclient-dev
* pip install mysql-python
* Set engine to marialdb in db_session.py
* Create database in marialdb
```BASH
CREATE DATABASE IF NOT EXISTS sqlalchemy_test CHARACTER SET utf8 COLLATE utf8_general_ci;
```
* python db_table_creation.py
* python db_insert.py
* python db_query.py
* python db_update.py
* python db_delete.py
