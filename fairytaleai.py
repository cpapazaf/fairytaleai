import streamlit as st
from streamlit_image_select import image_select
import openai

openai.api_key = st.secrets["OPENAI_KEY"]
model_engine = "text-davinci-003"

# st.markdown("<h1 style='text-align: center; color: black;'>Fairytale AI</h1>", unsafe_allow_html=True)
st.title('Fairytale AI :sunglasses:')

ANIMALS = {
    "https://freesvg.org/img/version2-yellow-tiger-cat.png": "cat",
    "https://www.publicdomainpictures.net/pictures/420000/nahled/dog-puppy-cartoon-illustration.png": "dog",
    "https://freesvg.org/img/sciccareddu.png": "donkey",
    "https://freesvg.org/img/Cute-Penguin.png": "penguin"
}

img = image_select(
    label="Select a carachter",
    images=list(ANIMALS.keys()),
    captions=[ANIMALS[i].capitalize() for i in ANIMALS.keys()],
)

DIDAGMA={
    'being brave when alone': "being brave when alone, stay calm and seek help from someone you trust",
    'staying strong when bullied': "staying strong and calm when someone tries to bully you as well as seek help from a trusted adult",
    'being kind an polite to others': "being kind and polite to others, always try to help when you can and know that you will feel good afterwards",
    'playing carefully': "being careful when playing with others and avoid having accidents",
    'taking care of oneself': "taking care of the wellbeing of the body and the mind by playing carefully and avoiding accidents",
    'stranger danger': "never talking or accepting anything from strangers as well as never following any stranger. Include in the story the phrase \"Stranger Danger!\"",
    'showing empathy': "showing empathy and trying to listen to other people's emotions",
    'darkness': 'not being scarred in darkness'
}

option = st.selectbox(
    "A story about ...",
    DIDAGMA.keys())

the_prompt = f"Please write a fairytale about {DIDAGMA[option]}. Use as caracter a little {ANIMALS[img]}. Make it similar to Aesop's fairytales and always include a leasson learned at the end. Use child friendly language."

if st.button("Write"):
    with st.spinner('Wait for it...'):
        try:
            # response = openai.Image.create(
            #     prompt=the_prompt,
            #     n=1,
            #     size="256x256",
            # )

            # st.image(response["data"][0]["url"])

            completion = openai.Completion.create(
                engine=model_engine,
                prompt=the_prompt,
                max_tokens=4096-len(the_prompt),
                n=1,
                stop=None,
                temperature=0.4,
            )

            response = completion.choices[0].text
            st.write(response)
        except openai.error.Timeout as e:
            #Handle timeout error, e.g. retry or log
            st.error(f"OpenAI API request timed out: {e}", icon="🚨")
            pass
        except openai.error.APIError as e:
            #Handle API error, e.g. retry or log
            st.error(f"OpenAI API returned an API Error: {e}", icon="🚨")
            pass
        except openai.error.APIConnectionError as e:
            #Handle connection error, e.g. check network or log
            st.error(f"OpenAI API request failed to connect: {e}", icon="🚨")
            pass
        except openai.error.InvalidRequestError as e:
            #Handle invalid request error, e.g. validate parameters or log
            st.error(f"OpenAI API request was invalid: {e}", icon="🚨")
            pass
        except openai.error.AuthenticationError as e:
            #Handle authentication error, e.g. check credentials or log
            st.error(f"OpenAI API request was not authorized: {e}", icon="🚨")
            pass
        except openai.error.PermissionError as e:
            #Handle permission error, e.g. check scope or log
            st.error(f"OpenAI API request was not permitted: {e}", icon="🚨")
            pass
        except openai.error.RateLimitError as e:
            #Handle rate limit error, e.g. wait or log
            st.error(f"OpenAI API request exceeded rate limit: {e}", icon="🚨")
            pass
