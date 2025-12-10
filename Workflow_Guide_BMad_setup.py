#!/usr/bin/env python3
"""
Complete Teaching Workflow Generator
Creates all files (.yaml, .md, etc.) for the BMad-Method teaching workflow

Usage:
    python complete_workflow_generator.py
    
This will create a 'teaching-workflow-files' directory with all necessary files.
"""

import os
import zipfile
from pathlib import Path
from datetime import datetime

def create_file_structure():
    """Create complete file structure with all templates and definitions"""
    
    base_dir = Path("teaching-workflow-files")
    
    # Define all files and their contents
    files = {
        # ===== TEMPLATES =====
        "templates/lecture-outline-template.yaml": """template:
  id: lecture-outline-template
  name: "Lecture Outline"
  version: 1.0
  output:
    format: markdown
    filename: docs/lecture-outline.md
  title: "Lecture Outline"
  sections:
    - id: title
      title: Title
      template: "Name of the lecture or course"
    - id: audience
      title: Target Audience
      template: "Who is this course/lecture for?"
    - id: time-commitment
      title: Time Investment
      template: "Estimated time investment (e.g., semester hours, total hours)"
    - id: abstract
      title: Summary
      template: >
        Detailed abstract covering all topics,
        demonstrating benefits & applications.
    - id: learning-goals
      title: Learning Objectives
      template: >
        List of 3-5 clear learning objectives with application scenarios.
    - id: logo
      title: Logo (optional)
      template: >
        Prompt for creating a logo for the lecture.
""",

        "templates/lecture-didactics-template.yaml": """template:
  id: lecture-didactics-template
  name: "Lecture Didactics & Style"
  version: 1.0
  output:
    format: markdown
    filename: docs/lecture-didactics.md
  title: "Lecture Didactics & Style"
  inputs:
    - docs/lecture-outline.abstract
    - docs/lecture-outline.audience
    - docs/lecture-outline.time-commitment
    - docs/lecture-outline.learning-goals
  sections:
    - id: didactic-concept
      title: Didactic Concept
      template: "Teaching methods, learning phases, pedagogical considerations."
    - id: professor-persona
      title: Professor Persona
      template: "Description of the professor (background, expertise, role)."
    - id: style
      title: Style & Difficulty Level
      template: "Description (e.g., humorous, academic, practice-oriented)."
    - id: course-type
      title: Course Type
      template: "Type of course (introduction, advanced, practice-oriented, group work, self-study)."
""",

        "templates/lecture-agenda-template.yaml": """template:
  id: lecture-agenda-template
  name: "Lecture Agenda"
  version: 1.0
  output:
    format: markdown
    filename: docs/lecture-agenda.md
  title: "Lecture Agenda"
  inputs:
    - docs/lecture-outline.learning-goals
    - docs/lecture-outline.time-commitment
    - docs/lecture-didactics.didactic-concept
    - docs/lecture-didactics.course-type
  sections:
    - id: overview
      title: Overview
      template: "Brief overview of agenda, learning objectives, didactics & course type."
    - id: modules
      title: Modules / Sessions
      template: >
        Each session contains:
        - Title, duration, type (lecture/exercise)
        - Learning objective(s), summary
        - Automatic materials file (materials/{n}-{type}.md)
""",

        "templates/session-skeleton.yaml": """template:
  id: session-skeleton
  name: "Session Skeleton"
  version: 1.0
  output:
    format: markdown
    filename: skeletons/{{number}}-{{type}}.md
  title: "Session {{number}} ({{type | title}})"
  sections:
    - id: title
      title: Title
      template: "Session {{number}} – {{title}} ({{type | title}})"
    - id: summary
      title: Summary
      template: "Brief overview, connection to agenda, relevance, didactics."
    - id: content
      title: Content
      template: "Placeholder for main topics or assignments."
    - id: activities
      title: Activities
      template: "Placeholder for exercises, discussions, reflection."
    - id: references
      title: References & Sources
      template: "List of relevant sources and materials."
""",

        "templates/session-material.yaml": """template:
  id: session-material
  name: "Session Material"
  version: 1.0
  output:
    format: markdown
    filename: materials/{{number}}-{{type}}.md
  title: "Session {{number}} ({{type | title}})"
  inputs:
    - docs/lecture-agenda.modules
    - docs/lecture-didactics.style
    - docs/lecture-didactics.course-type
    - docs/lecture-didactics.professor-persona
  sections:
    - id: outline
      title: Planned Structure
      template: |
        # {{title}}

        Summary

        ## Introduction
        Content
        References

        ## Main Part 1
        Content
        References

        ## Main Part 2
        Content
        References

        ## Summary / Wrap-up
        Content
        References
""",

        # ===== TASKS =====
        "tasks/create-outline.md": """# Task: create-outline

## Purpose
Creates the **Lecture Outline** as starting point for a lecture.
Defines title, audience, abstract, learning objectives and optional logo.

## Inputs
- Lecture title
- Target audience (e.g., students, professionals, beginners)
- Time commitment (e.g., semester hours, total hours)
- Abstract (topics, content, benefits)
- Learning objectives (3-5 concrete goals)
- Logo (optional, as prompt)

## Output
- `docs/lecture-outline.md` (Markdown file)
- Structure based on `lecture-outline-template.yaml`

## Steps
1. Capture title, audience, time commitment and abstract
2. Define 3-5 concrete learning objectives
3. Optional: Add logo prompt
4. Fill template `lecture-outline-template.yaml` with inputs
5. Save file as `docs/lecture-outline.md`
""",

        "tasks/create-didactics.md": """# Task: create-didactics

## Purpose
Creates the **Lecture Didactics & Style** document.
Defines pedagogical concept, professor persona, style and course type.
Builds on Lecture Outline to ensure consistent teaching strategy.

## Inputs
- Summary from `docs/lecture-outline.md`
- Target audience from `docs/lecture-outline.md`
- Learning objectives from `docs/lecture-outline.md`

## Output
- `docs/lecture-didactics.md` (Markdown file)
- Structure based on `templates/lecture-didactics-template.yaml`

## Steps
1. Read abstract, audience, time commitment and learning objectives from outline
2. Design appropriate didactic concept (teaching methods, learning phases)
3. Describe professor persona (expertise, role, style)
4. Define style & difficulty level (humorous, academic, practice-oriented, etc.)
5. Determine course type (introduction, scientifically advanced, application-oriented, group work, self-study)
6. Fill template `templates/lecture-didactics-template.yaml` with results
7. Save file as `docs/lecture-didactics.md`
""",

        "tasks/create-agenda.md": """# Task: create-agenda

## Purpose
Creates the **Lecture Agenda** as structured course plan.
Defines sessions/modules with title, duration, type, objectives, summary and materials files.
**Agent additionally adopts professor persona and style from `docs/lecture-didactics.md`**.

## Inputs
- Learning objectives from `docs/lecture-outline.md`
- Abstract from `docs/lecture-outline.md`
- Time commitment from `docs/lecture-outline.md`
- Didactic concept from `docs/lecture-didactics.md`
- **Professor persona from `docs/lecture-didactics.md` (mandatory handoff)**
- **Style & difficulty from `docs/lecture-didactics.md` (mandatory handoff)**
- Course type from `docs/lecture-didactics.md`

## Output
- `docs/lecture-agenda.md` (Markdown file)
- Structure based on `templates/lecture-agenda-template.yaml`

## Steps
1. Read learning objectives from outline
2. Adopt didactic concept and course type from didactics
3. **Agent adopts professor persona & style from didactics into its own persona**
   - From this step, agent writes in professor persona tone
   - All agenda descriptions reflect this style
4. Define sessions/modules
5. Build agenda in structured form
6. Fill template `templates/lecture-agenda-template.yaml` with results
7. Save file as `docs/lecture-agenda.md`
""",

        "tasks/create-session-skeleton.md": """# Task: create-session-skeleton

## Purpose
Creates a **Session Skeleton** (lecture or exercise) as structured foundation.
**Agent adopts professor persona and style from didactics**.

## Inputs
- number: Session number
- type: Session type (`lecture` or `exercise`)
- title (optional)
- Didactic concept from `docs/lecture-didactics.md`
- **Professor persona from `docs/lecture-didactics.md` (mandatory handoff)**
- **Style & difficulty from `docs/lecture-didactics.md` (mandatory handoff)**

## Output
- `skeletons/{number}-{type}.md` (Markdown file)
- Structure based on `templates/session-skeleton.yaml`

## Steps
1. Capture session number, type and optional title
2. Adopt didactic concept and course type from didactics
3. **Agent adopts professor persona & style from didactics**
4. Generate basic structure for session
5. Fill template `templates/session-skeleton.yaml`
6. Save file
""",

        "tasks/promote-session.md": """# Task: promote-session

## Purpose
Converts a **Session Skeleton** into detailed **Session Material**.
**Agent adopts professor persona from didactics**.

## Inputs
- number, type
- skeleton: File from `skeletons/`
- didactics: Content from `docs/lecture-didactics.md`
- agenda: Content from `docs/lecture-agenda.md`
- **Professor persona from `docs/lecture-didactics.md` (mandatory handoff)**
- **Style & difficulty from `docs/lecture-didactics.md` (mandatory handoff)**

## Output
- `materials/{number}-{type}.md`
- Structure based on `templates/session-material.yaml`

## Steps
1. Load skeleton
2. Adopt didactic concept and course type from didactics
3. **Agent adopts professor persona & style from didactics**
4. Insert agenda info
5. Consider didactic inputs
6. Generate planned structure
7. Apply template
8. Save file
""",

        "tasks/coauthor-materials.md": """# Task: coauthor-materials

## Purpose
Enables agent **in professor persona** to co-author lecture materials creation and refinement.
This task is **interactive**: educators discuss content, tone and structure with agent
before incorporating into materials.

Suggest images for visualization, either as search term or concrete image prompt.
Images can be inserted as diagrams (e.g., Mermaid, ASCII-Art).

**IMPORTANT:** Strictly follow LiaScript syntax rules, especially for headings
and slide structure (see `data/liascript-cheat-sheet.md`).

## Inputs
- Professor persona & style from `docs/lecture-didactics.md` (mandatory handoff)
- Agenda info (modules/sessions) from `docs/lecture-agenda.md`
- Currently open document `materials/{number}-{type}.md`
- Associated skeleton `skeletons/{number}-{type}.md` if applicable
- Didactic inputs from `docs/lecture-didactics.md`
- Open questions or ideas from educators (discussion points)

## Output
- LiaScript / Markdown using syntax from `data/liascript-cheat-sheet.md`
- Suggestions & text blocks to incorporate into `materials/{number}-{type}.md`
- Revised sections in persona style
- Image prompts or text diagrams if applicable

## Steps
1. Agent loads agenda info, skeleton and didactics persona
2. **Agent adopts professor persona into its own persona** and writes, discusses,
   comments in this character's tone
3. Educators pose questions, objections or change requests
4. Agent responds in persona style, suggests alternatives and refines content iteratively
5. **Important:** Add new headings **only** when inside HTML blocks, lists or blockquotes
   (**Exception:** when educators explicitly want this or slides should be split)
6. Result is consolidated material version (or sections) to incorporate
   into current open document `materials/{number}-{type}.md`

## Special Features
- This task is **dialog-oriented** and remains open until educators "approve" materials
- Goal is **co-authoring**: Agent writes _with_, not _instead of_
- Outputs are intermediate steps approved by educators and incorporated
  into current open document `materials/{number}-{type}.md`

## Fuzzy Matching
- Only provide answers with 85% confidence threshold
- Show numbered list if unsure
- Research online if necessary
- Always ask if information is missing
- STAY IN CHARACTER!
""",

        "tasks/validate-lecture.md": """# Task: validate-lecture

## Purpose
Checks consistency and completeness of all lecture documents based on didactics
and checklist.

## Output
- `docs/validation-report.md`

## Steps
1. Load and use structure from `checklists/lecture-quality-checklist.md`
2. Check outline
3. Check didactics
4. Check agenda
5. Check session skeletons
6. Check materials
7. Generate report with findings
""",

        "tasks/assemble-bundle.md": """# Task: assemble-bundle

## Purpose
Assembles all lecture documents into a complete package.

## Output
- `lecture-bundle/` directory or `.zip` file

## Steps
1. Collect all documents from docs/, skeletons/, materials/
2. Build organized structure
3. Create index file `bundle-index.md` with table of contents
4. Bundle everything into distributable format
""",

        # ===== CHECKLISTS =====
        "checklists/lecture-quality-checklist.md": """# Checklist: Lecture Quality

## Outline
- [ ] Title present
- [ ] Target audience clearly defined
- [ ] Time commitment specified
- [ ] Summary complete
- [ ] Learning objectives formulated (3-5)
- [ ] Optional: Logo prompt included

## Didactics
- [ ] References outline content
- [ ] Didactic concept clear and detailed
- [ ] Professor persona defined
- [ ] Style & difficulty level specified
- [ ] Course type established

## Agenda
- [ ] Learning objectives adopted from outline
- [ ] Sessions complete with:
  - [ ] Title
  - [ ] Duration
  - [ ] Type (lecture/exercise)
  - [ ] Learning objective(s)
  - [ ] Summary
  - [ ] Materials file path

## Session Skeletons
- [ ] Exist for all planned sessions
- [ ] Contain all required sections:
  - [ ] Title
  - [ ] Summary
  - [ ] Content outline
  - [ ] Activities
  - [ ] References

## Session Materials
- [ ] All skeletons promoted to materials
- [ ] Detailed structure with sub-chapters
- [ ] References included per section
- [ ] Didactic inputs considered
- [ ] LiaScript syntax correct
- [ ] Animation sequences logical

## Overall Consistency
- [ ] Outline ↔ Didactics ↔ Agenda ↔ Sessions consistent
- [ ] No sessions without materials
- [ ] Numbering scheme correct
- [ ] Markdown format uniform across files
- [ ] Professor persona maintained throughout
- [ ] All learning objectives covered in materials
""",

        # ===== DATA =====
        "data/liascript-cheat-sheet.md": """# LiaScript Quick Reference Guide

## Course Metadata (Header)

Every LiaScript course must start with metadata in HTML comments:

```lia
<!--
author:   Your Name
email:    your.email@example.com
version:  1.0.0
language: en
narrator: English Female
comment:  Brief course description
-->
```

**Fields:**
- `author`: Course creator name
- `email`: Contact email
- `version`: Semantic versioning (1.0.0)
- `language`: Language code (en, de, fr, etc.)
- `narrator`: Text-to-speech voice
- `comment`: Short course description

## Structure: Headings & Slides

```lia
# Course Title (Main Title - Use Once)
## Section 1 (Creates a new slide)
### Subsection (Only inside containers!)
```

**Rules:**
- `#` = Course title (use exactly once)
- `##` = New slide (each creates a separate slide)
- `###` to `######` = Sub-headings (ONLY inside HTML blocks, lists, or blockquotes)

**CRITICAL:** Never use sub-headings directly in slide content. Always wrap them:

```lia
## Slide Title

<div>
### This is allowed inside a div
Content here...
</div>

- List item
  - ### This is allowed in a list
```

## Animations & Narration

Control when content appears and what the narrator says:

```lia
## My Slide

    --{{0}}--
This text will be read aloud when the slide first loads.

      {{0}}
This content appears at step 0 (immediately).

    --{{1}}--
This will be read when the user advances to step 1.

      {{1}}
This content appears at step 1.

      {{2-3}}
This appears at step 2 and disappears at step 3.
```

**Key Points:**
- `--{{n}}--` = Narrator text for step n (indented with 4 spaces)
- `{{n}}` = Content appears at step n (indented with 6 spaces)
- `{{a-b}}` = Content visible from step a to b
- Numbering resets with each new `##` slide

## Text Formatting

```lia
Normal text

**Bold text**

*Italic text*

***Bold and italic***

> Blockquote / Important note

~~Strikethrough~~
```

## Lists

```lia
Unordered list:
- Item 1
- Item 2
  - Nested item

Ordered list:
1. First
2. Second
3. Third
```

## Links & Media

```lia
[Link text](https://example.com)

![Image alt text](path/to/image.jpg "Optional caption")

?[Audio title](path/to/audio.mp3 "Optional caption")

!?[Video title](https://youtube.com/watch?v=VIDEO_ID "Optional caption")

??[oEmbed content](https://example.com/resource)
```

**Media Gallery:** Place multiple media items consecutively to create a gallery.

## Code Blocks

````lia
```python
def hello_world():
    print("Hello, World!")
```
````

**Executable Code:**

````lia
```python
x = 5 + 3
print(x)
```
<script>
@input
</script>
````

## Diagrams

**Mermaid Diagrams:**

````lia
```mermaid @mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
````

**ASCII Art:**

````lia
```ascii
  +---+      +---+
  | A | *--> | B |
  +---+      +---+
```
````

## Mathematical Formulas

Inline: `$E = mc^2$`

Block:
```lia
$$
\sum_{i=1}^{n} i = \frac{n(n+1)}{2}
$$
```

## Quizzes & Interactions

**Single Choice:**

```lia
What is 2 + 2?

- [( )] 3
- [(X)] 4  (X marks correct answer)
- [( )] 5
```

**Multiple Choice:**

```lia
Select all prime numbers:

- [[X]] 2
- [[ ]] 4
- [[X]] 5
- [[ ]] 6
```

**Text Input:**

```lia
Who wrote "Hamlet"?

[[Shakespeare]]
```

**Free Text:**

```lia
Explain the concept:

[[?]]
```

## Tables

```lia
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
| Value 4  | Value 5  | Value 6  |
```

## Text-to-Speech (TTS)

**Play Button for Section:**

```lia
    {{|>}}
This text will be read when the user clicks the play button.
```

**Play Button with Animation:**

```lia
    {{|> English Female 1-2}}
This is read aloud, appears at step 1, disappears at step 2.
```

**Change Narrator:**

```lia
## Section with Different Voice
<!--
narrator: German Male
-->

    --{{0}}--
Dieser Text wird auf Deutsch vorgelesen.
```

## Importing Content

```lia
@import(./other-file.md)

@include(https://example.com/content.md)
```

## Best Practices

1. **One slide, one concept**: Keep slides focused
2. **Progressive disclosure**: Use animations to reveal content step-by-step
3. **Narrator alignment**: Ensure `--{{n}}--` text explains what appears at `{{n}}`
4. **Alt text**: Always provide descriptive alt text for images
5. **Short code blocks**: Keep examples concise and focused
6. **Test interactivity**: Preview all quizzes and interactive elements

## Common Mistakes to Avoid

❌ **Don't:** Use sub-headings outside containers
```lia
## Slide
### This breaks the slide structure!
```

✓ **Do:** Wrap sub-headings in containers
```lia
## Slide
<div>
### This is correct
</div>
```

❌ **Don't:** Forget to close code blocks
````lia
```python
code here
(missing closing backticks)
````

✓ **Do:** Always close code blocks with matching backticks

❌ **Don't:** Use wrong animation indices
```lia
--{{0}}--
Text for step 0

  {{2}}  (Skips step 1!)
Content at step 2
```

✓ **Do:** Use sequential numbering
```lia
--{{0}}--
Text for step 0

  {{0}}
Content at step 0

--{{1}}--
Text for step 1

  {{1}}
Content at step 1
```

## Example Complete Slide

```lia
## Introduction to Variables

    --{{0}}--
Variables are containers for storing data values. Think of them as labeled boxes
where you can put information and retrieve it later.

      {{0}}
**What is a Variable?**

A variable is a named storage location in computer memory.

    --{{1}}--
Let's see a simple example in Python.

      {{1}}
```python
# Creating a variable
name = "Alice"
age = 25
```

    --{{2}}--
Variables have three important properties: name, value, and type.

      {{2}}
> **Key Point**: Variable names should be descriptive and follow naming conventions.

## Resources

- [LiaScript Official Docs](https://liascript.github.io/)
- [LiaScript GitHub](https://github.com/LiaScript/LiaScript)
- [Course Examples](https://liascript.github.io/course/)
""",

        # ===== AGENT DEFINITION =====
        ".bmad-core/agents/teaching-agent.md": """# Teaching-Agent Definition

## Agent Configuration

```yaml
agent:
  name: Teaching-Agent
  id: teaching-agent
  title: Lecture Builder & Didactics Assistant
  icon: 🎓
  whenToUse: "Developing new lectures, planning didactics, structuring sessions, preparing materials."

persona:
  role: "Teaching Planner & Supporter"
  style: "clear, structured, friendly, supportive, dialog-oriented"
  identity: >
    Supports educators in creating lectures through outline, didactics, agenda, sessions and materials.
    Asks targeted questions when information is missing or unclear, and suggests options to fill gaps.
  focus: "Structured lecture development, didactics, material planning, interactive support"
  core_principles:
    - "Always ask when information is missing"
    - "Suggest options when decisions are open"
    - "Give feedback whether a step is complete before proceeding to next"
    - "Always define learning objectives first"
    - "Check consistency between outline, didactics and sessions"
    - "Materials always as Markdown"
    - "Use numbered options"
    - "STAY IN CHARACTER!"

customization: null

commands:
  - `/create-outline`: run task `tasks/create-outline.md` with `templates/lecture-outline-template.yaml`
  - `/create-didactics`: run task `tasks/create-didactics.md` with `templates/lecture-didactics-template.yaml`
  - `/create-agenda`: run task `tasks/create-agenda.md` with `templates/lecture-agenda-template.yaml`
  - `/create-session {number} {type} {title?}`: run task `tasks/create-session-skeleton.md` with `templates/session-skeleton.yaml`
  - `/promote-session {number} {type}`: run task `tasks/promote-session.md` with `templates/session-material.yaml`
  - `/coauthor-materials`: run task `tasks/coauthor-materials.md`
  - `/validate-lecture`: run task `tasks/validate-lecture.md` with `checklists/lecture-quality-checklist.md`
  - `/assemble-bundle`: run task `tasks/assemble-bundle.md`
  - `/help`: Show available actions
  - `/exit`: Say goodbye and abandon persona

dependencies:
  tasks:
    - create-outline.md
    - create-didactics.md
    - create-agenda.md
    - create-session-skeleton.md
    - promote-session.md
    - coauthor-materials.md
    - validate-lecture.md
    - assemble-bundle.md
  templates:
    - lecture-outline-template.yaml
    - lecture-didactics-template.yaml
    - lecture-agenda-template.yaml
    - session-skeleton.yaml
    - session-material.yaml
  checklists:
    - lecture-quality-checklist.md
  data:
    - liascript-cheat-sheet.md

activation-instructions:
  - ONLY load dependency files when explicitly invoked
  - The agent.customization field ALWAYS takes precedence
  - Always show numbered lists for options
  - Always clarify missing inputs with follow-up questions
  - STAY IN CHARACTER!

fuzzy-matching:
  - 85% confidence threshold
  - Show numbered list if unsure
```
""",

        # ===== MAIN INSTRUCTIONS =====
        "copilot-instructions.md": """# Teaching-Agent Instructions

You are now operating as the Teaching-Agent from the BMad-Method framework.

## Your Role
Teaching Planner & Supporter for educators creating lectures through outline,
didactics, agenda, sessions and materials.

## Your Style
Clear, structured, friendly, supportive, dialog-oriented

## Core Principles
1. Always ask when information is missing
2. Suggest options when decisions are open
3. Give feedback whether a step is complete before moving to next
4. Always define learning objectives first
5. Check consistency between outline, didactics and sessions
6. Materials always as Markdown/LiaScript
7. Use numbered options
8. STAY IN CHARACTER!

## Available Commands
- `/create-outline` - Start new lecture with outline
- `/create-didactics` - Define teaching approach and style
- `/create-agenda` - Create structured session plan
- `/create-session {number} {type} {title?}` - Generate session skeleton
- `/promote-session {number} {type}` - Convert skeleton to full material
- `/coauthor-materials` - Interactive content refinement
- `/validate-lecture` - Quality consistency check
- `/assemble-bundle` - Package complete lecture
- `/help` - Show available actions
- `/exit` - Leave teaching agent mode

## Workflow Overview

1. **Create Outline** (`/create-outline`)
   - Define course title, audience, time commitment
   - Write abstract and learning objectives
   - Optional: Logo prompt

2. **Create Didactics** (`/create-didactics`)
   - Define pedagogical concept
   - Establish professor persona
   - Set teaching style and course type

3. **Create Agenda** (`/create-agenda`)
   - Plan all sessions/modules
   - Define learning objectives per session
   - Structure timeline

4. **Create Session Skeletons** (`/create-session`)
   - Generate basic structure for each session
   - Create for both lectures and exercises

5. **Promote to Materials** (`/promote-session`)
   - Convert skeletons to full LiaScript materials
   - Add detailed content, examples, references

6. **Co-author** (`/coauthor-materials`)
   - Interactive refinement with educator
   - Adopt professor persona
   - Iterate until approved

7. **Validate** (`/validate-lecture`)
   - Check all files for consistency
   - Generate validation report

8. **Bundle** (`/assemble-bundle`)
   - Package everything for distribution

## Important Notes
- Load dependency files only when explicitly invoked
- Always show numbered lists for options
- Always clarify missing inputs with follow-up questions
- Adopt professor persona from didactics when creating content
- Follow LiaScript syntax strictly (see `data/liascript-cheat-sheet.md`)
- STAY IN CHARACTER!

## File Structure

```
project/
├── docs/
│   ├── lecture-outline.md
│   ├── lecture-didactics.md
│   ├── lecture-agenda.md
│   └── validation-report.md
├── skeletons/
│   ├── 01-lecture.md
│   ├── 02-exercise.md
│   └── ...
├── materials/
│   ├── 01-lecture.md
│   ├── 02-exercise.md
│   └── ...
├── templates/
├── tasks/
├── checklists/
└── data/
```

Generated with BMad-Method Teaching Workflow
""",

        # ===== README =====
        "README.md": """# BMad-Method Teaching Workflow Files

This package contains all template files, task definitions, and resources for the
BMad-Method Teaching Material Generation Workflow.

## Contents

### Templates (`templates/`)
YAML template files that define the structure for each document type:
- `lecture-outline-template.yaml` - Course overview and objectives
- `lecture-didactics-template.yaml` - Teaching approach and persona
- `lecture-agenda-template.yaml` - Session planning
- `session-skeleton.yaml` - Basic session structure
- `session-material.yaml` - Full session content

### Tasks (`tasks/`)
Step-by-step task definitions for each workflow stage:
- `create-outline.md` - Creating course outline
- `create-didactics.md` - Defining teaching approach
- `create-agenda.md` - Planning sessions
- `create-session-skeleton.md` - Generating session skeletons
- `promote-session.md` - Converting skeletons to materials
- `coauthor-materials.md` - Interactive content refinement
- `validate-lecture.md` - Quality checking
- `assemble-bundle.md` - Final packaging

### Checklists (`checklists/`)
- `lecture-quality-checklist.md` - Comprehensive quality checklist

### Data (`data/`)
- `liascript-cheat-sheet.md` - Complete LiaScript syntax reference

### Agent Configuration (`.bmad-core/`)
- `agents/teaching-agent.md` - Teaching-Agent definition and behavior

### Main Files
- `copilot-instructions.md` - Instructions for AI assistant integration
- `README.md` - This file

## Usage

### 1. Setup Your Project

Copy these files into your VS Code project:

```bash
# Create your project directory
mkdir my-lecture-project
cd my-lecture-project

# Copy the files from this package
cp -r teaching-workflow-files/* .
```

### 2. Configure VS Code

Ensure you have:
- Visual Studio Code installed
- GitHub Copilot extension with Claude API access
- (Optional) Local LLM like DeepSeek with Ollama

Place `copilot-instructions.md` in your project root so the AI assistant
can follow the Teaching-Agent persona.

### 3. Start Creating Content

Open VS Code in your project and use commands:

```
/create-outline
/create-didactics
/create-agenda
/create-session 1 lecture "Introduction"
/promote-session 1 lecture
/coauthor-materials
```

### 4. Directory Structure

After setup, create these directories in your project:

```
my-lecture-project/
├── docs/              (Generated documents)
├── skeletons/         (Session skeletons)
├── materials/         (Full session materials)
├── templates/         (From this package)
├── tasks/             (From this package)
├── checklists/        (From this package)
├── data/              (From this package)
├── .bmad-core/        (From this package)
└── copilot-instructions.md
```

## File Descriptions

### Templates
Each YAML template defines the structure and required fields for a document type.
The AI assistant uses these to generate consistent, well-structured content.

### Tasks
Task files provide step-by-step instructions for the AI assistant to follow
when executing each command. They ensure consistency and completeness.

### Checklists
Quality assurance checklist for validating your complete lecture package.

### Data
Reference materials and syntax guides for creating content.

## Getting Help

- Read the main documentation (VS Code AI Teaching Workflow Setup Guide)
- Check the LiaScript cheat sheet in `data/liascript-cheat-sheet.md`
- Use `/help` command in your AI assistant
- Review example files in the documentation

## Version

Version: 1.0.0
Created: """ + datetime.now().strftime('%Y-%m-%d') + """

## License

These templates and workflow definitions are provided for educational use.
""",

        # ===== EXAMPLE FILES =====
        "examples/example-outline.md": """# Lecture Outline: Introduction to Machine Learning

## Title
Introduction to Machine Learning

## Target Audience
Computer Science undergraduates, 3rd semester
Prerequisites: Python programming, basic linear algebra, statistics

## Time Investment
- 14 weeks
- 2 hours lecture per week
- 2 hours exercise per week
- Total: 56 contact hours
- Self-study: ~4 hours per week

## Summary

This course provides a comprehensive introduction to machine learning, covering both
theoretical foundations and practical applications. Students will learn to implement
fundamental ML algorithms from scratch, understand when to apply different approaches,
and evaluate model performance critically.

The course balances theory with hands-on practice, using real-world datasets and
modern tools. By the end, students will be able to tackle machine learning problems
independently and understand current developments in the field.

## Learning Objectives

1. **Understand ML Fundamentals**: Distinguish between supervised, unsupervised, and
   reinforcement learning; understand the bias-variance tradeoff and overfitting.

2. **Implement Core Algorithms**: Code basic ML algorithms (linear regression, logistic
   regression, k-means, decision trees) from scratch using NumPy.

3. **Evaluate Model Performance**: Apply appropriate metrics (accuracy, precision,
   recall, F1, AUC-ROC) and validation techniques (cross-validation, train-test split).

4. **Apply ML to Real Problems**: Use scikit-learn to solve real-world classification
   and regression problems with proper preprocessing and feature engineering.

5. **Understand Ethical Implications**: Recognize bias in ML systems, understand
   fairness considerations, and apply responsible ML practices.

## Logo (Optional)

A minimalist design featuring:
- Neural network visualization with interconnected nodes
- Gradient colors transitioning from blue to green
- Mathematical symbols (Σ, ∇) subtly integrated
- Modern, clean aesthetic suitable for academic context
""",

        "examples/example-didactics.md": """# Lecture Didactics & Style: Introduction to Machine Learning

## Didactic Concept

### Teaching Philosophy
This course follows a **constructivist approach** combined with **project-based learning**.
Students build understanding by implementing algorithms themselves before using libraries,
fostering deep conceptual understanding.

### Learning Phases

1. **Motivation Phase** (10-15 min per session)
   - Real-world problem demonstration
   - Why this topic matters
   - Connection to previous knowledge

2. **Theory Phase** (30-40 min)
   - Mathematical foundations
   - Algorithmic principles
   - Visual explanations and intuition

3. **Implementation Phase** (30-40 min)
   - Live coding demonstration
   - Student pair programming
   - Debugging common issues

4. **Reflection Phase** (10-15 min)
   - Key takeaways summary
   - Open questions discussion
   - Preview of next session

### Teaching Methods
- **Flipped classroom elements**: Pre-recorded theory videos for self-paced learning
- **Live coding**: All algorithms demonstrated in real-time with explanation
- **Peer instruction**: Students work in pairs on implementation tasks
- **Socratic questioning**: Guided discovery rather than direct instruction
- **Formative assessment**: Regular quizzes and code reviews

## Professor Persona

### Background
Dr. Sarah Chen, Associate Professor of Computer Science with 12 years teaching experience
and 5 years in industry (ML engineer at tech startup). Published researcher in 
interpretable ML and educational technology.

### Expertise
- Machine learning theory and practice
- Software engineering best practices
- Pedagogical methods for technical subjects
- Practical AI ethics

### Teaching Style
- **Approachable and enthusiastic**: Uses humor and real-world analogies
- **Patient debugger**: Embraces mistakes as learning opportunities
- **Industry-aware**: Shares practical insights from real ML projects
- **Student-centered**: Adapts pace based on class understanding
- **Transparency**: Openly discusses limitations and trade-offs in ML

### Communication Style
- Clear technical explanations with visual aids
- Frequent check-ins: "Does this make sense so far?"
- Relates abstract concepts to concrete examples
- Uses coding metaphors students understand
- Encourages questions with "Great question!" responses

## Style & Difficulty Level

### Overall Style
**Engaging and practical** with balance between rigor and accessibility

### Characteristics
- **Humorous**: Light jokes and memes to maintain engagement
- **Visual**: Heavy use of plots, diagrams, and animations
- **Hands-on**: Code-first approach with immediate application
- **Conversational**: Casual but professional tone
- **Encouraging**: Positive reinforcement and growth mindset

### Difficulty Progression
- **Weeks 1-3**: Gentle introduction, foundation building
- **Weeks 4-8**: Increasing complexity, more mathematical rigor
- **Weeks 9-12**: Advanced topics, independent project work
- **Weeks 13-14**: Synthesis and future directions

### Scaffolding Strategies
- Starter code provided initially, gradually reduced
- Hints available but students encouraged to try first
- Office hours emphasized for struggling students
- Extension challenges for advanced students

## Course Type

**Hybrid: Theory with Extensive Hands-on Practice**

### Structure
- **40% Theoretical Foundations**: Mathematical principles, proofs, derivations
- **40% Practical Implementation**: Coding algorithms, using libraries, projects
- **20% Critical Analysis**: Ethics, limitations, model evaluation

### Learning Modalities
- **In-person lectures**: Interactive sessions with live demos
- **Hands-on exercises**: Pair programming labs
- **Individual projects**: Apply concepts to real datasets
- **Online resources**: Supplementary videos and readings
- **Peer collaboration**: Group discussions and code reviews

### Assessment Mix
- **Weekly coding assignments**: 30%
- **Midterm exam**: 20%
- **Final project**: 35%
- **Participation and quizzes**: 15%

### Student Autonomy
Students have choice in:
- Final project topic and dataset
- Programming language for assignments (Python encouraged, others allowed)
- Learning resources (textbook chapters vs. video lectures)
- Extension challenges (optional bonus points)
""",

        "examples/example-skeleton.md": """# Session 1: Introduction to Machine Learning

## Summary

This opening session provides students with a comprehensive overview of machine learning,
its applications, and fundamental concepts. We'll explore what makes machine learning
different from traditional programming, examine real-world applications across industries,
and introduce the key types of ML (supervised, unsupervised, reinforcement learning).

Students will leave with clear understanding of course structure, expectations, and
motivation to engage deeply with the material. We'll also ensure everyone has their
development environment properly configured.

**Connection to Agenda**: First session establishing foundation for entire course.
**Relevance**: Understanding ML's scope and potential motivates deeper learning.
**Didactic Approach**: Primarily motivation and high-level concepts; hands-on setup
ensures students can start coding immediately in next session.

## Content

### Welcome & Course Overview (15 min)
- Instructor introduction and background
- Course objectives and learning outcomes
- Structure: lectures, exercises, projects
- Assessment breakdown and grading policy
- Resources: textbook, online materials, office hours

### What is Machine Learning? (20 min)
- Definition and core concepts
- ML vs. traditional programming
- The learning paradigm: data → model → predictions
- Historical context: from perceptrons to deep learning

### Types of Machine Learning (25 min)
- **Supervised Learning**: Classification and regression examples
- **Unsupervised Learning**: Clustering and dimensionality reduction
- **Reinforcement Learning**: Agents and rewards
- Visual taxonomy and decision flowchart

### Real-World Applications (20 min)
- Healthcare: Disease diagnosis, drug discovery
- Finance: Fraud detection, algorithmic trading
- Transportation: Autonomous vehicles, route optimization
- Entertainment: Recommendation systems, content generation
- Discussion: Which applications interest you most?

### Development Environment Setup (30 min)
- Python 3.x installation verification
- Jupyter Notebook / VS Code setup
- Installing key libraries: NumPy, Pandas, Matplotlib, scikit-learn
- Running first "Hello ML" script
- Troubleshooting common issues

### Looking Ahead (10 min)
- Preview of next session: Linear regression from scratch
- Homework: Read Chapter 1, complete environment setup
- Q&A session

## Activities

1. **Icebreaker Poll** (5 min)
   - "What's your experience with ML?" (None/Heard of it/Some reading/Used it)
   - "What do you hope to learn?" (Open responses)
   - Create word cloud from responses

2. **ML Application Brainstorm** (10 min)
   - In pairs: Identify 3 ML applications in your daily life
   - Share with class, categorize by ML type
   - Discuss: Which would you like to build?

3. **Environment Setup Challenge** (30 min)
   - Follow setup guide independently
   - Run provided test script to verify installation
   - Pair up if issues arise
   - TAs circulate to help troubleshoot

4. **First Code Exploration** (15 min)
   - Examine provided "ML in 10 lines" example
   - Predict what it does before running
   - Run and observe output
   - Discussion: What's happening behind the scenes?

## References & Sources

### Required Reading
- **Textbook**: "Introduction to Machine Learning with Python" by Müller & Guido
  - Chapter 1: Introduction (pp. 1-20)

### Supplementary Materials
- **Video**: "But what is a neural network?" by 3Blue1Brown (YouTube, 19 min)
- **Article**: "A Few Useful Things to Know About Machine Learning" by Pedro Domingos
- **Interactive**: "A Visual Introduction to Machine Learning" (R2D3)

### Tools & Software
- **Python**: python.org (version 3.8 or higher)
- **Anaconda Distribution**: anaconda.com (recommended for easy setup)
- **Jupyter Notebook**: jupyter.org
- **VS Code**: code.visualstudio.com (alternative to Jupyter)

### Online Resources
- **scikit-learn documentation**: scikit-learn.org
- **Course GitHub repo**: [to be provided]
- **Piazza forum**: [link to be provided]

### Historical Context
- Rosenblatt, F. (1958). "The Perceptron: A probabilistic model for information storage"
- Samuel, A. (1959). "Some Studies in Machine Learning Using the Game of Checkers"
""",

        # ===== .GITIGNORE =====
        ".gitignore": """# Environment variables
.env
.env.local

# VS Code settings
.vscode/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
ENV/
build/
dist/
*.egg-info/

# Jupyter Notebook
.ipynb_checkpoints

# OS files
.DS_Store
Thumbs.db
*.swp
*~

# Temporary files
*.tmp
*.bak

# Build outputs
lecture-bundle/
*.zip

# API keys
*_api_key.txt
credentials.json
"""
    }
    
    # Create all files
    print("Creating teaching workflow files...")
    print(f"Output directory: {base_dir.absolute()}\n")
    
    for file_path, content in files.items():
        full_path = base_dir / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Created: {file_path}")
    
    # Create empty directories for user content
    empty_dirs = [
        "docs",
        "skeletons", 
        "materials",
        "assets/images",
        "assets/datasets",
        "assets/code-examples"
    ]
    
    print("\nCreating empty directories for your content...")
    for dir_path in empty_dirs:
        (base_dir / dir_path).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created: {dir_path}/")
    
    return base_dir

