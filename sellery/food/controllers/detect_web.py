import io
from datetime import datetime
from PIL import Image
from google.cloud import vision
from collections import Counter
import base64
import re

def detect_web(base64_image):
    """Detects web annotations given an image."""
    a = datetime.now()
    
    img_str = re.sub("^.*?;base64,", "", base64_image)
    im = Image.open(io.BytesIO(base64.b64decode(img_str)))
    resized_im = im.resize((512,512), Image.ANTIALIAS)

    img_byte_arr = io.BytesIO()
    resized_im.save(img_byte_arr, format=im.format)
    content = img_byte_arr.getvalue()
    image = vision.Image(content=content)

    threshold_score = 0.5
    threshold_labels = []
    tags = []

    # Performs label detection on the image file
    client = vision.ImageAnnotatorClient()
    response = client.label_detection(image=image)
    labels = response.label_annotations
    
    for label in labels:
        if label.score >= threshold_score and len(tags) < 3:
            tags.append(label.description)

    response = client.web_detection(image=image)
    annotations = response.web_detection

    if len(annotations.best_guess_labels[0].label) == 0:
        best_guess_label = annotations.web_entities[0].description
    else:
        best_guess_label = annotations.best_guess_labels[0].label

    # For all labels with score above threshold 
    tmp = ""      
    for entity in annotations.web_entities:
        if entity.score >= threshold_score:
            tmp += entity.description + " "
    tmp = tmp.split()
    threshold_labels = Counter(tmp).most_common(1)[0][0]

    if len(threshold_labels) == 0:
        threshold_labels = best_guess_label
    return threshold_labels, tags[:3]