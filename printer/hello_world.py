"""Printer that prints hello, world!"""
from dependency_injector.wiring import inject, Provide

from container import Container


@inject
def start_endless_printer(build_message=Provide[Container.message_builder]):
    """Start endless printer."""
    message = build_message
    assert isinstance(message, str)
    while True:
        print(message)
