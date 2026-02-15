import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ================= CONFIG =================
# Option 1: Use environment variables (recommended for security)
API_KEY = os.getenv("TRELLO_API_KEY", "")
TOKEN = os.getenv("TRELLO_TOKEN", "")
BOARD_ID = os.getenv("TRELLO_BOARD_ID", "")

# Option 2: Hardcode for quick testing (not recommended for GitHub)
# API_KEY = "your_api_key_here"
# TOKEN = "your_token_here"  
# BOARD_ID = "your_board_id_here"

JSON_FILE = "learning_plan.json"  # Your JSON file

# Validate credentials
if not API_KEY or not TOKEN or not BOARD_ID:
    print("❌ Error: Missing Trello credentials!")
    print("Please set TRELLO_API_KEY, TRELLO_TOKEN, and TRELLO_BOARD_ID")
    print("Either in a .env file or as environment variables.")
    exit(1)
# =========================================

# Load JSON learning plan
with open(JSON_FILE, "r") as f:
    data = json.load(f)

# Assign Trello list names based on type
for course in data.get("courses", []):
    course['trello_list'] = "Courses"

for project in data.get("projects", []):
    project['trello_list'] = "Projects"

# Combine for processing
tasks = data.get("courses", []) + data.get("projects", [])

# Get all lists on the board
lists_url = f"https://api.trello.com/1/boards/{BOARD_ID}/lists"
lists_res = requests.get(lists_url, params={'key': API_KEY, 'token': TOKEN}).json()
list_map = {lst['name']: lst['id'] for lst in lists_res}

# Function to create a list if it doesn't exist
def get_or_create_list(list_name):
    if list_name in list_map:
        return list_map[list_name]
    create_url = f"https://api.trello.com/1/boards/{BOARD_ID}/lists"
    create_res = requests.post(create_url, params={'key': API_KEY, 'token': TOKEN, 'name': list_name}).json()
    list_id = create_res.get('id')
    list_map[list_name] = list_id
    print(f"Created new list: {list_name}")
    return list_id

# Process each task
for task in tasks:
    list_id = get_or_create_list(task['trello_list'])

    # Append dependencies info to description if exists
    desc = task.get('desc', '')
    if 'depends_on' in task:
        desc += "\n\nDependencies:\n- " + "\n- ".join(task['depends_on'])

    # Add the learning stage (To Learn / Learning / Mastered)
    desc += f"\n\nLearning Stage: {task.get('list', 'To Learn')}"

    # Create Trello card
    card_res = requests.post(
        "https://api.trello.com/1/cards",
        params={
            'key': API_KEY,
            'token': TOKEN,
            'idList': list_id,
            'name': task['name'],
            'desc': desc,
            'due': task.get('due', None)
        }
    ).json()

    card_id = card_res.get('id')
    if not card_id:
        print(f"Failed to create card: {task['name']}")
        continue
    print(f"Created card: {task['name']}")

    # Add checklist if exists
    if 'checklist' in task and card_id:
        checklist_res = requests.post(
            f"https://api.trello.com/1/cards/{card_id}/checklists",
            params={'key': API_KEY, 'token': TOKEN, 'name': 'Steps'}
        ).json()
        checklist_id = checklist_res.get('id')
        for item in task['checklist']:
            requests.post(
                f"https://api.trello.com/1/checklists/{checklist_id}/checkItems",
                params={'key': API_KEY, 'token': TOKEN, 'name': item}
            )

print("All cards processed successfully!")
