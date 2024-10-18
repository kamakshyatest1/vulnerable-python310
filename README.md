
# Vulnerable Python 3.10 Compatible Sample Project

This is a simple Python project designed to showcase the usage of outdated and vulnerable dependencies for testing purposes.
The project is restricted to Python 3.10.x.

## Prerequisites

- Python 3.10.x

## How to Run

1. Create a virtual environment:
    ```bash
    python3.10 -m venv venv
    ```

2. Activate the virtual environment:
    ```bash
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate   # On Windows
    ```

3. Install the project and dependencies:
    ```bash
    pip install .
    ```

4. Run the project:
    ```bash
    python main.py
    ```

## Dependencies

The project includes intentionally vulnerable versions of dependencies, such as:
- Flask 1.0
- Requests 2.19.1
- PyYAML 3.13

These versions are known to have security vulnerabilities and should not be used in production environments.

## Purpose

This project is for security testing and educational purposes only.
