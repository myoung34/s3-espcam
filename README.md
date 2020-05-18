S3 ESPCAM32
===========

A simple docker container to connect to an espcam32 and upload the images to s3


## Building ##

```
$ docker build -t s3-espcam .
```

## Running ##

```
$ docker run -it \
  -e S3BUCKET="my-bucket" \
  -e ESPHOST="frontdoor_cam.some.local" \
  -e ESPPASSWORD="password" \
  -e AWS_ACCESS_KEY_ID="AKIA...." \
  -e AWS_SECRET_ACCESS_KEY="redact...." \
  myoung34/s3-espcam:latest
```
