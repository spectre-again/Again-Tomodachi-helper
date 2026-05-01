# Again-Tomodachi Helper 🐱

A task management system with a Tamagotchi twist! Track your tasks, monitor progress, and automatically share completed work with your team through GitHub integration.

## Features

- 📋 **Task Management Interface** - Create, update, and track tasks in real-time
- 📊 **Progress Feed** - Visual dashboard showing task progress and completion status
- 🤖 **Smart Helper** - Automated task tracking and workflow management
- 📁 **GitHub Integration** - Automatically commit completed task results to a repository
- 💾 **Data Persistence** - Track task history and performance metrics
- 🎮 **Gamified Experience** - Tamagotchi-style pet that reflects your productivity

## Project Structure

```
Again-Tomodachi-helper/
├── frontend/              # React/Vue web application
├── backend/               # Node.js/Python API server
├── database/              # Database schemas and migrations
├── docs/                  # Documentation
└── config/                # Configuration files
```

## Quick Start

### Prerequisites
- Node.js (v16+)
- Python (v3.8+)
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/spectre-again/Again-Tomodachi-helper.git
cd Again-Tomodachi-helper

# Install dependencies
npm install
pip install -r requirements.txt
```

### Running the Application

```bash
# Start the backend server
python -m backend.main

# In another terminal, start the frontend
npm run dev
```

## Usage

### Creating a Task

1. Navigate to the main page
2. Click "New Task"
3. Fill in task details (title, description, deadline)
4. Assign priority level
5. Submit

### Tracking Progress

- View all tasks in the main feed
- Check progress percentage for each task
- See completed tasks move to "Finished" section

### Submitting Results

- Upon task completion, you'll be prompted to upload related files
- Files are automatically committed to the repository
- Your team can review and access all completed work

## Configuration

Create a `.env` file in the root directory:

```env
GITHUB_TOKEN=your_token_here
GITHUB_REPO=spectre-again/Again-Tomodachi-helper
DATABASE_URL=sqlite:///tasks.db
API_PORT=5000
```

## API Endpoints

- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/:id` - Update task
- `DELETE /api/tasks/:id` - Delete task
- `GET /api/feed` - Get task progress feed
- `POST /api/tasks/:id/complete` - Mark task as complete and submit files

## Database Schema

See `database/schema.sql` for the complete schema.

## Contributing

1. Create a feature branch
2. Make your changes
3. Submit a pull request

## License

MIT

## Author

[spectre-again](https://github.com/spectre-again)
