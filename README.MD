### To start project 
#### Step 1. create virtual env 

1. Navigate to Your Project Folder
``` bash
cd /path/to/your/project
```

2. Create the Virtual Environment: Run the following command to create a venv directory in your project folder:
``` bash
python3 -m venv venv
```
---
#### Step 2: Activate the Virtual Environment
- macOS/Linux:
``` bash
source venv/bin/activate
```

- windows
``` bash
.\venv\Scripts\activate
```
---
#### Step 3: Install Dependencies
1. Upgrade pip (optional but recommended):
``` bash
pip install --upgrade pip
```

2. Install Required Packages: For example:
``` bash
pip install requests
```

3. Freeze Dependencies (optional): Create a requirements.txt file for your project:
``` bash
pip freeze > requirements.txt
```

---

#### Step 4: Deactivate the Virtual Environment
When you are done working in the virtual environment, deactivate it:
``` bash
deactivate
```