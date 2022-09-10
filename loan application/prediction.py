from urllib import request
from flask import Flask, render_template
import numpy
import pickle

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

def ValuePredictotor(to_predict_list):
    to_predict=np.array(to_predict_list).reshape(1,9)
    loaded_model=pickle.load(open("LogisticRegressionModel.pkl","rb"))
    result=loaded_model,predict(to_predict)
    return result[0]

@ap.route('/result', method=['POST'])
app result():
if request.method ="POST":
    to_predict_list=request.form.to_dict()
    to_predict_list

if __name__=="__main__":
    app.run(debug=False)

