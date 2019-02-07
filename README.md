# cs411-prairielearn-demo
Work on a demo of how PrairieLearn could be used for CS 411 assignments

## Question Structure

Questions are set up to require as little work as possible to write a new question.
A given question must specify two files in the `tests` directory:

* `setup.sql`: creates any necessary tables and populates them with data; can contain
  multiple queries
* `solution.sql`: contains a single query that defines the "solution" to this question.
  The relation produced by the student query must match the solution exactly in order to
  receive credit.

This allows question authors to largely avoid hardcoding answers. An author must simply
specify the input data and the query that should operate on it, and the student submission
can be automatically checked for correctness.

## Running locally

The Docker image with MySQL in it isn't published anywhere yet. To run this with a local
copy of PrairieLearn, you'll need to first build the Docker image:

```
docker build docker -t mysql-test
```
