import streamlit as st
import pytesseract
import cv2
import os
from PIL import Image
from pytesseract import Output


def extract_text(image):
  image = cv2.imread(image)
  text = pytesseract.image_to_string(image, config=r'--oem 3 --psm 6 -l eng')
  data = pytesseract.image_to_data(image, output_type=Output.DICT)
  n_boxes = len(data['level'])
  for i in range(n_boxes):
    x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data[
        'height'][i]
    img = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
  return [Image.fromarray(img), text]


file = st.file_uploader(label='Select Image', type=['png', 'jpg', 'jpeg'])

if st.button('Extract Text'):
  with open('sample.png', "wb") as f:
    f.write(file.getvalue())
  st.write(extract_text('sample.png')[1])
  st.image(extract_text('sample.png')[0], width=640)
  os.remove('sample.png')

footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by Khan Faisal</p><br>
<a href='https://khanfaisal.netlify.app'>  Portfolio</a>
<a href="https://github.com/khanfaisal79960">  Github</a>
<a href="https://medium.com@khanfaisal79960">  Medium</a>
<a href="https://www.linkedin.com/in/khanfaisal79960">  Linkedin</a>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
