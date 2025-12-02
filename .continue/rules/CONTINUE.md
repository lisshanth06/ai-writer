# AI Writer App Guide

## Project Overview

The AI Writer App is a tool designed to help writers research and edit their content. It provides a unified environment where writers can:

- Manage writing projects
- Gather information from various sources (text, web, audio)
- Use AI assistance for content generation and editing
- Organize research materials

### Key Technologies
- **Frontend**: FastHTML framework
- **AI Components**: Langchain/Langgraph framework
- **Backend**: Python
- **Database**: Sqlite (SQL DB), Qdrant (Vector DB in local mode to persist vector information)

### High-level Architecture
The application follows a web-based architecture with AI integration:
- Web interface for user interactions
- AI processing backend for content generation and analysis
- Data storage for projects, sources, and documents

## Getting Started

### Prerequisites
- Python 3.10+ 
- Required packages (install via uv):
  - langchain/langgraph
  - django

### Installation Instructions
This project uses `uv` for all operations

1. Clone the repository
2. Install the required dependencies:
   ```
   uv sync
   ```
3. Run the application:
   ```
   uv run main.py
   ```

### Important Commands

1. Install the required dependencies:
   ```
   uv sync
   ```
2. Run the application:
   ```
   uv run python .\manage.py runserver
   ```
3. Add a dependency:
   ```
   uv add <dependency>
   ```

### Basic Usage
1. Create a new project from the main screen
2. Add sources in the Sources tab (text paste, web search, or audio transcription)
3. Switch to the Document tab to write and edit with AI assistance
4. Use the chat interface to give instructions to the AI

## Project Structure

### Overview of Directories
- `/` - Root directory containing the main application files
- `/docs` - Documentation for the project
- [Additional directories may be present as development continues]

### Key Files
- `writerapp/` - All the source code for the application goes here

Ignore these files, they are temporary:
- `main.py`
- `api.py` - API endpoints (currently in development)
- `python_dict_to_json_str.py`
- `jsonstr_to_python_dict.py`
- `http_GET_request.py`
- `get_request.py`
- `python-json.py`
- `json-python.py`

### Important Configuration Files
- `README.md` - Brief project overview
- `docs/REQUIREMENTS.md` - Detailed requirements and application flow
- `docs/DESIGN.md` - Architecture and technology stack
- `docs/langgraph-llms.txt` - Context for agents on using the Langgraph framework

## Development Workflow

### Coding Standards
- Follow Python PEP 8 style guidelines
- Use descriptive variable and function names
- Document functions and modules with docstrings

### Testing Approach
- Implement unit tests for individual components using pytest
- Test the AI integration with different prompts and scenarios
- Test the web interface across different browsers

### Build and Deployment Process
[To be determined as the project matures]

### Contribution Guidelines
1. Fork the repository
2. Create a feature branch
3. Make changes and test
4. Submit a pull request with detailed description of changes

## Key Concepts

### Domain-specific Terminology
- **Project**: A writing project the user is working on
- **Sources**: Information sources the writer uses for reference:
  - Text Source: Pasted text content
  - Web Search: Information retrieved from web searches
  - Audio: Transcribed content from audio files
- **Document**: The actual content being created by the writer

### Core Abstractions
- Source management system
- Document editing interface
- AI-assisted writing and editing
- Chat-based interaction for commands

### Design Patterns
- Web application with client-server architecture
- AI agent integration for content processing
- Separation of UI (document view, sources management) from business logic

## Common Tasks

### Managing Sources
1. Navigate to the Sources tab
2. Click "Create Source" button
3. Select the source type (text, web search, or audio)
4. Add the content or search query
5. Save the source

### Using AI Assistance
1. In the Document tab, use the chat interface
2. Type instructions like:
   - "Generate an introduction and put it at the top"
   - "Rewrite paragraph 2 and make it shorter with simple language"
   - "When was Python created?" (for information queries)
3. The AI will respond based on the sources and make changes to the document as requested

### Editing Documents
1. Use the document editor on the right side of the Document tab
2. Make manual edits as needed
3. Click Save to preserve your changes

## Troubleshooting

### Common Issues
- If the AI responses are not relevant, check if appropriate sources have been added
- Ensure internet connectivity for web search sources
- Verify audio files are in supported formats for transcription

### Debugging Tips
- Check console logs for error messages
- Verify that all required dependencies are installed
- Restart the application if unexpected behavior occurs

## References

### Documentation
- [FastHTML Documentation](https://fastht.ml/docs/index.html)
- [Langchain Documentation](https://docs.langchain.com/)

### Important Resources
- Project requirements: See `docs/REQUIREMENTS.md`
- Architecture details: See `docs/DESIGN.md`

---

*Note: This guide is a living document and will be updated as the project evolves. Some sections may require verification or additional details as development progresses.*