import cv2

class Predictor():
    
    cascade = 'haarcascade/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade)    
    
    #@staticmethod
    # def resize(image):
    #     width = int(1080)
    #     height = int(image.shape[0] * (width / image.shape[1]))
    #     dim = (width, height)
    #     image = cv2.resize(image, dim)
    #     return image

    # @staticmethod
    # def preprocess(image_bgr):
    #     image = image_bgr.copy()
    #     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #     image = cv2.GaussianBlur(image, (3,3), cv2.BORDER_DEFAULT)
    #     image = cv2.equalizeHist(image)
    #     return image
    
    @staticmethod
    def preprocess(vidio):
        while(vidio.capture.isOpened()):
            ret,frame = vidio.read()
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        return frame
    
    @staticmethod
    def draw(image_bgr, bouding_boxes):
        ret,frame = image_bgr.capture.isOpened()
        image = frame.copy()
        for (x,y,w,h) in bouding_boxes:
            cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
        return image
    
    @staticmethod
    def load_image(path):
        vidio = cv2.VidioCapture(path)
        return vidio

    @staticmethod
    def save_image(path, result):
        cv2.VideoWriter(path,result)

    @classmethod
    def predict(cls, vidio_bgr):
        vidio = vidio_bgr.copy()
        gray_image = cls.preprocess(vidio)
        bouding_boxes = cls.face_cascade.detectMultiScale(gray_image, 1.3, 5)
        result = cls.draw(vidio, bouding_boxes)
        return result

def process(source, target):
    image = Predictor.load_image(source)
    result = Predictor.predict(image)
    Predictor.save_image(target, result)

import os, shutil
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if(request.method == 'GET'):
        return render_template('index.html')
    elif(request.method == 'POST'):
        source = 'static/source.mp4'
        target = 'static/result.mp4'            
        image = request.files['image']
        image.save(source)
        process(source, target)
        return redirect(url_for('display'))

@app.route('/result', methods=['GET'])
def display():
    return render_template('display.html')

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
    shutil.rmtree('static')
