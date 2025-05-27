from deepface import DeepFace
import random
import json

# Load captions
with open("captions.json", "r") as f:
    captions = json.load(f)

# Path to sample image
image_path = "images/sample1.jpg"

# Analyze the emotion
result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)
emotion = result[0]['dominant_emotion']
print(f"Detected Emotion: {emotion}")

# Pick a random caption for that emotion
caption = random.choice(captions.get(emotion, ["No words... just feels."]))
print(f"\n🧠 Meme Caption:\n\"{caption}\"")
