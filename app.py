import os
from dotenv import load_dotenv
from groq import Groq
import gradio as gr

load_dotenv()

LLM= ["gemma-7b-it",
        "gemma2-9b-it",
        "llama2-70b-4096",
        "llama3-8b-8192"
        "llama3-70b-8192",
        "mixtral-8x7b-32768"]


#Initialize the values for the variables according to your purpose 
MODEL = LLM[0]
SYSTEM = """
        You are an exceptional conversation builder with very exciting choice of words.
        You are excellent in keeping the client interested in the conversation.
        You are precise and does not provide long boring passages while not necessary.
"""


#Create a GROQ instance
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


#response generation function
def generate(Prompt, history):
    """
    This is where the actual generation takes place

    Prompt: A str provided by the user.
    history: A list containing the previous conversation statements including the previous
             user prompts and the LLM response
    """

    history = []
    for user, content in history:
        history.append(content=user)
        history.append(content=content)

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": SYSTEM,

        },
        {
            "role": "user",
            "content": f"{Prompt}",
        }
    ],
    model=MODEL,
    )
    return (chat_completion.choices[0].message.content)


#Construction of the UI for the application
demo = gr.ChatInterface(
    title = f"A Simple ChatBot powered by GROQ 💥",
    description="Responses at the speed of lightning 🗲",
    undo_btn=None,
    retry_btn="Retry",
    clear_btn="Clear",
    fn = generate,
    examples= ["hi", "how are you?"],
).launch(share=False)





