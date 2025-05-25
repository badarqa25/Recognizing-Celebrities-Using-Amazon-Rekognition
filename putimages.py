import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image1.jpg','Beyonce'),
      ('image2.jpg','Bill Gates'),
      ('image3.jpg','Brad Pitt'),
      ('image4.jpg','Dwayane Johnson'),
      ('image5.jpg','Elon Musk'),
      ('image6.jpg','Jennifer Lopez'),
      ('image7.jpg','Jhonny Depp'),
      ('image8.jpg','Kamala Harris'),
      ('image9.jpg','Angelina Jolie')

      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('celebrityuploadsbybadarqa','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})