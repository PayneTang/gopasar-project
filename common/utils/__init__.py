from django.conf import settings
from google.cloud import storage
from datetime import datetime
import random
import string


"""
Contains common utility for whole application
"""


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def blob_exists(filename):
    """
    Check if a file exists in google cloud storage before upload
    """
    client = storage.Client()
    bucket = client.get_bucket(settings.GS_BUCKET_NAME)
    blob = bucket.blob(filename)
    return blob.exists()


def retrieve_upload_relative_path(filename):
    return filename.replace(settings.MEDIA_ROOT, "")


def delete_blob(blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(settings.GS_BUCKET_NAME)
    blob = bucket.blob(blob_name)
    blob.delete()


def get_product_upload_destination(instance, filename):
    """
    Generate upload destination for product image
    """
    today = datetime.now()
    date_str = today.strftime("%Y/%m/%d")

    filename = '%s.jpg' % filename.split('.')[0]  # change to jpg
    # path = 'media/uploads/product/{}/'.format(date_str)
    path = 'uploads/product/{}/'.format(date_str)
    dest = path + filename
    if blob_exists(dest):
        dest = path + '%s_%s.jpg' % (filename.split('.')[0], randomString())
    return dest


def get_avatar_upload_destination(instance, filename):
    """
    Generate upload destination for user profile image
    """
    today = datetime.now()
    date_str = today.strftime("%Y/%m/%d")

    filename = '%s.jpg' % filename.split('.')[0]  # change to jpg
    path = 'uploads/avatar/{}/'.format(date_str)
    dest = path + filename
    if blob_exists(dest):
        dest = path + '%s_%s.jpg' % (filename.split('.')[0], randomString())
    return dest
