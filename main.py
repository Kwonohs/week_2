import streamlit as st
import time
import numpy as np
import pandas as pd
import datetime

# st.text("hello world")
# st.write("hello world")
# st.title('Title1 :v:', help = 'what?') #description을 달아준다.
# st.header('Title2 :v:', divider = True) #선을 표현
# st.header('Title2 :v:', divider = True) 
# st.subheader('Title3 :v:', anchor = '4d1fe655') #링크된 곳으로 이동해주는것이 anchor

st.title('9.파이썬 모듈')
st.header('9.1 모듈과 import', anchor='a55a60f8')
st.header('9.2 표준 모듈의 활용', anchor='a55a60f8')
st.header('9.3 외부 모듈의 활용', anchor='a55a60f8')

st.title('10.파이썬의 파일 입출력')
st.header('10.1 파일 입출력의 개요', anchor='7123b396')
st.header('10.2 파일 출력(output)', anchor='7123b396')
st.header('10.3 파일 입력(input)', anchor='7123b396')

st.divider()

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

st.download_button(
    'download',
    '1234',
    file_name='default.txt'
)

st.link_button(
    'naver',
    url='https:/www.naver.com',
)

st.checkbox("is_decimal")
check = st.toggle("is_decimal")
if check:
    st.write("check on")

option = st.radio(
    'options',
    ["asd", "bsd", "csd"],
    index=0
)
st.write(option)


option = st.selectbox(
    'options',
    ['apple', 'banana', 'kiwi'],
    index = 0
)

option = st.multiselect(
    'options',
    ['apple', 'banana', 'kiwi'],
    default=['apple']
)

st.write(option)

color = st.select_slider(
    'select colr',
    options=[
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'indigo',
        'violet',
    ]
)


st.write(f'color: {color}')


user_input_number = st.number_input(
    'input number',

)

st.write(user_input_number)

age = st.slider(
    'select number in a given range',
    0,
    100,
)
st.write(age)

date = st.date_input(
    'input_date',
    datetime.datetime(2024, 8, 12) 
)

st.write(date)

col1, col2 = st.columns([1, 1]) #1:1로 쪼개는것
#col1, col2 = st.columns(2) 2등분
#col1, col2 = st.columns([0.3, 0.7]) 3:7로 쪼개는것
with col1:
    st.header('Col1')
    st.subheader('Col1.1')


with col2:
    st.header('Col2')
    st.subheader('Col2.1')
    col3, col4 = st.columns([0.3, 0.7])

    with col3:
        st.header('Col2')
        st.subheader('Col2.1')
    with col4:
        st.header('Col2')
        st.subheader('Col2.1')

with st.container(border = True):
    st.write('hello world')


with st.popover('click here'):
    st.write('hello world')
    st.write('hello world')
    st.write('hello world')
    st.write('hello world')
    st.write('hello world')
    st.write('hello world')



tab1, tab2 = st.tabs(['aplle', 'banana'])

with tab1:
    st.write('tab1')
    st.write('tab1')
    
with tab2:
    st.write('tab2')
    st.write('tab2')



# prompt = st.chat_input(
#     placeholder='default message'
# )
# st.write(prompt)

# progress_bar = st.progress(0, 'on going')

# for percentage in range(100):
#     time.sleep(0.05)
#     progress_bar.progress(percentage + 1,
#                           text='ongoing',
#                           )
    
# progress_bar.empty()




# st.markdown(':red-background[hello world]')
# st.divider() #줄 긋기
# st.code('''
#         print('hello world')
#         print('hello hello')
#         ''',
#         language='python',
#         line_numbers=True,
#         )

# st.divider() #줄 긋기
# def get_user_name():
#     return 'john'

# with st.echo('below'):
#     def get_punctuation():
#         return '!!!'

#     greeting = "Hi there, "
#     value = get_user_name()
#     punctuation = get_punctuation()

#     st.write(greeting, value, punctuation)




# st.write_stream(['''
# Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
# incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
# nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'''])


#streamlit을 웹에 출력하기 위해서는 기존에 웹을 실행시켰다면 ctrl + c를 눌러서 꺼주고
#다시 실행시킨다.

# _LOREM_IPSUM = """
# Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
# incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
# nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
# """

# def stream_data():
#     for word in _LOREM_IPSUM.split(" "):
#         yield word + " "
#         time.sleep(0.02)

#     yield pd.DataFrame(
#         np.random.randn(5, 10),
#         columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
#     )

#     for word in _LOREM_IPSUM.split(" "):
#         yield word + " "
#         time.sleep(0.02)

# if st.button("Stream data"):
#     st.write_stream(stream_data)