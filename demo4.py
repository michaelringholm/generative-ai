import tensorflow as tf   # For use with TensorFlow    v1.x
from typing import Tuple     # type hints        v3.5+
import numpy as np         # Python NumPy       v1.19.3
#LLAMA Call starts here
import requests   # To make http calls to send search queries to the Meta LLAMA Server(as needed )

def call_lamma(prompt:str):
    response =requests.get('https://llama.metamind.io/api/v1.6/topics', headers={},params={"search":prompt,"stop":10})
    data=response.json()['choices'][:10]

if __name__ == '__main__':
    print("Python test LLAMA")
    call_lamma("What is TensorFlow")