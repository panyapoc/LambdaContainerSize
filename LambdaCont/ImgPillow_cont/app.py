import json
from PIL import Image

def lambda_handler(event, context):
    #read the image
    im = Image.open("sample-image.png")

    #image size
    size=(200,200)
    #resize image
    out = im.resize(size)
    #save resized image
    out.save('/tmp/resize-output.png')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "done img",
        }),
    }
