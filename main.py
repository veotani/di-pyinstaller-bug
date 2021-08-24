"""
Demonstrate bug within dependency-injector -- PyInstaller collaboration.

When you try to run this script using `python main.py` it will run successfully. If you try to bundle this script
using PyInstaller, it will raise an exception.
"""
from container import prepare_container
from printer.hello_world import start_endless_printer


def main():
    """Configure containers and start running endless process that uses these containers."""
    prepare_container()
    start_endless_printer()


if __name__ == "__main__":
    main()
