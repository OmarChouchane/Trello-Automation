# 🚀 DevOps Learning Path Automation with Trello

## 📖 The Problem

As I embarked on my DevOps journey, I faced a common but overwhelming challenge: **too many courses, certifications, and projects to track**.

My learning plan included:

- 9+ certification courses (Terraform, Kubernetes, CKAD, GitHub Actions, ArgoCD, Prometheus, Istio)
- 4+ hands-on AWS/Kubernetes projects
- Complex dependencies between courses and projects
- Checklists for each learning module
- Different learning stages (To Learn, Learning, Mastered)

Managing all of this manually in Trello was time-consuming and error-prone. Every time I updated my learning plan, I had to:

- ✋ Manually create each card
- ✋ Copy/paste descriptions and checklists
- ✋ Track dependencies between courses
- ✋ Organize cards into the right lists

**This was taking away valuable time from actual learning!**

## 💡 The Solution

I built a simple Python automation script that transforms a structured JSON learning plan into organized Trello cards automatically.

### What It Does

✅ **Reads a JSON learning plan** with courses and projects  
✅ **Automatically creates Trello cards** with descriptions, checklists, and due dates  
✅ **Organizes cards into lists** (Courses, Projects, custom lists)  
✅ **Tracks dependencies** between courses and projects  
✅ **Adds learning stages** (To Learn, Learning, Mastered)  
✅ **Creates checklists** for step-by-step learning

### Time Saved

- **Before:** 30-45 minutes to set up a complete learning board
- **After:** 10 seconds to run the script

---

## 🎯 My DevOps Learning Path

This automation manages my comprehensive DevOps learning journey that includes:

### Certifications & Courses

- **Terraform** (Basics + Associate Certification)
- **Kubernetes** (Basics + CKAD Certification)
- **Helm** (Package Management)
- **GitHub Actions** (CI/CD Automation)
- **GitOps with ArgoCD**
- **Prometheus** (Monitoring + PCA Certification)
- **Istio Service Mesh**

### Hands-On Projects

1. **AWS 3-Tier Architecture with Terraform**
2. **Dynamic Web Application on AWS**
3. **Production-Ready EKS Cluster**
4. **EKS Microservices with Prometheus & Grafana**

---

## 🛠️ How It Works

### Prerequisites

- Python 3.x
- Trello account
- Trello API credentials (API Key & Token)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/OmarChouchane/trello-automation.git
   cd trello-automation
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Trello credentials**

   Create a `.env` file (or edit the script directly):

   ```env
   TRELLO_API_KEY=your_api_key_here
   TRELLO_TOKEN=your_token_here
   TRELLO_BOARD_ID=your_board_id_here
   ```

   **Get your Trello credentials:**
   - API Key: Visit [Trello API Key](https://trello.com/power-ups/admin)
   - Token: Generate from the same page
   - Board ID: Find it in your board URL: `https://trello.com/b/BOARD_ID/board-name`

### Usage

1. **Customize your learning plan** in `learning_plan.json`
2. **Run the automation**
   ```bash
   python create_trello_cards.py
   ```
3. **Watch your Trello board populate automatically!** 🎉

---

## 📄 JSON Structure

The `learning_plan.json` follows this structure:

```json
{
  "courses": [
    {
      "id": "course_id",
      "name": "Course Name",
      "desc": "Course description",
      "list": "To Learn",
      "checklist": ["Task 1", "Task 2"]
    }
  ],
  "projects": [
    {
      "name": "Project Name",
      "desc": "Project description",
      "list": "To Learn",
      "depends_on": ["course_id"],
      "checklist": ["Step 1", "Step 2"]
    }
  ]
}
```

---

## 🎓 Key Features

### 1. **Automatic List Creation**

The script detects if lists exist and creates them if needed:

- Courses → "Courses" list
- Projects → "Projects" list

### 2. **Dependency Tracking**

Projects can depend on courses or other projects:

```json
"depends_on": ["terraform_basics", "kubernetes_basics"]
```

### 3. **Interactive Checklists**

Each card gets a checklist for tracking progress:

```json
"checklist": [
  "Install Terraform",
  "Create resources",
  "Practice state commands"
]
```

### 4. **Learning Stages**

Track your progress with stages:

- 📚 **To Learn** - Not started yet
- 📖 **Learning** - Currently working on it
- ✅ **Mastered** - Completed and understood

---

## 🌟 Results & Impact

### Before

- Disorganized learning materials
- Unclear dependencies
- Manual tracking overhead
- Lost motivation due to complexity

### After

- ✅ Clear visual roadmap in Trello
- ✅ Automated setup in seconds
- ✅ Easy to update and maintain
- ✅ More time for actual learning
- ✅ Better progress tracking

---

## 🔮 Future Enhancements

- [ ] Add due date suggestions based on estimated learning time
- [ ] Integrate with Notion or other project management tools
- [ ] Add progress analytics and reporting
- [ ] Support for recurring tasks and reviews
- [ ] Add labels for difficulty levels
- [ ] Integration with calendar apps

---

## 🤝 Contributing

Feel free to fork this repository and customize it for your own learning journey! If you have suggestions or improvements, pull requests are welcome.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 About Me

I'm on a journey to master DevOps engineering, and I believe in **automating repetitive tasks** to focus on what matters: learning and building.

If this helped you organize your learning path, give it a ⭐️!

**Connect with me on LinkedIn:** [Linkedin](https://www.linkedin.com/in/omar-chouchane/)

---

## 🏷️ Tags

`#DevOps` `#Automation` `#Python` `#Trello` `#Terraform` `#Kubernetes` `#AWS` `#LearningPath` `#Productivity` `#100DaysOfDevOps`
