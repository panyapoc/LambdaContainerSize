# Serverless CheckRide : Lambda Container Support DeepDive

## Lambda Zip vs Lambda Cont Image

Build and Deploy

``` bash
sam build -u
sam deploy --no-confirm-changeset

```

ML Container sample image
* https://base64-to-image.com/
* LambdaCont/ml_cont/test.png




Gen Random File

250 MB

``` bash
base64 /dev/urandom | head -c 250000000 > file.txt
```