import json
import pandas as pd

def lambda_handler(event, context):

    interactions = pd.read_csv("interactions.csv")
    summary = interactions.groupby(['ITEM_ID','EVENT_TYPE'], as_index=False).size()

    print(summary)


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Done!",
        }),
    }
