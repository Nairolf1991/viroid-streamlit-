# imports
from datetime import datetime
import pytz
import pandas as pd
import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras import models
import numpy as np
from tensorflow.keras.models import Sequential,load_model,Model

app = FastAPI()

def onehote(sequence):
    '''Takes in entry a DNA sequence,
    Returns a One-Hot-Encoded matrix'''
    mapping = {"A": 0, "C": 1, "G": 2, "T": 3,"-":4}
    seq2 = [mapping[i] for i in sequence]
    matrix=np.array([[1,0,0,0],
           [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1],
            [0,0,0,0]])
    return matrix[seq2]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

### Fonction - FONCTION + afficher un score (confidence level aXXX)
@app.get("/viroid")
def is_viroid(seq):
    while len(seq)<499:
        seq+="-"
    seq_encoded = np.array(onehote(seq))
    model=load_model("../ohe_for_flow")
    result = model.predict(seq_encoded.reshape(1,499,4))
    return str(result[0][0])
