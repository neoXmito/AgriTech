import torch
import cv2
import numpy as np
from PIL import Image as PILImage  # Rename PIL Image to avoid conflict
import streamlit as st
import io

# Streamlit UI components
st.title('Tomato Disease Recognition')
st.write('Upload an image to detect disease in tomato plants.')

# File uploader widget
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the original image
    img = PILImage.open(uploaded_file)
    st.image(uploaded_file, caption='Original Image', use_column_width=True)

    # Load the YOLOv5 model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='Notebooks/disease_recognition/tomato/best.pt', force_reload=True)

    # Convert the image to NumPy array for manipulation
    img_np = np.array(img)

    # Run inference
    results = model(img)

    # Extract detection results (bounding boxes, class names, and confidence scores)
    detections = results.pandas().xyxy[0]  # Get bounding box coordinates and labels

    # Use a set to store unique disease names
    detected_diseases = set()

    # Iterate through detections and store unique disease names
    for index, row in detections.iterrows():
        disease_name = row['name']
        detected_diseases.add(disease_name)  # Add disease name to the set

    # Print detected disease names without repetition
    st.write("### Detected Diseases:")
    for disease in detected_diseases:
        st.write(disease)  # Display each disease name only once

    # Iterate through detections and draw bounding boxes
    for index, row in detections.iterrows():
        xmin, ymin, xmax, ymax = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        label = f"{row['name']} {row['confidence']:.2f}"
        color = (0, 255, 0)  # Green color for bounding box

        # Draw rectangle and label on the image
        cv2.rectangle(img_np, (xmin, ymin), (xmax, ymax), color, 2)
        cv2.putText(img_np, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Convert the image from BGR (OpenCV) to RGB (PIL Image format)
    img_with_boxes_rgb = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    # Convert the image to bytes for display in Streamlit
    img_byte_arr = io.BytesIO()
    PILImage.fromarray(img_with_boxes_rgb).save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Display the processed image with bounding boxes
    st.image(img_byte_arr, caption='Processed Image with Bounding Boxes', use_column_width=True)

    st.write("### Image has been processed")
