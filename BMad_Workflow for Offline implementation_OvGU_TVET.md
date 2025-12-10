
# **AI-Powered Course Generator (Offline) — Full Step-by-Step Guide**

### *Using Python, Ollama & DeepSeek on macOS*

Author: **Masub Makhdoom**
Version: 1.0
Date: *Your date here*

---

## 🧭 **Introduction**

This guide teaches you how to create an **offline AI course generator** on macOS using:

* **Python 3.14**
* **Ollama** (offline AI engine)
* **DeepSeek-Coder** (local LLM)
* **Visual Studio Code**
* **YAML & Markdown automation script**

The system works fully offline after initial installation.

---

# **1. Install Required Tools**

---

## **1.1 Open Terminal**

Press:

```
Command (⌘) + Space → type “Terminal” → Enter
```

---

## **1.2 Install Homebrew (Package Manager)**

Run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Add Homebrew to PATH:

```bash
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/usr/local/bin/brew shellenv)"
```

Verify:

```bash
brew --version
```

---

## **1.3 Install Python, Git, and Ollama**

```bash
brew install python3 git ollama
```

Check versions:

```bash
python3 --version
git --version
ollama --version
```

Expected:

* Python 3.14.x
* Git 2.x
* Ollama 0.x

---

# **2. Install & Run the Offline AI Model**

---

## **2.1 Start Ollama Background Service**

```bash
brew services start ollama
```

Verify:

```bash
brew services list
```

Status should be:

```
ollama   started
```

---

## **2.2 Download DeepSeek Model**

```bash
ollama pull deepseek-coder
```

This will download ~700 MB–2 GB depending on the version.

---

# **3. Create Course Automation Project**

---

## **3.1 Create the Project Folder**

```bash
cd ~/Documents
mkdir CourseProjectTool
cd CourseProjectTool
```

---

## **3.2 Create Python Script File**

```bash
touch smart_course_project.py
open -a "Visual Studio Code" smart_course_project.py
```

---

# **4. Paste This Python Script Into the File**

Copy and paste **everything below** into `smart_course_project.py`:

```python
import subprocess
from pathlib import Path

BASE_PATH = Path.home() / "Documents" / "Mini_Workshop_Course_Development"
COURSE_NAME = "Mini Workshop Course Development"
MODEL = "deepseek-coder"

def ollama_generate(prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", MODEL],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8", errors="ignore")

def save_yaml(folder: str, filename: str, content: str):
    path = BASE_PATH / folder
    path.mkdir(parents=True, exist_ok=True)
    with open(path / filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] saved {folder}/{filename}")

def create_ai_course():
    sections = {
        "personality": "Define learners, tone, and course context.",
        "structure": "Outline units, structure, and sequence.",
        "activities": "List tasks, discussions, reflections.",
        "output": "Describe learning outcomes and assessment."
    }

    print(f"[AI] Generating course: {COURSE_NAME}\n")

    for section, desc in sections.items():
        filename = f"{section}.yaml"
        target_file = BASE_PATH / section / filename
        if target_file.exists():
            print(f"[skip] {section}.yaml already exists")
            continue
        prompt = f"Create a YAML file for the {section} part of a course titled '{COURSE_NAME}'. Focus on: {desc}."
        print(f"[AI] Generating {section}.yaml ...")
        content = ollama_generate(prompt)
        save_yaml(section, filename, content)

    summary_md = BASE_PATH / f"{COURSE_NAME.replace(' ', '_')}.md"
    prompt_summary = f"""
Generate a Markdown summary for '{COURSE_NAME}' including:
- Course description
- Learning objectives
- Section overview
- Expected outcomes
- Final message
"""
    print("[AI] Generating Markdown summary...")
    summary_content = ollama_generate(prompt_summary)

    with open(summary_md, "w", encoding="utf-8") as f:
        f.write(summary_content)

    print(f"\n✅ Course '{COURSE_NAME}' created at {BASE_PATH}")

if __name__ == "__main__":
    create_ai_course()
```

Save with:

```
⌘ + S
```

---

# **5. Generate the Course**

---

## **5.1 Open VS Code Terminal**

Inside VS Code:

```
View → Terminal
```

OR shortcut:

```
Ctrl + `
```

---

## **5.2 Run the Script**

```bash
python3 smart_course_project.py
```

---

## **5.3 Expected Output**

```
[AI] Generating personality.yaml ...
[OK] saved personality/personality.yaml
[AI] Generating structure.yaml ...
[OK] saved structure/structure.yaml
[AI] Generating activities.yaml ...
[OK] saved activities/activities.yaml
[AI] Generating output.yaml ...
[OK] saved output/output.yaml

[AI] Generating Markdown summary...
[OK] saved Mini_Workshop_Course_Development.md

✅ Course 'Mini Workshop Course Development' created at ~/Documents/Mini_Workshop_Course_Development
```

---

# **6. View Your Course Files**

Navigate to:

```
Finder → Documents → Mini_Workshop_Course_Development
```

You will see:

```
personality/personality.yaml
structure/structure.yaml
activities/activities.yaml
output/output.yaml
Mini_Workshop_Course_Development.md
```

---

# **7. Edit or Regenerate Sections**

---

## **7.1 Edit Manually**

Open any file:

```bash
open -a "Visual Studio Code" ~/Documents/Mini_Workshop_Course_Development/structure/structure.yaml
```

Edit → Save → Done.

---

## **7.2 Regenerate Only One Section**

Delete the file:

```bash
rm ~/Documents/Mini_Workshop_Course_Development/activities/activities.yaml
```

Re-run script:

```bash
python3 smart_course_project.py
```

It will regenerate ONLY missing files.

---

# **8. Create a New Course Easily**

Open your Python script:

```bash
open -a "Visual Studio Code" smart_course_project.py
```

Change the line:

```python
COURSE_NAME = "Quantitative Research Methods"
```

Save → Run:

```bash
python3 smart_course_project.py
```

A new folder will appear:

```
Documents/Quantitative_Research_Methods
```

---

# **9. Troubleshooting**

| Issue                 | Solution                                       |
| --------------------- | ---------------------------------------------- |
| `ollama not running`  | Run `brew services start ollama`               |
| `.md file is empty`   | Ensure summary section is pasted correctly     |
| Script prints nothing | File was empty → paste code and save           |
| Model downloads again | Don’t run `ollama serve`, keep service running |

---

# **10. Final Notes**

* This generator is fully offline
* You can create unlimited courses
* You can connect this YAML → LiaScript → SCORM
* Ideal for TVET, university, microcredentials

---

If you want this turned into a **LiaScript interactive course**, **SCORM package**, or **GitHub classroom template**, just tell me!
