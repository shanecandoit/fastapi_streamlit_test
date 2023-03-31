
import streamlit as st
import json
import requests

st.title("Streamlit Demo :cat:")

option = st.selectbox(
    'what operation do you want to perform?',
    ('Add', 'Subtract', 'Multiply', 'Divide')
)

st.write('')
st.write('select the numbers you want to use')
x = st.number_input('x', 0, 100, 20)
y = st.number_input('y', 0, 100, 10)

inputs = {'operation': option, 'x': x, 'y': y}
print(f'inputs: {inputs}')

if st.button('Calculate'):

    data=json.dumps(inputs)
    print(f'data: {data}')

    res = requests.post(
        'http://localhost:8000/calculate',
        data=data)

    st.subheader(f'Result {res.json()["result"]}')
