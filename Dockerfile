FROM python:3.8.0-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

RUN apt-get upgrade -y
RUN apt-get update
RUN apt-get install libgl1 -y
RUN apt-get install libgl1-mesa-dev -y
RUN apt-get install libglib2.0-0 -y

COPY . /app
COPY ./yolov5/data /app/data
COPY ./yolov5/runs/detect /app/runs/detect
COPY ./yolov5/runs/detect/test_img.jpg /app/runs/detect/test_img.jpg
COPY /yolov5/runs/train/VehicleDetection/weights/best.pt /app/runs/train/VehicleDetection/weights/best.pt

EXPOSE 8501

CMD ["streamlit", "run", "yolov5/app.py"]
