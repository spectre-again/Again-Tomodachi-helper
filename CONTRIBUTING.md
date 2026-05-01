# Contributing to Again-Tomodachi Helper

We love your input! We want to make contributing to this project as easy and transparent as possible.

## Development Setup

### Prerequisites
- Node.js v16+
- Python 3.8+
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/spectre-again/Again-Tomodachi-helper.git
   cd Again-Tomodachi-helper
   ```

2. **Set up backend**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   ```

3. **Set up frontend**
   ```bash
   cd frontend
   npm install
   ```

4. **Configure environment**
   - Update `.env` with your settings
   - For GitHub integration, add your GitHub Personal Access Token

5. **Run both services**
   ```bash
   # Terminal 1 - Backend
   python -m backend.main

   # Terminal 2 - Frontend
   npm run dev
   ```

## Code Style

### Python
- Follow PEP 8 guidelines
- Use type hints where possible
- Document functions with docstrings

### JavaScript/React
- Use ES6+ syntax
- Follow Airbnb style guide
- Use meaningful variable names
- Comment complex logic

## Commit Messages

- Use clear, descriptive commit messages
- Start with a verb: "Add", "Fix", "Update", etc.
- Reference issues when applicable: "Fixes #123"

## Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and commit: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a Pull Request with a clear description

## Testing

- Test your changes locally before submitting
- Ensure no console errors
- Test on different screen sizes

## Reporting Bugs

Use GitHub Issues with:
- Clear title
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if relevant

## Feature Requests

- Use GitHub Issues with label "enhancement"
- Describe the use case
- Explain the benefit

## Questions?

Feel free to open an issue or contact the maintainers.

Happy coding! 🚀
