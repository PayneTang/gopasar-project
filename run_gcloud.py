from google.cloud import storage


def list_blobs(bucket_name):
    storage_client = storage.Client()

    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(blob.public_url)
        # print("Blob {} is publicly accessible at {}".format(
        #     blob.name, blob.public_url))


def blob_exists(bucket_name, filename):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(filename)
    return blob.exists()


# If you don't specify credentials when constructing the client, the
# client library will look for credentials in the environment.
storage_client = storage.Client()

# Make an authenticated API request
buckets = list(storage_client.list_buckets())

mybucket = [bucket.name for bucket in buckets if bucket.name ==
            "gopasar.appspot.com"][0]

# list_blobs(mybucket)
exist = blob_exists(
    mybucket, "media/uploads/product/2020/05/25/vertical_wallpaper.jpg")
print(exist)
