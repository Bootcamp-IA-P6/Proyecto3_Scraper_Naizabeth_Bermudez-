import pymysql

# Hemos subido el número a 2.2.1 para que Django 6.0 no proteste
pymysql.version_info = (2, 2, 1, 'final', 0)
pymysql.install_as_MySQLdb()