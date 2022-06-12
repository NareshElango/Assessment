# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 21:24:13 2022

@author: NARESH
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as gr
from PIL import Image
img=Image.open(r"C:\Users\INTEL\anaconda3\download.jpg")
st.image(img,width=500)
st.title("Dungeons & Dragons")
st.subheader("plz input the number of coins that you have (in the appropriate box)")
copper=0.01
silver=0.1
electrium=0.5
gold=1
platinum=10
placeholder_copper=st.empty()
placeholder_silver=st.empty()
placeholder_electrium=st.empty()
placeholder_gold=st.empty()
placeholder_platinum=st.empty()
numcopper=placeholder_copper.number_input("Enter the number of copper that you have:",min_value=0)
numsilver=placeholder_silver.number_input("Enter the number of silver that you have:",min_value=0)
numelectrium=placeholder_electrium.number_input("Enter the number of electrium that you have:",min_value=0)
numgold=placeholder_gold.number_input("Enter the number of gold that you have:",min_value=0)
numplatinum=placeholder_platinum.number_input("Enter the number of platinum that you have:",min_value=0)
total=(numcopper*copper)+(numsilver*silver)+(numelectrium*electrium)+(numgold*gold)+(numplatinum*platinum)
total=round(total)
st.write("the total number of currency that you have:")
st.write(total)
coins=[
       {"values":copper,"count":numcopper},
       {"values":silver,"count":numsilver},
       {"values":electrium,"count":numelectrium},
       {"values":gold,"count":numgold},
       {"values":platinum,"count":numplatinum}
      ]
df=pd.DataFrame(coins)
st.write(df)
data=df
st.write("BAR CHART")
st.bar_chart(df)
st.write("LINE CHART")
st.line_chart(df)
st.write("AREA CHART")
st.area_chart(df)

