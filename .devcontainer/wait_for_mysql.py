import os
import time

import pymysql


deadline = time.time() + 90

while time.time() < deadline:
    try:
        connection = pymysql.connect(
            host=os.environ.get('MYSQL_HOST', 'mysql'),
            port=int(os.environ.get('MYSQL_PORT', '3306')),
            user=os.environ.get('MYSQL_USER', 'root'),
            password=os.environ.get('MYSQL_PASSWORD', 'student'),
            database=os.environ.get('MYSQL_DATABASE', 'vehicle_management_db'),
        )
        connection.close()
        print('MySQL is ready.')
        raise SystemExit(0)
    except pymysql.MySQLError:
        time.sleep(3)

raise SystemExit('MySQL did not become ready in time.')
