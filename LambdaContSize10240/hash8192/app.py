import json
import hashlib

BLOCKSIZE = 65536
sha1 = hashlib.sha1()

def lambda_handler(event, context):
    with open('file.txt', 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            sha1.update(buf)
            buf = afile.read(BLOCKSIZE)

    print("SHA1: {0}".format(sha1.hexdigest()))
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hash done",
        }),
    }
