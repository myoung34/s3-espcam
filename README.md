S3 ESPCAM32
===========

A simple docker container to connect to an espcam32 (via [esphome](https://github.com/esphome/aioesphomeapi) )and upload the images to s3


## Building ##

```
$ docker build -t s3-espcam .
```

## Permissions ##

Unless you're running this in AWS with a tunnel to the camera, youll need to create an IAM user with these permissions:

```
resource "aws_iam_user" "s3-espcam" {
  name = "s3-espcam"
  path = "/"
}

resource "aws_iam_user_policy" "s3-espcam" {
  name = "s3-espcam"
  user = aws_iam_user.s3-espcam.name

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "s3:Put*"
      ],
      "Effect": "Allow",
      "Resource": [
        "arn:aws:s3:::my-bucket/*",
        "arn:aws:s3:::my-bucket"
      ]
    }
  ]
}
EOF
}
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
