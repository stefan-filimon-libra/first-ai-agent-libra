"""
Application configuration.

This module contains all configurable settings used by the AI agent.

Future exercises may extend this file with:
- Model configuration
- API credentials
- Prompt templates
- Embedding settings
- Logging configuration
"""

MODEL_NAME = "qwen3:1.7b"
MODEL_ENDPOINT= "http://localhost:11434/api/chat"
SYSTEM_PROMPT = "Your name is Codey Brown and you are a math tutor. You have to act like a math tutor: explicative, pactient and kind. You will be able to answer any math problem."
