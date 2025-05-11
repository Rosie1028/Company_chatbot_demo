import streamlit as st
import logging
from pathlib import Path
from backend.agents.agent import get_agent
from backend.config import app_config, CSS_PATH

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_custom_css() -> None:
    """Load and apply custom CSS styles."""
    try:
        if not CSS_PATH.exists():
            logger.warning(f"CSS file not found at {CSS_PATH}")
            return
            
        with open(CSS_PATH) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            logger.info("Custom CSS loaded successfully")
    except Exception as e:
        logger.error(f"Error loading CSS: {str(e)}")

def initialize_session_state() -> None:
    """Initialize session state variables."""
    try:
        if "messages" not in st.session_state:
            st.session_state.messages = []
            logger.info("Session state initialized")
    except Exception as e:
        logger.error(f"Error initializing session state: {str(e)}")

def display_chat_history() -> None:
    """Display the chat message history."""
    try:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    except Exception as e:
        logger.error(f"Error displaying chat history: {str(e)}")

def process_user_input(prompt: str, agent) -> None:
    """Process user input and generate response."""
    try:
        # Display user message
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        logger.info(f"User message processed: {prompt}")

        # Get AI response
        with st.spinner("Thinking..."):
            res = agent(prompt)
            response = res["output"]
            logger.info("AI response generated successfully")

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(response)
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )
    except Exception as e:
        logger.error(f"Error processing user input: {str(e)}")
        st.error("Sorry, I encountered an error. Please try again.")

def main() -> None:
    """Main application function."""
    try:
        # Set page config - MUST be the first Streamlit command
        st.set_page_config(
            page_title=app_config.APP_NAME,
            page_icon=app_config.APP_ICON,
            layout=app_config.LAYOUT
        )

        # Load custom CSS
        load_custom_css()

        # Initialize the agent
        agent = get_agent()
        logger.info("Agent initialized successfully")

        # Main title and description
        st.title(f"{app_config.APP_ICON} {app_config.APP_NAME}")
        st.markdown("""
        Welcome to our AI Assistant! I can help you with information about:
        - Current projects and their status
        - Team members and their roles
        - Recent publications and research
        - General company information

        Feel free to ask any questions!
        """)

        # Initialize session state
        initialize_session_state()

        # Display chat history
        display_chat_history()

        # Chat input
        if prompt := st.chat_input(app_config.CHAT_INPUT_PLACEHOLDER):
            process_user_input(prompt, agent)

    except Exception as e:
        logger.error(f"Error in main application: {str(e)}")
        st.error("An unexpected error occurred. Please try refreshing the page.")

if __name__ == "__main__":
    main()
