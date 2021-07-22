# Serverless CheckRide : Lambda Container Support DeepDive

## Container Size - Cold Start

Build and Deploy

``` bash
sam build -u
sam deploy --no-confirm-changeset

```


Gen Random File

256MB - 268435456
512MB - 536870912
1024MB - 1073741824
2048MB - 2147483648
4096MB - 4294967296
8192MB - 8589934592

``` bash
base64 /dev/urandom | head -c xxxxxxx > file.txt
```

Check Size
``` bash
ls */file.txt -hl
```