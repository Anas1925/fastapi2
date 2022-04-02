import uvicorn 
from fastapi import FastAPI
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

    return ({'prediction': prediction} )
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
