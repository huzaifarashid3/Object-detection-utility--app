import streamlit as st
import os, os.path
from PIL import Image
imgs = []
path = 'images' 
for f in os.listdir(path):
    imgs.append(Image.open(os.path.join(path,f)))

for img in imgs:
    st.image( img, caption=f"Processed image", use_column_width=True,)
