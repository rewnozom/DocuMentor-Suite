from typing import Dict, Type, List
from .base import BaseCommand
from .implementations import (
    FullInfoCommand,
    SummaryCommand,
    TechnicalCommand,
    CompatibilityCommand
)

class CommandRegistry:
    """
    Central registration and management of all commands.
    """
    def __init__(self):
        self.commands: Dict[str, Type[BaseCommand]] = {}
        self._register_default_commands()

    def _register_default_commands(self):
        """Registers standard commands"""
        self.register_command('f', FullInfoCommand)
        self.register_command('s', SummaryCommand)
        self.register_command('t', TechnicalCommand)
        self.register_command('c', CompatibilityCommand)

    def register_command(self, identifier: str, command_class: Type[BaseCommand]):
        """Registers a new command"""
        self.commands[identifier] = command_class

    def get_command(self, identifier: str) -> BaseCommand:
        """Gets a command instance"""
        if identifier not in self.commands:
            raise ValueError(f"Unknown command: {identifier}")
        return self.commands[identifier]()

    def list_commands(self) -> List[str]:
        """Lists all available commands"""
        return list(self.commands.keys())