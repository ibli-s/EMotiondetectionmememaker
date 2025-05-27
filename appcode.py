from deepface import DeepFace
import random
import json
with open("captions.json", "r") as f:
    captions = json.load(f)
image_path = "images/sample1.jpg"
result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)
emotion = result[0]['dominant_emotion']
print(f"Detected Emotion: {emotion}")
caption = random.choice(captions.get(emotion, ["No words... just feels."]))
print(f"\n🧠 Meme Caption:\n\"{caption}\"")
