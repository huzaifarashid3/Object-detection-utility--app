
let classifier, img, result;
function preload() {
    classifier = ml5.imageClassifier('MobileNet');
    img = document.createElement('img');
    result = document.getElementById('result');
}
preload();
function gotResult(error, results) {
    if (error) {
        console.error(error);
    } else {
        console.log(results);
        result.textContent = `1. ${results[0].label}`;
    }
}
const video = document.getElementById('video');
const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
const captureButton = document.getElementById('captureButton');
const capturedImageContainer = document.getElementById('captured-image-container');

let stream;
let canvas = document.createElement('canvas');
let context = canvas.getContext('2d');

startButton.addEventListener('click', function () {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (mediaStream) {
            stream = mediaStream;
            video.srcObject = mediaStream;
        })
        .catch(function (err) {
            console.error('Error accessing webcam: ', err);
        });
});

stopButton.addEventListener('click', function () {
    if (stream) {
        const tracks = stream.getTracks();
        tracks.forEach(track => track.stop());
        video.srcObject = null;
    }
});

captureButton.addEventListener('click', function () {
    if (stream) {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
        const imageData = canvas.toDataURL('image/jpeg');

        displayCapturedImage(imageData);

        img.src = imageData;
        result.textContent = `loading...`;
        classifier.classify(img, gotResult);
    }
});

function displayCapturedImage(imageData) {
    const img = document.createElement('img');
    img.src = imageData;
    capturedImageContainer.appendChild(img);
}
