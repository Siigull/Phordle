from google.cloud import vision
import os

client = vision.ImageAnnotatorClient()

os.environ['VISION_CREDENTIALS'] = 'top-chain-394711-21fa8ce1fe35.json'

def object_in_photo(photo, objects):
    response = client.annotate_image({
    'image': {'content': photo},
    'features': [{'type_': vision.Feature.Type.FACE_DETECTION}]
    })
    response = client.annotate_image( )
    print(response)