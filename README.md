# Sergio - AI-Powered Property Dealer  

Sergio is an AI-powered, voice-enabled sales agent designed to assist users in real estate transactions. The system leverages advanced language models and Speech-to-Text (STT) and Text-to-Speech (TTS) technologies to create a conversational and interactive experience for potential buyers and sellers.  

With Sergio, users can communicate in natural language, inquire about properties, and close deals seamlessly, ensuring a professional, customer-focused experience.  

Experience at [encode-sergio](https://encode-sergio.streamlit.app/)

---

## Features  

### 1. **Voice Interaction**  
- **Speech-to-Text (STT):** Users can speak into their microphone, and Sergio transcribes the audio to text using the SpeechRecognition library.  
- **Text-to-Speech (TTS):** Sergio generates responses and converts them into speech using the Deepgram API, creating a seamless conversational experience.  

### 2. **AI-Powered Responses**  
- Uses **LangChain** and **LangGraph** to process user inputs and generate professional, context-aware responses.  
- Integrated with tools like **Tavily Search** to fetch real-time information and enhance the interaction.  

### 3. **Real Estate Expertise**  
- Sergio acts as a real estate agent, guiding users through the property inquiry process, understanding their needs, and offering tailored solutions.  
- Provides concise, empathetic, and professional responses to help close deals effectively.  

### 4. **Audio Playback**  
- Automatically plays audio responses for a more engaging experience.  

---

## Installation  

### Prerequisites  
Ensure the following are installed on your system:  
- Python 3.7+  
- FFmpeg (required for audio playback)  

### Steps  

1. **Clone the Repository**  
   ```bash  
   git clone <repository-url>  
   cd <repository-folder>  
   ```  

2. **Set Up a Virtual Environment**  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # For Windows: venv\Scripts\activate  
   ```  

3. **Install Dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Set Up Environment Variables**  
   Create a `.env` file in the project directory with the following keys:  
   ```env  
   API_KEY=<your_groq_api_key>  
   TRI_KEY=<your_tavily_api_key>  
   DEEPGRAM_API_KEY=<your_deepgram_api_key>  
   ```  

5. **Run the Application**  
   ```bash  
   streamlit run <filename>.py  
   ```  

---

## Usage  

1. Open the application in your browser (default: `http://localhost:8501`).  
2. Click the **microphone button** to speak to Sergio.  
3. Sergio will transcribe your speech, generate a response, and play it back to you.  
4. Engage in a conversation to inquire about properties or close deals.  

---

## Project Structure  

```plaintext  
├── main.py                   # Main Streamlit app  
├── requirements.txt          # Python dependencies  
├── system_prompt.txt         # System prompt for the AI agent  
├── .env                      # Environment variables  
├── ai_response.mp3           # Generated AI response audio file  
├── recorded_audio.wav        # Recorded user audio  
└── README.md                 # Project documentation  
```  

---

## Technologies Used  

### 1. **Speech-to-Text (STT)**  
- `SpeechRecognition`: Used to transcribe user audio into text.  

### 2. **Text-to-Speech (TTS)**  
- `Deepgram API`: Converts AI-generated text into realistic speech.  

### 3. **Language Model**  
- `LangChain` and `LangGraph`: Generate intelligent and context-aware responses.  
- Integrated with **Tavily Search Results** for real-time data access.  

### 4. **Frontend**  
- `Streamlit`: Provides an interactive user interface for voice-based interactions.  

---

## Features in Detail  

### AI Responses  
Sergio uses **Groq's ChatGroq** model with pre-trained capabilities to engage users in meaningful conversations. It processes user inputs and responds in a professional tone, focusing on customer satisfaction and deal closure.  

### Real-Time Audio Playback  
With TTS integration, responses are automatically converted into speech and played back to the user, ensuring a smooth and engaging experience.  

---

## Future Enhancements  

- **Multi-Language Support**: Add support for non-English languages.  
- **Property Database Integration**: Connect to real estate databases for dynamic property listings.  
- **Personalization**: Tailor responses based on user preferences and history.  

---

## Contributing  

1. Fork the repository.  
2. Create a new branch:  
   ```bash  
   git checkout -b feature-name  
   ```  
3. Commit your changes:  
   ```bash  
   git commit -m "Add feature description"  
   ```  
4. Push to the branch:  
   ```bash  
   git push origin feature-name  
   ```  
5. Submit a pull request.  

---

## License  

This project is licensed under the MIT License. See the `LICENSE` file for more details.  

---

## Contact  
Here’s the corrected formatting for your contact section:  

---

## Contact  

For questions, feedback, or collaboration opportunities, feel free to reach out to us:  

### **Lakshya Batra**  
- **Email**: [tt1222163@textile.iitd.ac.in](mailto:tt1222163@textile.iitd.ac.in)  
- **LinkedIn**: [linkedin.com/in/lakshyabatra04/](https://www.linkedin.com/in/lakshyabatra04/)  

### **Lakshya Kumar**  
- **Email**: [tt1222183@textile.iitd.ac.in](mailto:tt1222183@textile.iitd.ac.in)  
- **LinkedIn**: [linkedin.com/in/lakshya-kumar-5a205a258/](https://www.linkedin.com/in/lakshya-kumar-5a205a258/)  

### **Dipanshu Goyal**  
- **Email**: [tt1222143@textile.iitd.ac.in](mailto:tt1222143@textile.iitd.ac.in)  
- **LinkedIn**: [linkedin.com/in/dipanshu-goyal-76a1b825a/](https://www.linkedin.com/in/dipanshu-goyal-76a1b825a/)  

Enjoy using Sergio! 😊  
