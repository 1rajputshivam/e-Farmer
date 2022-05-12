

from fileinput import filename
from unicodedata import name
from unittest import result
from flask import Flask, render_template, request
import numpy as np
import os
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
model=load_model('DenseNet121.h5')
print('model loaded')                  

def pred_crop(crop_leaf):
    test_image=load_img(crop_leaf,target_size=(256,256))
    print('got image for prediction')
    test_image=img_to_array(test_image)/255
    test_image=np.expand_dims(test_image,axis=0)
    result=model.predict(test_image).round(3)
    print('raw result= ',result)
    pred=np.argmax(result)

    if pred == 0:
        return "Apple Disease Black Root","prediction.html" # if index 0 burned leaf
    elif pred == 1:
        return "Apple Disease Rust","prediction.html" # # if index 1
    elif pred == 2:
        return "Apple Healthy ","prediction.html"  # if index 2  fresh leaf
    elif pred == 3:
        return "Cherry Disease","prediction.html" # if index 3
    elif pred == 4:
        return "Cherry Healthy","prediction.html" # # if index 1
    elif pred == 5:
        return "Maize Disease Blight","prediction.html"  # if index 2  fresh leaf
    elif pred == 6:
        return "Maize Disease Gray Spot","prediction.html"
    elif pred == 7:
        return "Maize Healthy","prediction.html" # # if index 1
    elif pred == 8:
        return "Peach Disease Bacerial","prediction.html"  # if index 2  fresh leaf
    elif pred == 9:
        return "Peach Healthy","prediction.html" # if index 3
    elif pred == 10:
        return "Potato Disease Early Blight","prediction.html" # # if index 1
    elif pred == 11:
        return "Potato Disease Late Blight","prediction.html"  # if index 2  fresh leaf
    elif pred == 12:
        return "Potato Healthy","prediction.html"  # if index 2  fresh leaf
    elif pred == 13:
        return "Tomato Disease Blight","prediction.html"  # if index 2  fresh leaf
    elif pred == 14:
        return "Tomato Disease Target Spot","prediction.html"  # if index 2  fresh leaf
    elif pred == 15:
        return "Tomato Disease Yellow Virus","prediction.html"  # if index 2  fresh leaf
    else:
        return "Tomato Healthy","prediction.html"  # if index 2  fresh leaf
    
        


app=Flask(__name__, template_folder='template')

@app.route("/",methods=['GET','POST'])
def index():
    return render_template('index.html')
    
@app.route("/prediction",methods=['GET','POST'])
def predict():
    if request.method=='POST':
        file=request.files['img']
        filename=file.filename
        print("input posted", filename)
        file_path=os.path.join('static/uploads',filename)
        file.save(file_path)
        print('predicting class')
        pred, output_page=pred_crop(crop_leaf=file_path)
        return render_template(output_page,pred_optput=pred, user_image=file_path)

############## Navigations
@app.route('/about',methods=['GET','POST'])  
def login():  
    return render_template("about.html");

@app.route('/home',methods=['GET','POST'])  
def home():  
    return render_template("index.html");

@app.route('/Contact',methods=['GET','POST'])  
def Contact():  
    return render_template("Contact.html");
@app.route('/logo',methods=['GET','POST'])  
def logo():  
    return render_template("index.html");

############## crops pages
@app.route('/wheat',methods=['GET','POST'])  
def Wheat():  
    return render_template("wheat.html");
@app.route('/Apple',methods=['GET','POST'])  
def Apple():  
    return render_template("Apple.html");
@app.route('/Cherry',methods=['GET','POST'])  
def Cherry():  
    return render_template("Cherry.html");
@app.route('/Maize',methods=['GET','POST'])  
def Maize():  
    return render_template("Maize.html");
@app.route('/Peach',methods=['GET','POST'])  
def Peach():  
    return render_template("Peach.html");
@app.route('/Potato',methods=['GET','POST'])  
def Potato():  
    return render_template("Potato.html");
@app.route('/Tomato',methods=['GET','POST'])  
def Tomato():  
    return render_template("Tomato.html");
@app.route('/thankyou',methods=['GET','POST'])  
def thankyou():  
    return render_template("https://formsubmit.co/1rajputshivam@gmail.com.html");



if __name__=="__main__":
    app.run(threaded=False)

    
    