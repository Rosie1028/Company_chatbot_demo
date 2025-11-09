Company AI Assistant Demo
Overview
Company AI Assistant Demo is a lightweight chatbot application developed using Streamlit and Python. Originally built for a medical institution, it has been generalized for broader use as a company-facing assistant. The chatbot simulates an internal AI assistant capable of answering predefined questions about projects, team members, and publications. It serves as a modular, customizable proof-of-concept for building conversational interfaces in organizational settings.

You can view the repository here: Company AI Assistant Demo on GitHub

Tech Stack
Python: Core backend logic and data handling.

Streamlit: Web framework for building the interactive chat interface.

Custom CSS: Used to style and customize the frontend appearance.

In-Memory Data Storage: Sample data stored in Python dictionaries for quick prototyping.

Modular Architecture: Backend logic separated into agents for easy customization.

Features
Interactive Chat Interface: Real-time conversation simulation using Streamlit.

Predefined Responses: Handles common queries about company operations.

Modular Design: Easily customizable sample data and response logic.

Generalized Use Case: Adapted from a medical institution prototype to a flexible company-facing assistant.

Project Structure
Code
intranet_bot/
├── app.py              # Main Streamlit application
├── style.css           # Custom styling
├── requirements.txt    # Project dependencies
└── backend/
    └── agents/
        └── agent.py    # Chatbot logic and responses
Installation
Prerequisites
Python 3.8 or higher

pip (Python package installer)

Setup
bash
git clone https://github.com/Rosie1028/Company_chatbot_demo.git
cd intranet_bot

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
Run the Application
bash
streamlit run app.py
Then open your browser to the URL shown in the terminal (usually http://localhost:8501).

Testing the Chatbot
Try asking questions like:

Greetings: "Hello", "Hi there", "Hey"

Projects: "What projects are you working on?", "Tell me about your initiatives"

Team: "Who are the team members?", "Tell me about your staff"

Publications: "What publications do you have?", "What papers have you published?"

Customization
Sample Data: Modify SAMPLE_DATA in backend/agents/agent.py to reflect your own organization.

Response Patterns: Adjust RESPONSES in the same file to change how the chatbot replies.

Styling: Edit style.css to customize colors, layout, and visual elements.

License
This project is licensed under the MIT License.

