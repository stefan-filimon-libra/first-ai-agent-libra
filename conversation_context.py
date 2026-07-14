"""
Conversation memory management.

This module is responsible for storing and retrieving
messages exchanged between the user and the AI assistant.
"""

from config import SYSTEM_PROMPT

class ConversationContext:
    def __init__(self):
        self.messages = [
            self.assemble_system_prompt()
        ]

    def assemble_system_prompt(self):
        return {
            "role":"sys_prompt",
            "content": SYSTEM_PROMPT
        }
        # TODO: return a system message dict with the system prompt from config
        # Hint: Observe the message format used in agent.py
        # Hint: The system prompt should be a message dict with role "system"

    def add_message(self, message):
        pass
        # TODO: Implement message addition logic
        print(message)
        self.messages.append(message)

    def get_history(self):
        pass
        # TODO: return the full message history
        return self.messages
