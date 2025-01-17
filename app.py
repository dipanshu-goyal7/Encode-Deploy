from typing import Annotated
from typing_extensions import TypedDict
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from audio_recorder_streamlit import audio_recorder
from speech_recognition import Recognizer, AudioFile
import requests
import streamlit as st
import requests
from dotenv import load_dotenv
import os
import base64
from langchain_core.messages import BaseMessage

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode, tools_condition

# Load environment variables
load_dotenv()

# Memory Saver
memory = MemorySaver()

# Define the State
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Initialize the Graph Builder
graph_builder = StateGraph(State)
os.environ["TAVILY_API_KEY"] =os.getenv("TRI_KEY")
tool = TavilySearchResults(max_results=2)
tools = [tool]
# Initialize the LLM
llm = ChatGroq(
    temperature=0.7,
    groq_api_key=os.getenv("API_KEY"),
    model="llama-3.1-70b-versatile"
)
llm_with_tools = llm.bind_tools(tools)

# Define the Chatbot Node
def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# Build the Graph
graph_builder.add_node("chatbot", chatbot)

tool_node = ToolNode(tools=[tool])
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
# Any time a tool is called, we return to the chatbot to decide the next step
graph_builder.add_edge("tools", "chatbot")
graph_builder.set_entry_point("chatbot")
graph = graph_builder.compile()

def text_to_speech(text, output_file):
    """Convert text to speech using Deepgram TTS and save as MP3."""
    DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
    TTS_API_URL = "https://api.deepgram.com/v1/speak?model=aura-orpheus-en"
    
    headers = {
        "Authorization": f"Token {DEEPGRAM_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "text": text
    }
    response = requests.post(TTS_API_URL, headers=headers, json=payload, stream=True)
    if response.status_code == 200:
        # Save the audio response as MP3
        with open(output_file, "wb") as f:
            f.write(response.content)
        return True
    else:
        st.error(f"Deepgram TTS Error: {response.json()}")
        return False

def transcribe_audio(audio_file_path):
    """Transcribe audio using the SpeechRecognition library."""
    recognizer = Recognizer()
    with AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except Exception as e:
            return ""

# Streamlit App
def auto_play_audio(audio_file):
    with open(audio_file,"rb") as audio_file:
        audio_bytes=audio_file.read()
    base64_audio=base64.b64encode(audio_bytes).decode("utf-8")
    audio_html=f'<audio src="data:audio/mp3;base64,{base64_audio}" controls autoplay>'
    st.markdown(audio_html, unsafe_allow_html=True)

def create_streamlit_app():
    st.set_page_config(layout="wide", page_title="Sergio")
    st.title("Sergio - AI Powered Property Dealer")

    # Session state for messages
    if "messages" not in st.session_state:
        st.session_state.messages = [
            ("system", '''You are Sergio, a professional and customer-focused real estate agent. 
             Customers will call or inquire online about properties. Your goal is to engage them warmly, understand their requirements, 
             and provide tailored property suggestions. Maintain a friendly and professional tone, highlighting key features and benefits.
              Address any queries confidently and guide the conversation toward scheduling a site visit or next steps. Once the customer 
              agrees, express gratitude and assure them that a team member will contact them soon to finalize the arrangements. 
              Keep responses concise, empathetic, and solution-oriented to leave a lasting positive impression.Keep your answer in 70 words''')
        ]
    # Audio Recorder
    st.markdown("### Click Below to talk")
    audio_bytes = audio_recorder()

    if audio_bytes:
        # Save audio
        audio_file_path = "recorded_audio.wav"
        with open(audio_file_path, "wb") as f:
            f.write(audio_bytes)

        # Transcribe audio
        user_input = transcribe_audio(audio_file_path)

        if len(user_input) != 0:
            # Append transcribed text to chat history
            st.session_state.messages.append(("user", user_input))

            # Generate AI response
            config = {"configurable": {"thread_id": "1"}}
            last_event = None

            for event in graph.stream({"messages": st.session_state.messages}, config):
                last_event = event  # Keep updating last_event with the current event

# After the loop, last_event will contain the last event
            if last_event is not None:
                for value in last_event.values():
                    ai_response = value["messages"][-1].content
           
                    st.session_state.messages.append(("ai", ai_response))

                    # Display response
                    st.markdown(f"**AI:** {ai_response}")
                    
                    # Convert AI response to speech (MP3)
                    tts_output_file = "ai_response.mp3"  # Save as MP3
                    if text_to_speech(ai_response, tts_output_file):
                        auto_play_audio(tts_output_file)
        else:
            # Handle case where no audio is detected
            st.markdown(f'Sorry, could not hear you')

if __name__ == "__main__":
    create_streamlit_app()
