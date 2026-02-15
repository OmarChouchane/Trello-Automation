# 🤝 Contributing to DevOps Learning Path Automation

First off, thank you for considering contributing to this project!

## How Can I Contribute?

### 🐛 Reporting Bugs

If you find a bug, please create an issue with:

- A clear, descriptive title
- Steps to reproduce the problem
- Expected behavior vs actual behavior
- Your environment (OS, Python version)
- Screenshots if applicable

### 💡 Suggesting Enhancements

Have an idea? Create an issue with:

- A clear description of the enhancement
- Why it would be useful
- Possible implementation approach

### 🔧 Pull Requests

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes**
4. **Test your changes**
5. **Commit** with clear messages (`git commit -m 'Add amazing feature'`)
6. **Push to your branch** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request**

## Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/trello-automation.git
cd trello-automation

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your credentials
cp .env.example .env
# Edit .env with your Trello credentials

# Run the script
python create_trello_cards.py
```

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Keep functions small and focused

## Enhancement Ideas

Looking for something to work on? Here are some ideas:

### Easy

- [ ] Add support for card colors/labels
- [ ] Add progress bar during card creation
- [ ] Better error messages
- [ ] Add command-line arguments

### Medium

- [ ] Support for multiple boards
- [ ] Export Trello board back to JSON
- [ ] Add due date suggestions based on course length
- [ ] Integration with other tools (Notion, Monday.com)

### Advanced

- [ ] Web UI for managing learning plans
- [ ] Progress tracking and analytics
- [ ] Automated reminders via email/Slack
- [ ] AI-powered learning path recommendations

## Questions?

Feel free to open an issue with the "question" label!

---

Thank you for contributing! 🙌
