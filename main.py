import streamlit as st
import os
import shutil
from yolov5 import detect
from PIL import Image


def loadImage(image_file):
    print("Loading: ", image_file)
    img = Image.open(image_file)
    img.save(os.path.join("data", image_file.name))
    return img


def detectObject(current_dir):
    import time
    st.subheader("Image Input")
    image = st.sidebar.file_uploader(
        'Upload Image', type=['jpg', 'png', 'jpeg'])
    conf = st.sidebar.slider('Confidence: ', 0.0, 1.0, 0.3)
    iou = st.sidebar.slider('Threshold: ', 0.0, 1.0, 0.45)

    if image is not None:
        file_details = {"file name": image.name,
                        "file type": image.type,
                        "file size": image.size}
        st.write(file_details)
        st.image(loadImage(image), width=640)
        filename = image.name
        image_file = os.path.join("data", filename)
    else:
        filename = "test_img.jpg"
        image_file = "data/"+filename
        image = Image.open(image_file)
        image_file = os.path.join(current_dir, image_file)
        st.image(image, width=700)

    weight_path = os.path.join(
        current_dir,
        "yolov5/runs/train/VehicleDetection/weights/best.pt")
    shutil.rmtree('yolov5/runs/detect/')
    t = time.time()
    detect.run(weights=weight_path,
               name="VehilceDetectionTest",
               source=image_file,
               conf_thres=float(conf),
               iou_thres=float(iou),
               device='cpu')
    time = time.time() - t
    image_file_output = "yolov5/runs/detect/VehilceDetectionTest/"+filename
    img = Image.open(image_file_output)
    st.subheader("Detection Result: ")
    st.image(img, width=700)
    st.write("Inference time: {} s".format(time))


def main():
    st.title('Vehicle Object Detection')
    st.write("""
        This vehicle object detection project takes in an image and outputs the image with bounding boxes created around the objects in the image, also classname or label with it's confidence score.
        """)
    current_dir = os.getcwd()
    detectObject(current_dir)


if __name__ == '__main__':
    main()
