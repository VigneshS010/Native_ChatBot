import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from openai import OpenAI

# Load model and tokenizer only once to avoid repeated loading
@st.cache_resource
def load_model():
    model_name = 'Hemanth-thunder/english-tamil-mt'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    return tokenizer, model

tokenizer, model = load_model()

def translate(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    translate_tokens = model.generate(**inputs)
    return tokenizer.decode(translate_tokens[0], skip_special_tokens=True)




def chatbot(text):

    client = OpenAI(
        
    api_key=st.secrets["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1",
    )

    completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    extra_body={},
    model="google/gemma-3-1b-it:free",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": text
            },
            # {
            #   "type": "image_url",
            #   "image_url": {
            #     "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
            #   }
            # }
        ]
        }
    ]
    )
    return completion.choices[0].message.content


# st.set_page_config(layout="wide")
st.title('Tamil Chatbot and Translator')

col1, col2 = st.columns(2)

# Initialize session state with seperate keys
if 'chatbot_display_text' not in st.session_state:
    st.session_state.chatbot_display_text = ''
if 'chatbot_transfer_text' not in st.session_state:
    st.session_state.chatbot_transfer_text = ''
if 'user_input_tamil_convertor' not in st.session_state:
    st.session_state.user_input_tamil_convertor = ''

with col1:
    # st.markdown(
    #     """
    #     <style>
    #     [data-testid="stTextArea"] textarea {
    #         width: 200% !important;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True,
    # )
    user_input_chatbot = st.text_area('Speak with Chatbot: ', '')
    # chatbot_text = ''

    if st.button('Answer', key='ChatBot Button'):
        if user_input_chatbot:
            st.session_state.chatbot_display_text = chatbot(user_input_chatbot)
            st.session_state.chatbot_transfer_text = st.session_state.chatbot_display_text #copy also to transfer state.
        else:
            st.write('Please enter some text for the chatbot')

    if st.session_state.chatbot_display_text: # only displays if it has content.
        st.write('ChatBot Response: ')
        st.write(st.session_state.chatbot_display_text)

    if st.session_state.chatbot_transfer_text:
        if st.button('Copy Response to Translator', key='copy_to_translator'):
            st.session_state.user_input_tamil_convertor = st.session_state.chatbot_transfer_text


with col2:
    user_input_tamil_convertor = st.text_area('English to Tamil Convertor: ', st.session_state.user_input_tamil_convertor)
 
    if st.button('Translate', key='translate_button'):
        if user_input_tamil_convertor:
            translated_text = translate(user_input_tamil_convertor)
            st.write('Translated Tamil Text: ')
            st.write(translated_text)
        else:
            st.write('Please enter some text to translate.')

    # if st.session_state.trigger and chatbot_text:
    #     chatbot_converted = translate(chatbot_text)
    #     st.write('Tamil Translated text')
    #     st.write(chatbot_converted)
    #     trigger = False
        
   
        

