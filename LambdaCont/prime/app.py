import json

def printprime (lower,upper):
    # Python program to display all the prime numbers within an interval
    print("Prime numbers between", lower, "and", upper, "are:")
    for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

printprime (999000,1000000)

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "done",
        }),
    }
