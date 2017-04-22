# import boto3

# BUCKET = "amazon-rekognition"

# def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="us-west-2"):
# 	rekognition = boto3.client("rekognition", region)
# 	response = rekognition.detect_labels(
# 		Image={
# 			"S3Object": {
# 				"Bucket": bucket,
# 				"Name": key,
# 			}
# 		},
# 		MaxLabels=max_labels,
# 		MinConfidence=min_confidence,
# 	)
# 	return response['Labels']


# for label in detect_labels(BUCKET, KEY):
# 	print "{Name} - {Confidence}%".format(**label)


import boto3  
import json
import os, sys
import image
from PIL import Image

f = open("elephant-in-the-room.jpg")
rek = boto3.client('rekognition') # Setup the Rekognition Client  

print "Getting Image"  
readfile = f.read()# Read the image

print "Image retrieved"  
print "Sending to Rekognition"

# Detect the items in the image
results = rek.detect_labels(  
    Image={
        'Bytes': readfile
    }
)

print "Rekognition done"

# Print the result
print json.dumps(  
    results['Labels'],
    indent=2
)

# Print a message for each item
for label in results["Labels"]:  
    print "I am {}% confident of of the image having a {} in it".format(
        int(label['Confidence']),
        label['Name'],
    )
