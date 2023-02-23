import streamlit as st
import openai

openai.api_key = ""
model_engine = "text-davinci-003"

st.markdown("<h1 style='text-align: center; color: black;'>Fairytale AI</h1>", unsafe_allow_html=True)


from streamlit_image_select import image_select

ANIMALS = {
    "https://freesvg.org/img/Blue-Cat.png": "cat",
    "https://www.publicdomainpictures.net/pictures/420000/nahled/dog-puppy-cartoon-illustration.png": "dog",
    "https://freesvg.org/img/sciccareddu.png": "donkey",
    "https://freesvg.org/img/Cute-Penguin.png": "penguin"
}

img = image_select(
    label="Select a carachter",
    images=list(ANIMALS.keys()),
    captions=["Cat", "Dog", "Donkey", "Penguin"],
)

DIDAGMA={
    'brave when alone': "",
    'strong when under bullying': "",
    'kind an polite to others': "",
    'strong after an accident': "",
}

option = st.selectbox(
    "A story about being ...",
    DIDAGMA.keys())

if st.button("Write"):
    with st.spinner('Wait for it...'):
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=f"Please write a fairytale about being {option}. Use as caracter a small {ANIMALS[img]}. Please make it similar to Aesop's fairytales and always add a leasson learned at the end.",
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )

        response = completion.choices[0].text
        st.write(response)
