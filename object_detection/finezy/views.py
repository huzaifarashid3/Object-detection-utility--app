from django.shortcuts import render
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Create your views here.
def index(request):
    return render(request, 'finezy/index.html', {'message': 'hello mom'})


# Define the detect function
def detect(request):
    return render(request, 'finezy/detect.html')


def results(request):
    if request.method == 'POST':
        image_file = request.FILES['image_data']
        # predicted_class = process(image_file)
        predicted_class = "hi" 
        return render(request, 'finezy/results.html', {'image_data':image_file, 'predicted_class':predicted_class})
    return render(request, 'finezy/detect.html')


# Load the pre-trained model
# model = load_model('object_detection_model.h5')
def process(image_file):
    # Get the image file from the request
    image = Image.open(image_file)
    # Convert the image to a numpy array
    image_array = np.array(image)
    # Reshape the image array to match the input shape of the model
    image_array = image_array.reshape(-1, 224, 224, 3)
    # Normalize the pixel values to be between 0 and 1
    image_array = image_array / 255.0
    # Make a prediction using the model
    prediction = model.predict(image_array)
    # Get the class label with the highest probability
    predicted_class = np.argmax(prediction)
    # Return the predicted class label as a response
    return predicted_class 


def history(request):
    # show past images in a grid
    pass