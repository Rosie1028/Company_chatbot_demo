# Company AI Assistant Demo

A simple chatbot demo that simulates a company's AI assistant. This project demonstrates a basic chatbot interface using Streamlit, with predefined responses about company projects, team members, and publications.

## Features

- Interactive chat interface
- Predefined responses for common queries
- Information about:
  - Company projects
  - Team members
  - Publications
  - General company information

## Tech Stack

- **Frontend/UI**:
  - Streamlit (Python web framework)
  - Custom CSS for styling
  - Responsive chat interface

- **Backend**:
  - Python 3.8+
  - In-memory data storage (sample data)
  - Modular architecture with backend/agents separation

- **Development Tools**:
  - Virtual environment (venv)
  - pip for package management
  - Environment variables for configuration

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd intranet_bot
```

2. Create and activate a virtual environment:
```bash
# On macOS/Linux
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

## Testing the Chatbot

You can test the chatbot with various questions. Here are some examples:

### Greetings
- "Hello"
- "Hi there"
- "Hey"

### Projects
- "What projects are you working on?"
- "Tell me about your initiatives"
- "What's the status of current projects?"

### Team
- "Who are the team members?"
- "Tell me about your staff"
- "Who works in the company?"

### Publications
- "What publications do you have?"
- "Tell me about your research"
- "What papers have you published?"

## Project Structure

```
intranet_bot/
├── app.py              # Main Streamlit application
├── style.css           # Custom styling
├── requirements.txt    # Project dependencies
└── backend/
    └── agents/
        └── agent.py    # Chatbot logic and responses
```

## Customization

You can customize the chatbot by modifying the following:

1. Sample data in `backend/agents/agent.py`:
   - Update `SAMPLE_DATA` to include your own projects, team members, and publications
   - Modify `RESPONSES` to change the chatbot's response patterns

2. Styling in `style.css`:
   - Customize the appearance of the chat interface
   - Modify colors, spacing, and other visual elements

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.



