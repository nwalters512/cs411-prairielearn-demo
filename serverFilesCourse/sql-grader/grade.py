import json
import mysql.connector
import sqlparse

# Creates a new database with the given name, populates it with data from the
# "setup.sql" file, and sets that database as the current database. Returns a
# cursor for use
def create_and_use_database(cnx, name):


if __name__ == "__main__":
  cnx = mysql.connector.connect(user='root', password="password")
  cursor = cnx.cursor()

  # Default database setup
  cursor.execute("CREATE DATABASE solution DEFAULT CHARACTER SET 'utf8'")
  cursor.execute("USE solution")
  with open('/grade/tests/setup.sql') as setup_queries_file:
    setup_queries_raw = setup_queries_file.read()
  setup_queries = sqlparse.split(setup_queries_raw)
  for query in setup_queries:
    cursor.execute(query)

  # Generate solution rows based on the solution query
  with open('/grade/tests/solution.sql') as solution_file:
    solution_query = solution_file.read()
  print(solution_query)
  cursor.execute(solution_query)
  for solution_row in cursor:
    print(solution_row)

  # Create a new table for students so that they're working with a completely separate data set
  with open('/grade/student/query.sql') as student_file:
    student_query = student_file.read()
  grading_result = {}
  grading_result['score'] = 0.0
  grading_result['succeeded'] = False
  grading_result['output'] = output

  with open('results.json', mode='w') as out:
    json.dump(grading_result, out)
