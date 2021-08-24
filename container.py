"""DI container."""
from dependency_injector.containers import DeclarativeContainer
from dependency_injector import providers

from message_builder.hello_world import build


class Container(DeclarativeContainer):
    """Container with only message builder."""

    message_builder = providers.Callable(build)


def prepare_container():
    container = Container()
    import printer
    container.wire(packages=[printer])
