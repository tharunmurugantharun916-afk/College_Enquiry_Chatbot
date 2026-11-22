AI-Based College Enquiry Chatbot
================================

PROJECT CONTENTS
- app.py: Flask web server and /chat API endpoint
- chatbot.py: keyword-based question matching and sample answers
- templates/index.html: chatbot page
- static/style.css: page design
- static/script.js: browser-to-server chat connection
- requirements.txt: Python dependency

REQUIREMENTS
- Python 3.9 or newer
- VS Code (recommended)
- A web browser

RUN ON WINDOWS
1. Extract this ZIP file.
2. Open the extracted College_Enquiry_Chatbot folder in VS Code.
3. Open Terminal > New Terminal.
4. (Optional but recommended) Create a virtual environment:
      py -m venv .venv
      .venv\Scripts\activate
5. Install dependencies:
      python -m pip install -r requirements.txt
6. Start the server:
      python app.py
7. Keep the terminal running and open this URL in your browser:
      http://127.0.0.1:5000

IMPORTANT
- Do not open templates/index.html directly by double-clicking it.
- Do not use the VS Code Live Server extension for this Flask project.
- The browser page must be opened through http://127.0.0.1:5000.
- Stop the server with Ctrl+C in the terminal.
- Edit the sample answers in chatbot.py to add your actual college name,
  courses, fees, hostel details, placements and contact information.

ABOUT THE "AI"
This starter project uses keyword matching and a prepared knowledge base.
It is a basic chatbot prototype, not a generative AI model. A real AI model
or API can be integrated as a later enhancement.
