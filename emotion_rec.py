import cv2
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import tempfile
from deepface import DeepFace
import os

## GUI Setup
st.title("Emotion Recognition App")
st.write("Upload an image/video to recognize emotions.")

def analyize_emotion(img_vid):
    try:
        #this analysis on my img/video 
        analysis=DeepFace.analyze(img_vid, actions=['emotion'], enforce_detection=False)
        return analysis[0]['emotion']
    except ValueError as e:
        st.error(f"error: {e}")
        return None

option=st.selectbox("Select Input Type",("Image","Video"))
##main function
if option=='Image':
    uploded_file=st.file_uploader("upload your iamge",type=['jpg','jpeg','png','webp'])
    if uploded_file is not None:
        img=Image.open(uploded_file)
        img_arr=np.array(img)
        st.image(img_arr,caption='Uploaded image')
        emotion_scores=analyize_emotion(img_arr)
        #emotion_scores--> {'angre'=0.1,'sad':0,6.....}
        if emotion_scores:
            detected_emotion=max(emotion_scores,key=emotion_scores.get)
            st.write(f"Detected Emotion: {detected_emotion}")
        else:
            st.write("No emotion detected or an error occurred.")

if option=='Video':  
    uploded_file=st.file_uploader("upload your video",type=['mp4','avi','mov'])      
    if uploded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tfile:
            # Save the uploaded file to a temporary file
            tfile.write(uploded_file.read())
            video_path=tfile.name
        cap=cv2.VideoCapture(video_path)
        stframe=st.empty()


        frame_count=0
        freme_rate=100
        while cap.isOpened():
            ret,frame=cap.read()
            if not ret:
                break
            frame_count+=1
            if frame_count % freme_rate == 0:
                frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                emotion_scores=analyize_emotion(frame_rgb)
                if emotion_scores:
                    detected_emotion=max(emotion_scores,key=emotion_scores.get)
                    cv2.putText(frame,detected_emotion,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                else:
                    detected_emotion="No emotion detected"
                    cv2.putText(frame,"No emotion detected",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                stframe.image(frame,channels='BGR', caption=f"Frame {frame_count} - {detected_emotion}", use_container_width =True)

        cap.release()
        st.write("Video processing complete.")

