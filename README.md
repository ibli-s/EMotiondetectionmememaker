# EMotiondetectionmememaker
Code for a tiny app that generates a caption like “When you realize it's Monday 😐
A mini Python app that detects emotions from an image using DeepFace and generates funny meme captions based on the detected emotion.

 Features

- Uses DeepFace to analyze the dominant emotion in a face image.
- Displays a corresponding meme caption that matches the detected emotion.
- Works with sample images (no webcam needed).
- Easy to extend with your own captions and images.

 How It Works

1. Load a face image.
2. Detect the dominant emotion using DeepFace.
3. Match the emotion with a funny caption from a JSON file.
4. Display the caption and save the meme text output.

 Requirements

- Python 3.x
- DeepFace (`pip install deepface`)
- OpenCV (`pip install opencv-python`)

 Usage

1. Clone or download this repo.
2. Install required packages:
 copy and paste in cmd
   pip install deepface opencv-python

