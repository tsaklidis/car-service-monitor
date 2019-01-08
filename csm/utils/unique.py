import hashlib
import datetime


def unique_id(length=8):
    salt = hashlib.sha1(str(datetime.datetime.now())).hexdigest()[:5]
    return hashlib.sha1(salt).hexdigest()[:length]
