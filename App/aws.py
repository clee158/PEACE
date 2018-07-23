import os, sys, boto3

import App.constants as const

# Upload an image to AWS S3
def upload_images(path):
    bucket_name = const.BUCKET_NAME
    filename = path.split('/')[-1]

    session = boto3.Session(aws_access_key_id=os.environ[const.ACCESS_KEY],
                            aws_secret_access_key=os.environ[const.SECRET_KEY])

    s3 = session.client('s3')

    # check path & open file
    try:
        data = open(path, 'rb')
    except Exception as e:
        data.close()
        sys.exit('Encountered error opening file: {}. Error: {}'.format(path, e))

    # upload image to s3
    try:
        response = s3.put_object(Bucket=bucket_name, Key=filename, Body=data)
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            data.close()
            sys.exit('Encountered error uploading {} to bucket {}. Error: {}'.format(filename, bucket_name, response))
        else:
            data.close()

    except Exception as e:
        data.close()
        sys.exit('Encountered error uploading {} to bucket {}. Error: {}'.format(filename, bucket_name, e))

    return "https://s3.amazonaws.com/rating-imgs/" + filename
