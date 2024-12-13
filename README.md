# Mistral Chatbot

In this project, I implemented Mistral AI's API into this software webapp, making my own chatbot. I decided to make this chatbot, unlike Mistral's, actually save your data and conversations, giving the bot a memory of all his actions and interactions with you. You can also create and switch between different users, each with its own database and history. So if you wish to go back to an old conversation, even after you closed and stopped running the software, you can!

## Example Use Case

**Scenario**: You have two conversation contexts, the "Default" and "Work" which you named.  
- In the "Work" context, you ask the bot domain-specific questions about your projects. The chatbot learns from prior exchanges, so when you come back tomorrow and select "Work" context again, it recalls what you discussed.
- In the "Default" context, you ask casual questions about recipes or travel. This conversation remains separate, so the chatbot doesn’t mix project-related content into your personal queries.

For example:
1. **Work Context**:
   - User: *"What’s the status of Project X’s deadline?"*
   - Chatbot: *"Last time you asked, the deadline for Project X was in two weeks."*

2. **Default Context**:
   - User: *"What’s the status of Project X’s deadline?"*
   - Chatbot: *"I'm sorry, I don't have information about Project X. Maybe you could tell me more about it?"*

## Features
- **Multiple Conversation Contexts**: Users can create and switch between different conversation contexts.
- **Dynamic Database Management**: Each conversation context is stored in a separate database.
- **Interactive Chatbot**: Engage with a chatbot that remembers conversation history within each context.

## Project Structure

   ```bash
    Mistral-Internship-Project/
    │
    ├── .github/
    │   └── workflows/
    │       └── ci.yml          # Continuous integration
    │
    ├── data/                   # SQLite databases for each user
    │
    ├── Mistral/
    │   ├── __init__.py         # Initializes the Mistral package and sets up the FastAPI app.
    │   ├── models.py           # SQLAlchemy models for database tables
    │   ├── pydantic_models.py  # Pydantic models for request and response validation
    │   ├── routes.py           # API routes logic for handling requests
    │   └── templates/
    │       └── index.html      # UI HTML/Javascript
    │
    ├── tests/
    │   ├── functional/
    │   │   └── test_routes.py  # Functional tests for API routes
    │   ├── unit/
    │   │   └── test_model.py   # Unit tests for individual components
    │   ├── API_testing.py      # Initial script for testing the Mistral API
    │   └── conftest.py         # Configuration for pytest
    │
    ├── config.py               # Configuration file for env variables and settings
    ├── app.py                  # FastAPI application
    ├── Dockerfile              # Docker file of the application
    ├── docker-compose.yml      # Configuration for Docker Compose to run the app
    |
    ├── .gitignore
    ├── .dockerignore
    ├── requirements.txt
    └── README.md
```

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/Mistral-Internship-Project.git
   cd Mistral-Internship-Project
   ```

2. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your Mistral API key:

   ```
   MISTRAL_API_KEY=your_api_key_here
   ```

3. **Build the Docker Image**

   ```bash
   docker build -t mistral-internship-project .
   ```

4. **Run the Docker Container**

   ```bash
   docker compose up
   ```
   Open your browser and go to `http://0.0.0.0:8000`.

## Installation (Without Docker)

1. **Set Up a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your Mistral API key:

   ```
   MISTRAL_API_KEY=your_api_key_here
   ```

4. **Start the Server**

   ```bash
   uvicorn app:app --reload
   ```
   Open your browser and go to `http://localhost:8000`.


## Testing
Tests are run automatically by continuous integration. They include unit and functional tests using pytest. The repository is also linted using flake8. To test either, run the CI GHA or locally:

1. **Run Tests**

   Use `pytest` to run the test suite:

   ```bash
   PYTHONPATH=. pytest tests/
   ```

2. **Linting**

   Use `flake8` to check for style issues:

   ```bash
   flake8 .
   ```

## CI/CD

The project uses GitHub Actions for continuous integration. The workflow is defined in `.github/workflows/ci.yml` and includes steps for testing and linting.

## Usage

- **Chat with the Bot**: Start a conversation by typing in the input box.
- **Switch Contexts**: Use the dropdown to switch between different conversation contexts or create a new one.
- **Persistent Conversations**: Each context maintains its own conversation history.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.