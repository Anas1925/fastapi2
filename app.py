import uvicorn 
from fastapi import FastAPI
import pandas as pd
import numpy as np
import pickle


from pydantic import BaseModel
class BAM(BaseModel):
    
    month: int
    off_peak : int
    peak: int
    load: int
    noOfBulb:int
    noOfFans: int
    noOfAC : int


app = FastAPI()
model =pickle.load(open('bam_model','rb'))
# model = load_model('bam_model')
@app.get('/')
def index():
    return {'welcome': 'hello Stranger'}

@app.get('/welcome')
def get_name(name:str):
    
    return {"welcome :f{name}"}
@app.post('/predict')

def predict_bam(data:BAM):
    data =data.dict()
    print(data)
    month=data['month']
    off_peak =data['off_peak']
    peak=data['peak']
    load=data['load']
    noOfBulb=data['noOfBulb']
    noOfFans=data['noOfFans']
    noOfAC =data['noOfAC']
    
    prediction = model.predict([[month,off_peak , peak , load , noOfBulb , noOfFans , noOfAC]]).tolist()
# def predict_bam(month, off_peak, peak, load, noOfBulb, noOfFans, noOfAC):
#     data = pd.DataFrame([[month, off_peak, peak, load, noOfBulb, noOfFans, noOfAC]])
#     data.columns = [ "month","off_peak","peak","load","no_of_bulb","no_of_fans","no_of_ac"]
#     predictions = model.predict(data) 
#     return {'prediction': int(predictions)}
    
    return ({'prediction': prediction} )
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
