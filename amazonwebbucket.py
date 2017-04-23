import boto3  
import json
import os, sys
import image
import re
from PIL import Image
# from pattern.en import singularize

# def isplural(pluralForm):
#      singularForm = singularize(pluralForm)
#      plural = True if pluralForm is not singularForm else False
#      return plural, singularForm

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

	jsonDatastring = json.dumps(results2['FaceDetails'], indent=2)
	jsonData = json.loads(jsonDatastring)

	if len(jsonData) == 0:
		results3 = rek.detect_labels(  
		    Image={
		        'Bytes': readfile
		    },
		    MaxLabels=15,
	    	MinConfidence=60
		)

		objectsDictionaryArray = []
		jsonData2 = json.dumps(results3, indent=2)
		newData2 = json.loads(jsonData2)
		objects = newData2["Labels"]

		for i in objects:
			nameOfObject = i.get("Name")
			objectsDictionaryArray.append(nameOfObject)
		jointString = ', '.join(objectsDictionaryArray[:len(objectsDictionaryArray)-1])
		lastElement = '{}'.format(objectsDictionaryArray[len(objectsDictionaryArray)-1])

		print("Your environment contains a {} and a {}".format(jointString, lastElement))

			
	else:
		jsonDataa = json.dumps(results2['FaceDetails'][0], indent=2)
		print(jsonDataa)
		newData = json.loads(jsonData)
		emotions = newData["Emotions"]

		HighageRange = newData["AgeRange"]["High"]
		LowageRange = newData["AgeRange"]["Low"]
		averageAge = (HighageRange+LowageRange)/2 #another variable to send to remi
		everyemotionArray = []

		for i in emotions:
			everyemotionArray.append(i)

		singleEmotion = everyemotionArray[0]
		conf = singleEmotion["Confidence"]

		n = conf*0.01
		print(singleEmotion["Type"])

		if singleEmotion["Type"] == "SAD" or singleEmotion["Type"] == "CONFUSED" or singleEmotion["Type"] == "ANGRY" or singleEmotion["Type"] == "DISGUSTED":
			# print singleEmotion["Type"]
			print((1/n)-1)
		elif singleEmotion["Type"] == "HAPPY" or  singleEmotion["Type"] == "SURPRISED" or singleEmotion["Type"] == "CALM":
			# print singleEmotion["Type"]
			print(n)
		else:
			print(0.5)

		print("Seems as though this persons age is {}".format(averageAge))

		results3 = rek.detect_labels(  
		    Image={
		        'Bytes': readfile
		    },
		    MaxLabels=15,
	    	MinConfidence=60
		)

		jsonData2 = json.dumps(results3, indent=2)
		newData2 = json.loads(jsonData2)
		objects = newData2["Labels"]
		# print(objects)

		for i in objects:
			print i

if __name__ == '__main__':

	methodname = sys.argv[1]
	imageRekogniser(methodname)



