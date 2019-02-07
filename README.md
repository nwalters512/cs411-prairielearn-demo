# cs411-prairielearn-demo
Work on a demo of how PrairieLearn could be used for CS 411 assignments

## Question Structure

Questions are set up to require as little work as possible to write a new question.
A given question must specify two files in the `tests` directory:

* `setup.sql`: creates any necessary tables and populates them with data; can contain
  multiple queries
* `solution.sql`: contains a single query that defines the "solution" to this question.

When a question is graded, two databases are created and populated with `setup.py`.
The query in `solution.sql` is run on one of the databases, and the query submitted
by the student is run on the other. The resulting relations are compared, and the
student gets credit if the relation they return matches the solution exactly.

With those two files, it's possible to create a question that tests `SELECT` queries.
But what if you want to test insertion, updating, or deletion? Those queries won't
return relations; instead, you really want to diff the contents of a database after
the query completes. To do that, you can specify an optional third file `dump.sql`.
This contains a query that will be used to diff the contents of the databases after
the solution and student queries are run on their respective databases.

This allows question authors to largely avoid hardcoding answers. An author must simply
specify the input data and the query that should operate on it, and the student submission
can be automatically checked for correctness.

## Running locally

The Docker image with MySQL in it isn't published anywhere yet. To run this with a local
copy of PrairieLearn, you'll need to first build the Docker image:

```
docker build docker -t mysql-test
```
