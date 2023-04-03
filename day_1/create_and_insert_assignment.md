# Create and Insert Assignment
This repo contains a file named `Titanic`. Your task is to load the data from the provided file(use `pandas`). 

Using the `psycopg2` and `pandas` library:

* Read in the `titanic.csv` file to a DataFrame object.
* Use `df.to_sql()` or create a `Base` class to insert the data into a new table named `titanic` in a PostGreSQL database.

Then, in Python, write the following queries to test:

* Count how many rows you have.
* How many people survived?
* What passenger class has the largest population?