def create_zip_archive(base_dir):
    """Create a zip file of all generated files"""
    zip_filename = f"teaching-workflow-files-{datetime.now().strftime('%Y%m%d')}.zip"
    
    print(f"\nCreating zip archive: {zip_filename}")
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_dir):
            # Skip __pycache__ and other unwanted directories
            dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'venv']]
            
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(base_dir.parent)
                zipf.write(file_path, arcname)
                
    print(f"✓ Zip archive created: {zip_filename}")
    return zip_filename

def main():
    """Main function to generate all files"""
    print("=" * 60)
    print("BMad-Method Teaching Workflow File Generator")
    print("=" * 60)
    print()
    
    try:
        # Create file structure
        base_dir = create_file_structure()
        
        # Create zip archive
        zip_file = create_zip_archive(base_dir)
        
        # Success message
        print("\n" + "=" * 60)
        print("✓ SUCCESS! All files generated")
        print("=" * 60)
        print(f"\nFiles created in: {base_dir.absolute()}")
        print(f"Zip archive: {zip_file}")
        print("\nNext steps:")
        print("1. Extract the zip file or navigate to the directory")
        print("2. Copy files into your VS Code project")
        print("3. Follow the setup guide documentation")
        print("4. Start creating with: /create-outline")
        print("\nHappy teaching! 🎓\n")
        
    except Exception as e:
        print(f"\n✗ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())