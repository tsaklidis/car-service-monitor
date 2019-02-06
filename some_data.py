import os

os.system("echo '[info] Lazy data dump started...'")
os.system("python manage.py create_owners 7")
os.system("python manage.py create_cars 3")
