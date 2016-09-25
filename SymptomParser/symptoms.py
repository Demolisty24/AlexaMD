import requests
import pymysql.cursors
import string

POST_URL = "https://api.infermedica.com/v2/symptoms"
header = { "app_id" : "9cfcafae", "app_key" : "55b78a933718c8e68ba37f2f8d80b1a7"}
r = requests.get(POST_URL, headers=header)
json = r.json()

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='alexa_md',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        for key in json:
            exclude = set(string.punctuation)
            sql = "INSERT INTO `symptoms` (`symptom`, `id`) VALUES (%s, %s)"
            cursor.execute(sql, (''.join(ch for ch in key['name'].lower() if ch not in exclude), key['id']))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

finally:
    connection.close()