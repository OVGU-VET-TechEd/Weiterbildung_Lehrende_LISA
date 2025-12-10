<!--
author: Hannes Tegelbeckers
email: hannes.tegelbeckers@ovgu.de
version: 1.0
language: en
comment: #


-->

# LiaScript Training Sequence: Zero to Hero (30 minutes)

## Training Overview
**Target Audience:** Teachers and Trainers  
**Duration:** 30 minutes  
**Approach:** Hands-on, progressive learning tasks  
**Goal:** From complete beginner to creating interactive educational content

---

## Task 1: Introduction & First Steps (5 minutes)

### What is LiaScript?
- Open-source markup language for creating interactive educational content
- Combines Markdown with educational features (quizzes, animations, code execution)
- No installation required - works in any web browser
- Perfect for creating engaging online courses and tutorials

### Your First LiaScript Document
**Task:** Create a basic LiaScript file

```markdown
# My First LiaScript Course

Welcome to my interactive course!

## Lesson 1: Getting Started

This is regular text content.

> **Note:** This is a highlighted note block.
```

**Action:** Save as `course.md` and open in LiaScript editor at https://liascript.github.io/

---

## Task 2: Adding Interactive Elements (7 minutes)

### Adding Quizzes
**Task:** Transform static content into interactive quizzes

```markdown
## Quiz Time!

What is 2 + 2?

- [( )] 3
- [(X)] 4
- [( )] 5

What are the primary colors? (Multiple choice)

- [[X]] Red
- [[ ]] Purple
- [[X]] Blue
- [[X]] Yellow
- [[ ]] Green

Fill in the blank: The capital of France is [[Paris]].
```

**Practice:** Create a quiz relevant to your subject area

---

## Task 3: Multimedia Integration (5 minutes)

### Adding Rich Media
**Task:** Embed videos, audio, and images

```markdown
## Multimedia Lesson

### Video Content
!?[Introduction Video](https://www.youtube.com/embed/dQw4w9WgXcQ)

### Audio Explanation
?[Audio Lesson](https://www.soundjay.com/misc/bell-ringing-05.wav)

### Visual Aid
![Diagram](https://via.placeholder.com/400x300?text=Your+Diagram+Here)
```

**Challenge:** Add one multimedia element to your course

---

## Task 4: Code Execution & Programming (6 minutes)

### Interactive Code Blocks
**Task:** Create executable code examples

```markdown
## Programming Section

Try this Python code:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
```

Modify the JavaScript below:

```javascript
let students = ['Alice', 'Bob', 'Charlie'];
console.log('Number of students:', students.length);
```

**Advanced:** Add code execution for your subject (Python, JavaScript, HTML, etc.)

---

## Task 5: Advanced Features (5 minutes)

### Surveys and Text Input
**Task:** Create interactive surveys

```markdown
## Student Feedback

What's your experience level?

    [(beginner)] Beginner
    [(intermediate)] Intermediate  
    [(advanced)] Advanced

Share your thoughts:

    [[Your feedback here...]]
```

### Animations and Effects
**Task:** Add visual animations

```markdown
## Animated Content

    {{1}}
Welcome to the course!

    {{2}}
Here's step one of the process.

    {{3}}
And here's the final result!
```

---

## Task 6: Course Structure & Navigation (2 minutes)

### Complete Course Template
**Task:** Build a full course structure

```markdown
<!--
author: Your Name
email: your.email@example.com
version: 1.0.0
language: en
narrator: US English Female
-->

# Complete Interactive Course

> **Course Description:** Brief overview of what students will learn

## Table of Contents

1. [Introduction](#introduction)
2. [Main Content](#main-content)
3. [Assessment](#assessment)
4. [Resources](#resources)

## Introduction
Course introduction content...

## Main Content
Interactive lessons with quizzes and multimedia...

## Assessment
Final quiz or project...

## Resources
Additional materials and links...
```

---

## Rapid Implementation Checklist

### ✅ Essential LiaScript Elements You've Mastered:
- [ ] Basic Markdown formatting
- [ ] Multiple choice quizzes `[( )] [(X)]`
- [ ] Multi-select questions `[[ ]] [[X]]`
- [ ] Text input fields `[[answer]]`
- [ ] Video embedding `!?[title](url)`
- [ ] Audio embedding `?[title](url)`
- [ ] Code execution blocks
- [ ] Surveys and feedback forms
- [ ] Animations `{{1}} {{2}} {{3}}`
- [ ] Course metadata and structure

### 🚀 Next Steps After Training:
1. **Practice:** Create a 5-minute lesson in your subject area
2. **Explore:** Visit https://liascript.github.io/course/ for advanced examples
3. **Community:** Join LiaScript GitHub discussions
4. **Resources:** Bookmark the LiaScript documentation

### 💡 Pro Tips for Success:
- Start simple, then add interactivity gradually
- Test your content frequently in the LiaScript viewer
- Use consistent formatting throughout your courses
- Preview on different devices (mobile-friendly)
- Keep backup copies of your `.md` files

---

## Challenge: Create Your First Mini-Course (Bonus)

**Goal:** Before leaving today, create a 3-slide interactive mini-course on any topic you teach.

**Must Include:**
- Title slide with course info
- One interactive quiz
- One multimedia element
- Basic navigation structure

**Time:** 10 minutes additional practice

---

## Resources for Continued Learning

- **Official Documentation:** https://liascript.github.io/
- **Course Examples:** https://github.com/liaScript/docs
- **Template Repository:** https://github.com/liaScript/template
- **Community Support:** GitHub Issues and Discussions
