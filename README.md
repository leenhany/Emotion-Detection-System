# Emotion Detection System 😄😢😠
This project is a web-based Emotion Detection System built using Streamlit and the DeepFace library. It allows users to upload an image or video, and it detects and displays the dominant emotion on faces using deep learning.

# 📌 Features
🔍 Detect emotions from uploaded images.

🎞️ Detect emotions in video frames.

📊 Uses DeepFace for robust facial emotion analysis.

🧠 Streamlit-powered interactive UI.
# 💻 Demo
Upload your image or video, and let the app analyze and display detected emotions like:
(Angry - Disgust - Fear - Neutral - Surprise - Happy - Fear)
# 🛠️ Tech Stack
<li/>Python 3
<li/>Streamlit – Web interface 
<li/>OpenCV – Video processing
<li/>DeepFace – Emotion recognition
<li/>PIL – Image processing


# 📂 How to Run
<pre lang="markdown"> ```bash
  $ git clone https://github.com/yourusername/Emotion-Detection-System.git 
  $ cd Emotion-Detection-System 
  $ streamlit run emotion_rec.py ``` </pre>
 <H3>If you don’t have a requirements: </H3> 
<pre lang="markdown"> ```bash
  $ pip install streamlit
  $ pip install pillow
  $ pip install opencv-python
  $ pip install numpy
  $ pip install deepface ``` </pre>
  
# 🧠 How It Works
For Image:
<li/>Upload an image (JPG, PNG, WEBP).
<li/>The app uses DeepFace to detect the emotion.
<li/>Displays the image and the predicted emotion.

For Video:
<li/>Upload a video (MP4, AVI, MOV).
<li/>The app reads every 100th frame, processes it, and overlays the detected emotion.
<li/>Displays the video frames in real time.

# 📷 Screenshots
<H3>For Image:</H3>
<img width="626" height="799" alt="Screenshot 2025-07-25 181534" src="https://github.com/user-attachments/assets/63bcbd72-0443-43b5-8e34-a1847f01f148" />
<H3>For Video:</H3>
<img width="894" height="801" alt="Screenshot 2025-07-25 182630" src="https://github.com/user-attachments/assets/8e646361-411c-4b32-95c9-7255589a9439" />

# 🤝 Contributing
Contributions are welcome! Open an issue or submit a pull request.


