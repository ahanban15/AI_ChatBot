import streamlit as st
from streamlit_chat import message
import json
from bardapi import Bard

with open('credentials.json', 'r') as f:
    file = json.load(f)
    token = file['token']


# output of prompt
def generate_response(prompt):
    # prompt = 'test'
    # return prompt
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response


# function to receive user queries
def get_text():
    input_text = st.text_input("CN BOT:", "", key='Press Enter to apply')
    return input_text


# Title of AI-Bot
st.title('Personal Tutoring Bot!!!')

# background of Bot
changes = '''
<style>
[data-testid = "stAppViewContainer"]
    {
        background: orange;
        background-size:cover;
    }
</style>
'''

# commit that change
st.markdown(changes, unsafe_allow_html=True)
print(st.session_state)

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# to get input query from user
user_input = get_text()

# function calling if else
if user_input:
    print(user_input)
    output = generate_response(user_input)
    print(output)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

# to store and show the live prompts of an active session
if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], key="user_" + str(i), is_user=True)
