

import boto3  
import json
import os, sys
import image
from PIL import Image
import numpy as np

def replace_element(lst, new_element, indices):
	for i in indices:
		lst[i] = new_element
	return lst

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

	HighageRange = newData["AgeRange"]["High"]
	LowageRange = newData["AgeRange"]["Low"]
	averageAge = (HighageRange/LowageRange)/2 #another variable to send to remi


	everyemotionArray = []
	ageRangeArray =[]
	objectArray = []

	for i in emotions:
		everyemotionArray.append(i)

	# for i in ageRange:
	# 	print(i)

	singleEmotion = everyemotionArray[0]

	conf = singleEmotion["Confidence"]

	n = conf*0.01
	print(singleEmotion["Type"])

	if singleEmotion["Type"] == "SAD" or singleEmotion["Type"] == "CONFUSED" or singleEmotion["Type"] == "ANGRY" or singleEmotion["Type"] == "DISGUSTED":
		# print singleEmotion["Type"]
		print((1/n)-1)
	elif singleEmotion["Type"] == "HAPPY" or  singleEmotion["Type"] == "SURPRISED" or singleEmotion["Type"] == "CALM":
		# print singleEmotion["Type"]
		print n
	else:
		print 0.5







	# lowercaseString = currentEmotion.lower()

	# for i in ageRange:
	# 	# therange = json.dumps(i, indent=2)
	# 	# high = i.get("High")
	# 	print i

	# print ageRange

if __name__ == '__main__':

	methodname = sys.argv[1]
	imageRekogniser(methodname)



