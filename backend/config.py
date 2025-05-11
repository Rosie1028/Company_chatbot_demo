from typing import Dict, List
from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class AppConfig:
    """Application configuration settings."""
    APP_NAME: str = "Company AI Assistant"
    APP_ICON: str = "🤖"
    LAYOUT: str = "wide"
    CHAT_INPUT_PLACEHOLDER: str = "Ask me anything..."

@dataclass
class QueryPatterns:
    """Query pattern configurations."""
    GREETING: List[str] = field(default_factory=lambda: ["hello", "hi", "hey", "greetings"])
    PROJECTS: List[str] = field(default_factory=lambda: ["project", "work", "initiative", "status"])
    TEAM: List[str] = field(default_factory=lambda: ["team", "member", "employee", "staff", "who"])
    PUBLICATIONS: List[str] = field(default_factory=lambda: ["publication", "paper", "research", "article"])

@dataclass
class ResponseTemplates:
    """Response template configurations."""
    PROJECTS: List[str] = field(default_factory=lambda: [
        "Here are our current projects:",
        "Let me tell you about our ongoing projects:",
        "Here's what we're working on:"
    ])
    TEAM: List[str] = field(default_factory=lambda: [
        "Our team consists of:",
        "Here are our team members:",
        "Let me introduce you to our team:"
    ])
    PUBLICATIONS: List[str] = field(default_factory=lambda: [
        "Here are our recent publications:",
        "We've published several papers:",
        "Our research output includes:"
    ])
    GREETING: List[str] = field(default_factory=lambda: [
        "Hello! How can I help you today?",
        "Hi there! What would you like to know?",
        "Welcome! What can I tell you about our company?"
    ])
    FALLBACK: List[str] = field(default_factory=lambda: [
        "I'm not sure about that, but I can tell you about our projects, team, or publications.",
        "I don't have that information, but I can help you with other company-related questions.",
        "I'm still learning! Try asking about our projects, team members, or publications."
    ])

# Initialize configurations
app_config = AppConfig()
query_patterns = QueryPatterns()
response_templates = ResponseTemplates()

# File paths
ROOT_DIR = Path(__file__).parent.parent
CSS_PATH = ROOT_DIR / "style.css" 