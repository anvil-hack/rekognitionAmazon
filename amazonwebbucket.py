import line to: from /usr/local/lib/python2.7/dist-packages/watson_developer_cloud
import VisualRecognitionV3 as VisualRecognition
import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='{6ca7f05707251912ffb02b7f89f974eb66a004fd}')

print(json.dumps(visual_recognition.classify(images_url=https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg), indent=2))




