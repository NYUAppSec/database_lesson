# Database Lesson

## Overview

In this demonstration, we'll discuss taking an appropriately formatted CSV file and inserting it into a SQLite database using Python's Pandas library. The demonstration data contains information about the United States National Parks.

## Quickstart

Follow these simple commands to create the park.db database.
```bash
$ git clone git@github.com:NYUAppSec/database_lesson.git
$ cd database_lesson/
$ python -m venv db-lesson
$ source db-lesson/bin/activate
$ pip install -r requirements.txt
$ python csv2db.py park
```

Once the database is created, it will have a single table (park) that can be queried in your favorite SQLite-compatible database console. The table should be in First Normal Form (1NF).


### Querying
Try running a query to find our which parks were established before 1900.
```SQL
SELECT * FROM PARK WHERE founded < '1900-01-01'
```

### Questions 
Right now, the database lists the primary state or territory for each park, but some parks span across multiple states. How could we improve the database to better model the real world?

How many national parks are there in Utah? How many of these were founded before 1950?
