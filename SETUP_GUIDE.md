# 🚀 Quick Setup Guide

Follow these steps to set up your GitHub repository and push your code.

## Step 1: Create Your .env File

Create a file named `.env` in the project root with your Trello credentials:

```bash
TRELLO_API_KEY=your_actual_api_key
TRELLO_TOKEN=your_actual_token
TRELLO_BOARD_ID=your_actual_board_id
```

**⚠️ Important:** The `.env` file is already in `.gitignore`, so your credentials won't be pushed to GitHub!

## Step 2: Initialize Git Repository

Open a terminal in your project folder and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create your first commit
git commit -m "Initial commit: DevOps Learning Path Automation"
```

## Step 3: Create GitHub Repository

1. Go to [https://github.com/new](https://github.com/new)
2. Name your repository (e.g., `devops-learning-automation` or `trello-automation`)
3. Choose **Public** (to share with LinkedIn)
4. **DO NOT** initialize with README (you already have one)
5. Click "Create repository"

## Step 4: Push to GitHub

GitHub will show you commands, but here's what you need:

```bash
# Add your GitHub repository as remote (replace with YOUR repository URL)
git remote add origin https://github.com/yourusername/your-repo-name.git

# Push your code
git branch -M main
git push -u origin main
```

## Step 5: Verify

1. Refresh your GitHub repository page
2. You should see all your files (except .env which is ignored)
3. README.md should display on the main page

## Step 6: Share on LinkedIn

1. Copy your repository URL (e.g., `https://github.com/yourusername/repo-name`)
2. Use the LinkedIn post templates from `LINKEDIN_POST_TEMPLATE.md`
3. Add screenshots of your Trello board
4. Post and engage with comments!

---

## Optional: Add a Repository Description

On GitHub, click "About" (top right) and add:

- **Description:** "Python automation script that transforms a structured DevOps learning plan into organized Trello cards"
- **Website:** Your LinkedIn profile URL
- **Topics:** `python`, `automation`, `trello`, `devops`, `terraform`, `kubernetes`, `aws`, `learning`

---

## Optional: Add Repository Image

1. Take a screenshot of your organized Trello board
2. Go to repository Settings → scroll to "Social preview"
3. Upload your screenshot

This image will appear when you share your repo link!

---

## Next Steps

After posting on LinkedIn:

- Star your own repository ⭐
- Watch for issues and PRs from others
- Respond to comments on LinkedIn
- Consider writing a blog post about it

---

## Need Help?

### Common Issues:

**Issue:** `git: command not found`

- **Solution:** Install Git from [git-scm.com](https://git-scm.com/)

**Issue:** Authentication error when pushing

- **Solution:** Use a Personal Access Token instead of password
  - Go to GitHub Settings → Developer settings → Personal access tokens → Generate new token
  - Use the token as your password when prompted

**Issue:** Can't find .env file

- **Solution:** It's a hidden file. In Windows Explorer, enable "Show hidden files"

---

Good luck with your GitHub repo and LinkedIn post! 🚀

If this helped you, don't forget to star the repo and share your success story!
