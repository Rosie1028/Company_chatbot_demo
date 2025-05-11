import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.agents import initialize_agent
from langchain.tools import Tool
import random
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from ..config import query_patterns, response_templates

# Load environment variables
load_dotenv()

# Get OpenAI API key with error handling
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found in environment variables. "
        "Please add it to your .env file or set it as an environment variable."
    )

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class Project:
    """Project data structure."""
    name: str
    status: str
    team: str

@dataclass
class Publication:
    """Publication data structure."""
    title: str
    year: int
    authors: List[str]

@dataclass
class TeamMember:
    """Team member data structure."""
    name: str
    role: str
    department: str

class CompanyData:
    """Class to store and manage company data."""
    
    def __init__(self):
        self.projects: List[Project] = [
            Project("AI Research Initiative", "Active", "Data Science"),
            Project("Cloud Migration", "Completed", "Infrastructure"),
            Project("Security Audit", "In Progress", "Security")
        ]
        
        self.publications: List[Publication] = [
            Publication("Machine Learning in Practice", 2023, ["John Doe", "Jane Smith"]),
            Publication("Cloud Computing Trends", 2024, ["Alice Johnson"])
        ]
        
        self.team: List[TeamMember] = [
            TeamMember("John Doe", "Lead Data Scientist", "Data Science"),
            TeamMember("Jane Smith", "Senior Developer", "Engineering"),
            TeamMember("Alice Johnson", "Project Manager", "Product")
        ]

class ResponseTemplates:
    """Class to manage response templates for different types of queries."""
    
    def __init__(self):
        self.templates = {
            "projects": response_templates.PROJECTS,
            "team": response_templates.TEAM,
            "publications": response_templates.PUBLICATIONS,
            "greeting": response_templates.GREETING,
            "fallback": response_templates.FALLBACK
        }
    
    def get_random_response(self, category: str) -> str:
        """Get a random response from the specified category."""
        try:
            return random.choice(self.templates.get(category, self.templates["fallback"]))
        except Exception as e:
            logger.error(f"Error getting response for category {category}: {str(e)}")
            return self.templates["fallback"][0]

class ChatbotAgent:
    """Main chatbot agent class that handles query processing and response generation."""
    
    def __init__(self):
        self.data = CompanyData()
        self.responses = ResponseTemplates()
        self.query_patterns = {
            "greeting": query_patterns.GREETING,
            "projects": query_patterns.PROJECTS,
            "team": query_patterns.TEAM,
            "publications": query_patterns.PUBLICATIONS
        }
        logger.info("ChatbotAgent initialized successfully")
    
    def _format_projects_response(self) -> str:
        """Format projects information for response."""
        try:
            projects_info = "\n".join([
                f"- {p.name} ({p.status})" 
                for p in self.data.projects
            ])
            return f"{self.responses.get_random_response('projects')}\n{projects_info}"
        except Exception as e:
            logger.error(f"Error formatting projects response: {str(e)}")
            return self.responses.get_random_response("fallback")
    
    def _format_team_response(self) -> str:
        """Format team information for response."""
        try:
            team_info = "\n".join([
                f"- {m.name} ({m.role})" 
                for m in self.data.team
            ])
            return f"{self.responses.get_random_response('team')}\n{team_info}"
        except Exception as e:
            logger.error(f"Error formatting team response: {str(e)}")
            return self.responses.get_random_response("fallback")
    
    def _format_publications_response(self) -> str:
        """Format publications information for response."""
        try:
            pub_info = "\n".join([
                f"- {p.title} ({p.year})" 
                for p in self.data.publications
            ])
            return f"{self.responses.get_random_response('publications')}\n{pub_info}"
        except Exception as e:
            logger.error(f"Error formatting publications response: {str(e)}")
            return self.responses.get_random_response("fallback")
    
    def _matches_pattern(self, query: str, pattern: List[str]) -> bool:
        """Check if query matches any of the given patterns."""
        try:
            return any(word in query.lower() for word in pattern)
        except Exception as e:
            logger.error(f"Error matching pattern: {str(e)}")
            return False
    
    def process_query(self, query: str) -> Dict[str, str]:
        """Process the user query and generate appropriate response."""
        try:
            logger.info(f"Processing query: {query}")
            
            if not query or not isinstance(query, str):
                logger.warning("Received invalid query")
                return {"output": self.responses.get_random_response("fallback")}
            
            if self._matches_pattern(query, self.query_patterns["greeting"]):
                return {"output": self.responses.get_random_response("greeting")}
            
            if self._matches_pattern(query, self.query_patterns["projects"]):
                return {"output": self._format_projects_response()}
            
            if self._matches_pattern(query, self.query_patterns["team"]):
                return {"output": self._format_team_response()}
            
            if self._matches_pattern(query, self.query_patterns["publications"]):
                return {"output": self._format_publications_response()}
            
            logger.info("No matching pattern found, using fallback response")
            return {"output": self.responses.get_random_response("fallback")}
            
        except Exception as e:
            logger.error(f"Error processing query: {str(e)}")
            return {"output": self.responses.get_random_response("fallback")}

def get_agent():
    """Factory function to create and return a new chatbot agent."""
    try:
        agent = ChatbotAgent()
        logger.info("Agent created successfully")
        return agent.process_query
    except Exception as e:
        logger.error(f"Error creating agent: {str(e)}")
        raise
