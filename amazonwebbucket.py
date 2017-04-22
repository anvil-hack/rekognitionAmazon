

import boto3  
import json
import os, sys
import image
from PIL import Image



def imageRekogniser(imageurl):

	f = open("{}".format(imageurl))
	rek = boto3.client('rekognition') # Setup the Rekognition Client  
	readfile = f.read()# Read the image
	results2 = rek.detect_faces(  

	    Image={
	        'Bytes': readfile
	    },
	    Attributes=[
	    'ALL',
	]
	)

	jsonData = json.dumps(results2['FaceDetails'][0], indent=2)
	newData = json.loads(jsonData)
	emotions = newData["Emotions"]


	emotionArray = []

	for i in emotions:
		# eachemotion = json.dumps(i, indent=2)
		mood = i.get("Type")
		emotionArray.append(mood)

	currentEmotion = emotionArray[0]
	lowercaseString = currentEmotion.lower()

	print newData




if __name__ == '__main__':
	methodname = sys.argv[1]
	imageRekogniser(methodname)



