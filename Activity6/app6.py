import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("🎥 Real-Time Video Filters")
st.subheader("Choose a mode from the sidebar")

# Sidebar: Select processing mode
mode = st.sidebar.selectbox("🔧 Select Mode", ["Canny Edge Detection", "Face Detection", "Grayscale", "Blur"])
take_snapshot = st.sidebar.button("📸 Take Snapshot")

# Sidebar: Dynamic controls based on mode
if mode == "Canny Edge Detection":
    st.sidebar.markdown("### Canny Thresholds")
    low_thresh = st.sidebar.slider("Low Threshold", 0, 255, 50)
    high_thresh = st.sidebar.slider("High Threshold", 0, 255, 150)

elif mode == "Face Detection":
    st.sidebar.markdown("### Detection Settings")
    scale_factor = st.sidebar.slider("Scale Factor", 1.1, 2.0, 1.1, 0.1)
    min_neighbors = st.sidebar.slider("Min Neighbors", 1, 10, 5)

elif mode == "Blur":
    st.sidebar.markdown("### Blur Settings")
    kernel_size = st.sidebar.slider("Kernel Size", 1, 21, 5, step=2)

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Placeholders for video and snapshot
video_placeholder = st.empty()
snap_placeholder = st.empty()

# Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    st.error("❌ Webcam not accessible.")
else:
    snapshot = None
    while True:
        ret, frame = cap.read()
        if not ret:
            st.warning("⚠️ Failed to capture frame.")
            break

        frame = cv2.flip(frame, 1)
        processed = frame.copy()

        # Apply selected processing
        if mode == "Canny Edge Detection":
            processed = cv2.Canny(processed, low_thresh, high_thresh)
            processed = cv2.cvtColor(processed, cv2.COLOR_GRAY2RGB)

        elif mode == "Face Detection":
            gray = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=scale_factor, minNeighbors=min_neighbors)
            for (x, y, w, h) in faces:
                cv2.rectangle(processed, (x, y), (x+w, y+h), (0, 255, 0), 2)
            processed = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)

        elif mode == "Grayscale":
            processed = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)
            processed = cv2.cvtColor(processed, cv2.COLOR_GRAY2RGB)

        elif mode == "Blur":
            processed = cv2.GaussianBlur(processed, (kernel_size, kernel_size), 0)
            processed = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)

        # Display processed frame
        video_placeholder.image(processed, channels="RGB", caption=f"{mode}")

        # Take snapshot
        if take_snapshot:
            snapshot = processed.copy()
            snap_placeholder.image(snapshot, caption="📸 Snapshot Taken!", use_column_width=True)
            take_snapshot = False
            break

    cap.release()
