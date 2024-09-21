# Real-Time Log Watching with Django Channels

This project implements a real-time log watching solution using Django Channels. It allows clients to monitor updates to a log file in real time via WebSocket connections, simulating behavior similar to the `tail -f` command in UNIX.

## Features

- Real-time log updates sent to connected clients.
- Clients receive the last 10 lines of the log file upon connecting.
- Supports multiple clients simultaneously.
- Built using Django Channels and `aiofiles` for asynchronous file handling.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Django
- Django Channels
- `aiofiles`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/priyanshukatiyar14/log-monitoring.git
   cd log-monitoring
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Django project:

   - Update `settings.py` to include `'channels'` in your `INSTALLED_APPS`.
   - Define your channel layers (e.g., Redis) in `settings.py`.

## Usage

1. Create a log file if it doesn't already exist:

   ```bash
   touch logfile.log
   ```

2. Run the Django development server in another terminal:

   ```bash
   python manage.py runserver
   ```

3. Connect to the WebSocket endpoint (e.g., via a web client or tool) at:

   ```
   ws://localhost:8000/ws/log/
   ```

4. You will receive real-time log updates as they are appended to `logfile.log`.

## Code Overview

### `consumers.py`

- Contains the `LogConsumer` class that handles WebSocket connections.
- Monitors the log file for new entries and broadcasts updates to connected clients.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django Channels](https://channels.readthedocs.io/en/stable/)
- [aiofiles](https://github.com/Tinche/aiofiles)

### Instructions for Use

- Update the repository URL in the **Clone the repository** section.
- If you have specific dependencies, add them to `requirements.txt` and include instructions for any additional setup.
- Modify any project-specific instructions or information as needed.
