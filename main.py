import pandas as pd
import streamlit as st

dt = {
  'car': ['BMW', 'Volvo', 'Ford'],
  'passings': [ 3, 7, 2 ]
}

df = pd.DataFrame(dt)

st.title('Uber pickups in NYC')
