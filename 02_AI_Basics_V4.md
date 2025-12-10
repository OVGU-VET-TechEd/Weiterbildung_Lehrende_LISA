<!--
author: AI in TVET Workshop Team
email: tvet.ai@education.org
version: 1.5.0
language: en
narrator: US English Female
comment: AI Basics and Human Agency for TVET Teachers. A comprehensive 15-minute learning nugget focused on developing critical understanding of AI fundamentals while maintaining human decision-making authority in educational contexts.

link: https://raw.githubusercontent.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/refs/heads/main/ASSET_basic.css

@style
.welcome-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 3rem;
    margin: 2rem 0;
    border-radius: 20px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.3);
}

.sector-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    margin: 1rem;
    border-radius: 15px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    transition: transform 0.3s ease;
}

.sector-card:hover {
    transform: translateY(-5px);
}

.ai-tool-demo {
    background: #f8f9fa;
    border: 2px solid #007bff;
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1rem 0;
}

.nugget-header {
    background: linear-gradient(45deg, #ff6b6b, #ffa726);
    color: white;
    padding: 1.5rem;
    border-radius: 15px;
    margin: 1rem 0;
    text-align: center;
}

.competency-framework {
    text-align: center;
    margin: 2rem 0;
    padding: 1rem;
    background: white;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.reflection-section {
    background: #fafafa;
    border-left: 4px solid #9c27b0;
    padding: 1.5rem;
    margin: 2rem 0;
}

.resource-link {
    background: #28a745;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    text-decoration: none;
    display: inline-block;
    margin: 0.25rem;
    transition: all 0.3s ease;
}

.resource-link:hover {
    background: #218838;
    transform: scale(1.05);
}

.quiz-interactive {
    background: linear-gradient(45deg, #ff6b6b, #ffa726);
    color: white;
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
}

.contact-info {
    background: #fff3e0;
    border: 1px solid #ff9800;
    padding: 1rem;
    border-radius: 8px;
    margin: 1rem 0;
}

.audio-control {
    background: #e8f5e8;
    padding: 0.5rem;
    border-radius: 5px;
    margin: 0.5rem 0;
}

.definition-card {
    background: #e3f2fd;
    border: 1px solid #2196f3;
    border-radius: 10px;
    padding: 1rem;
    margin: 0.5rem 0;
    cursor: pointer;
    transition: all 0.3s ease;
}

.definition-card:hover {
    background: #bbdefb;
    transform: scale(1.02);
}

.risk-warning {
    background: #fff3e0;
    border: 2px solid #ff9800;
    border-radius: 10px;
    padding: 1rem;
    margin: 1rem 0;
    border-left: 5px solid #f57c00;
}

.human-agency-box {
    background: #e8f5e8;
    border: 2px solid #4caf50;
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1rem 0;
    border-left: 5px solid #2e7d32;
}
@end

@customQuiz
[[.]]
<script>
"@0" == btoa( "@input".trim().toLowerCase() )
</script>
@end

@aiDemo: <div class="ai-tool-demo">**🤖 AI Demo:** @0<br>**🛠️ Tool:** @1<br>**🔗 Try it:** [Click here](@2)</div>

@sectorCard: <div class="sector-card">**@0**<br>@1</div>

@resourceLink: <a href="@1" class="resource-link" target="_blank">@0</a>

@competencyHighlight: <div class="competency-framework"><p style="color: #2196f3; font-weight: bold;">@0</p></div>

@scenarioCard: <div style="background: #f8f9fa; color: #333; padding: 1.5rem; margin: 1rem 0; border-radius: 15px; box-shadow: 0 4px 16px rgba(0,0,0,0.1); border-left: 4px solid #007bff;"><h4>🛠️ @0</h4><p>@1</p></div>

@definitionCard: <div class="definition-card"><strong>@0:</strong> @1</div>

@riskWarning: <div class="risk-warning"><strong>⚠️ @0</strong><br>@1</div>

@humanAgency: <div class="human-agency-box"><strong>🤝 Human Agency Principle:</strong> @0</div>

@h5p: <div class="h5p-element"><iframe src="@0" width="100%" height="@1" frameborder="0"></iframe></div>
-->

# 🧠 AI Basics: Building Understanding and Human Agency

<svg xmlns='http://www.w3.org/2000/svg' width='1100' height='400' viewBox='0 0 800 450'>
  <!-- Background -->
  <rect width='800' height='450' fill='#0072CE' />
  
  <!-- White rounded rectangle container -->
  <rect x='50' y='50' width='700' height='350' rx='20' fill='white' />
  
  <!-- Title -->
  <text x='400' y='120' font-family='Segoe UI, Arial, sans-serif' font-size='36' font-weight='bold' text-anchor='middle' fill='#0072CE'>
    AI Basics &amp; Human Agency
  </text>
  
  <!-- Subtitle -->
  <text x='400' y='160' font-family='Segoe UI, Arial, sans-serif' font-size='24' font-weight='bold' text-anchor='middle' fill='#00A1DE'>
    Virtual Training Nugget 2.0
  </text>

  <!-- Framework Reference -->
  <text x='400' y='190' font-family='Segoe UI, Arial, sans-serif' font-size='16' font-weight='bold' text-anchor='middle' fill='#00A1DE'>
    UNESCO AI Competency: Human-Centered Mindset
  </text>

  <!-- Collaboration info -->
  <text x='400' y='215' font-family='Segoe UI, Arial, sans-serif' font-size='16' font-weight='bold' text-anchor='middle' fill='#00A1DE'>
    Maintaining Human Control in AI-Enhanced Education
  </text>

  <!-- Academic reference -->
  <text x='400' y='240' font-family='Segoe UI, Arial, sans-serif' font-size='14' font-weight='bold' text-anchor='middle' fill='#00A1DE'>
    A collaboration of the UNEVOC Network - ASSET Project
  </text>
  
  <!-- Key Focus -->
  <text x='400' y='280' font-family='Segoe UI, Arial, sans-serif' font-size='18' font-weight='bold' text-anchor='middle' fill='#0072CE'>
    Understanding AI Fundamentals While Staying in Control
  </text>
</svg>

<!-- License info -->
<div style="position: fixed; bottom: 10px; right: 10px; font-size: 12px; opacity: 0.7;">
  <a href="https://creativecommons.org/licenses/by-sa/4.0/" style="margin-left: 5px; text-decoration: none;">CC BY-SA 4.0</a>
</div>

<!-- UNEVOC -->
<div style="position: fixed; bottom: 1px; left: 20px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/UNESCO-UNEVOC_logo.png?raw=true" alt="UNEVOC Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">UNEVOC</div>
</div>

<!-- ASSET -->
<div style="position: fixed; bottom: 1px; left: 180px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/ASSET_icon.png?raw=true" alt="ASSET Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">ASSET</div>
</div>

<!-- HWK Blume -->
<div style="position: fixed; bottom: 1px; left: 340px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/HWK_Blume.png?raw=true" alt="HWK Blume Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 7px;">HWK Blume</div>
</div>

<!-- GIZ -->
<div style="position: fixed; bottom: 1px; left: 500px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/giz-logo.gif?raw=true" alt="GIZ Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">GIZ</div>
</div>

<!-- UoVT -->
<div style="position: fixed; bottom: 1px; left: 660px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/UoVT_Logo.png?raw=true" alt="UoVT Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">UoVT</div>
</div>

<!-- OVGU -->
<div style="position: fixed; bottom: 1px; left: 820px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/Masub27/Intro/blob/main/ovgu.png?raw=true" alt="OVGU Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">OVGU</div>
</div>

<!-- HRDC -->
<div style="position: fixed; bottom: 1px; left: 980px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/hrdc_logo.png?raw=true" alt="HRDC Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">HRDC</div>
</div>

<!-- MITD -->
<div style="position: fixed; bottom: 1px; left: 1140px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/mitd_logo.png?raw=true" alt="MITD Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">MITD</div>
</div>

---

## 🎯 Course Overview

<div class="nugget-header">
**Virtual Training Nugget 2:** AI Basics and Human Agency
<br>
**Competency Focus:** Human-Centered Mindset (Acquire Level) | **Duration:** 15 minutes
</div>

<div class="audio-control">
🎵 **Audio Narration Available** - Click the speaker icon to listen to this content
</div>

**📚 Learning Objectives**

By the end of this nugget, you will be able to:

1. **Define** essential AI terminology (algorithm, model, weights, bias, prompting) in simple terms
2. **Distinguish** between different types of AI systems and their applications in education
3. **Recognize** AI hallucinations and bias in educational contexts
4. **Apply** human agency principles to maintain control over AI-assisted teaching
5. **Evaluate** AI outputs critically while leveraging their benefits responsibly

---

## UNESCO Competency Focus: Human-Centered Mindset

@competencyHighlight(🎯 Current Focus: Developing critical understanding that AI is human-led, ensuring human agency in educational decision-making)

**Core Principle:** Teachers maintain authority over AI systems, not the reverse. AI serves human learning goals, and educators retain final decision-making power in educational contexts.

| Learning Progression | Your Current Level | What This Means |
|---------------------|-------------------|-----------------|
| **Acquire** | **🎯 YOU ARE HERE** | Develop critical understanding of AI's human-led nature |
| **Deepen** | Next Level | Apply human-centered principles in AI tool selection |
| **Create** | Advanced Level | Design AI-enhanced experiences prioritizing human agency |

---

## Continuing Rani's Journey

@scenarioCard(Rani's Next Challenge, After completing her AI orientation - Rani feels ready to dive deeper. She wants to understand the technical basics: What exactly are these "models" and "algorithms" everyone mentions? Why do people talk about AI "hallucinating" or being "biased"? How can she use AI tools while ensuring she and not the AI—remains in charge of her students' educational experience?)

Rani's questions reflect a critical need: **understanding AI terminology and principles while maintaining human agency.** Let's explore these concepts together.

---

# 🔤 Key AI Definitions: Demystifying the Jargon

Understanding AI terminology empowers you to make informed decisions about educational technology. Let's break down essential concepts:

## Core AI Vocabulary

@definitionCard(Artificial Intelligence, The broad field of creating machines or software that perform tasks requiring human-like intelligence—learning, pattern recognition, decision-making, and content generation. In education, AI might personalize learning paths or provide instant feedback.)

@definitionCard(Algorithm, A step-by-step procedure or set of rules for solving problems. Traditional algorithms follow explicit human programming; AI algorithms learn and improve from data. Think of it as a "recipe" that computers follow.)

@definitionCard(Model, A trained AI system that makes predictions or decisions based on learned patterns. After training on thousands of examples, a model becomes capable of handling new, similar situations. It's the "graduate" of the AI learning process.)

@definitionCard(Weights, Internal parameters that determine how an AI model processes information. During training, these weights adjust to improve performance—like strengthening neural connections in learning. You won't see weights directly, but they control model behavior.)

@definitionCard(Bias, Systematic errors or unfair patterns in AI outputs, often reflecting prejudices in training data or design. In education, this might manifest as AI tools favoring certain demographics over others.)

@definitionCard(Prompting, The process of communicating with AI systems through carefully crafted inputs or questions. Effective prompting requires clear instructions, context, and examples to guide AI responses toward desired outcomes.)

### 🎓 Interactive Definition Matching

Test your understanding by matching terms to scenarios:

**Scenario 1:** Rani trains a system to recognize faulty circuit components by showing it thousands of labeled images. The final trained system is called a ______.

    [(X)] Model
    [( )] Algorithm  
    [( )] Prompt
    [( )] Weight

**Scenario 2:** When Rani asks an AI assistant "Create a quiz question about Ohm's Law for beginner students," she is ______.

    [( )] Training
    [(X)] Prompting
    [( )] Modeling
    [( )] Weighting

**Scenario 3:** An AI grading tool consistently gives lower scores to essays written by non-native English speakers, even when content quality is equivalent. This demonstrates ______.

    [( )] Hallucination
    [(X)] Bias
    [( )] Prompting
    [( )] Algorithm

---

# 🔧 Types of AI Systems: Understanding the Landscape

Different AI approaches serve different educational needs. Understanding these types helps you choose appropriate tools. You don’t need to master the technical details to benefit from them. The goal is simply to recognize the main categories and what they can offer in learning contexts. Think of these models as broad "families" of AI, each with strengths and limitations.

This overview is meant to provide orientation, not deep technical training. It can help you decide which tools might be useful in your practice and where you may want to explore further. If a particular approach sparks your interest, it can also serve as a starting point for more specialized professional development.

## Traditional Rule-Based Systems

**How they work:** Follow explicit "if-then" rules programmed by humans  

**Educational example:** A tutoring program that displays specific hints when students make common errors  

**Advantages:** Transparent, predictable, easy to control  

**Limitations:** Cannot adapt to unexpected situations or learn from experience  


## Machine Learning (ML) Systems

**Core concept:** Learn patterns from data rather than following fixed rules

@competencyHighlight(Supervised Learning)

- **Process:** Learns from labeled examples (input-output pairs)
- **TVET Application:** Training a system to classify correct vs. incorrect solder joints using labeled images
- **Strength:** High accuracy when sufficient quality data is available

@competencyHighlight(Unsupervised Learning) 

- **Process:** Finds hidden patterns in unlabeled data
- **TVET Application:** Clustering student learning behaviors to identify different learning styles
- **Strength:** Discovers unexpected patterns humans might miss

@competencyHighlight(Reinforcement Learning)

- **Process:** Learns through trial and error with rewards/penalties
- **TVET Application:** AI that learns optimal teaching sequences by tracking student engagement and success
- **Strength:** Continuously improves through interaction

## Neural Networks and Deep Learning

**Structure:** Networks of interconnected mathematical functions mimicking brain neurons  

**Capability:** Excel at complex pattern recognition (images, speech, text)  

**TVET Applications:**  

- Analyzing motor sounds to predict equipment failure
- Recognizing hand-drawn circuit diagrams
- Converting technical speech to text for accessibility

@aiDemo(Experience neural networks in action, Google's Teachable Machine, https://teachablemachine.withgoogle.com/)

## Generative AI

**Capability:** Creates new content (text, images, code, audio) based on learned patterns  

**Popular examples:** ChatGPT, DALL-E, GitHub Copilot  

**Educational power:** Can generate lesson materials, practice problems, and explanations  

**Critical consideration:** May produce convincing but incorrect content ("hallucinations")  


## Expert Systems

**Approach:** Combine rule-based logic with specialized knowledge databases  

**TVET Application:** Diagnostic systems for troubleshooting electronic equipment  

**Advantage:** Highly accurate within narrow domains  

**Limitation:** Cannot learn or adapt without human programming  

@sectorCard(Choosing the Right AI Type, Rani considers different AI systems for her electronics lab. For equipment diagnostics she prefers an expert system's reliability and explainability. For generating diverse practice problems she uses generative AI but always reviews outputs. For analyzing student progress patterns she explores machine learning tools. Understanding each type's strengths helps her make informed choices.)

---

# ⚠️ AI's Critical Limitations: Hallucinations and Bias

Understanding AI's failure modes is essential for maintaining human agency and protecting student learning.

## AI Hallucinations: When AI Confidently Gets It Wrong

@riskWarning(Definition, AI hallucination occurs when systems generate factually incorrect or nonsensical information while appearing confident and authoritative. This happens because AI predicts likely words/content, not truth.)

### Real-World Examples in Education

**Rani's Experience:** She asked a chatbot for a biography of a famous electronics engineer. The AI provided accurate basic information but invented a prestigious award the engineer never received. The fabricated detail was seamlessly integrated with true facts.

**Classroom Danger:** Students might ask AI to explain circuit analysis and receive a response containing invented formulas or non-existent components, potentially spreading misinformation.

**Protection Strategy:**

- Always verify factual claims from AI sources
- Cross-reference technical information with authoritative sources  
- Teach students to treat AI as a starting point, not final authority
- Use AI for brainstorming and drafts, not definitive answers

### Types of Hallucinations to Watch For

1. **Factual Errors:** Incorrect dates, names, specifications, or formulas
2. **Invented Sources:** References to non-existent research papers or websites
3. **Logical Inconsistencies:** Contradictory statements within the same response
4. **Technical Impossibilities:** Describing processes or components that violate physical laws

## AI Bias: When Systems Perpetuate Unfairness

@riskWarning(Definition, AI bias refers to systematic prejudice in AI outputs that unfairly advantages or disadvantages certain groups. This typically stems from biased training data or flawed assumptions built into algorithms.)

### Educational Bias Examples

**Language Bias:** An AI writing evaluator trained primarily on native English speakers might systematically score ESL students lower, regardless of content quality.

**Gender Bias:** Career guidance AI might recommend electronics engineering more frequently to male students if historical data shows gender imbalances in the field.

**Cultural Bias:** AI tools trained on Western educational contexts might not recognize valid learning approaches from other cultural traditions.

### Rani's Bias Discovery

@scenarioCard(AI Grading Bias, Rani experimented with an AI essay grader for technical writing assignments. She noticed a troubling pattern: essays by non-native English speakers consistently received lower scores, even when their technical content was excellent. Investigation revealed the AI was trained predominantly on native English academic writing, creating an inherent bias against different writing styles. Rani abandoned automated grading and instead uses AI to generate rubric suggestions, which she then reviews and adapts.)

### Recognizing and Addressing Bias

**Detection Strategies:**

- Monitor AI outputs across different student demographics
- Compare AI recommendations with your professional judgment
- Question whether AI training data represents your student population
- Look for systematic patterns in AI decisions

**Mitigation Approaches:**

- Use diverse AI tools to cross-check results
- Supplement AI insights with human oversight
- Explicitly prompt AI to consider diverse perspectives
- Educate students about potential AI biases

---

# 🤝 Maintaining Human Agency: You Stay in Control

Human agency means educators retain ultimate authority over educational decisions, using AI as a tool rather than allowing it to drive choices.

@humanAgency(Teachers make final decisions about curriculum, assessment, and student support. AI provides suggestions and assistance, but human judgment determines educational outcomes.)

## Principles of Human Agency in Education

@competencyHighlight(Critical Oversight)

**Practice:** Review all AI-generated content before using it with students  
**Example:** Rani uses AI to draft quiz questions but edits each one for accuracy, clarity, and appropriateness  
**Rationale:** AI may not understand your specific context, student needs, or learning objectives

@competencyHighlight(Final Decision Authority)  

**Practice:** Treat AI outputs as recommendations, not commands  
**Example:** If AI suggests a student needs additional support, Rani investigates using her professional judgment and multiple data sources  
**Rationale:** Educational decisions affect real people and require contextual understanding AI lacks

@competencyHighlight(Accountability Awareness)

**Practice:** Accept responsibility for all AI-assisted educational content and decisions  
**Example:** Rani ensures any AI-generated materials align with her professional standards and institutional policies  
**Rationale:** AI systems don't bear responsibility for educational outcomes—humans do

@competencyHighlight(Transparent Communication)

**Practice:** Inform students and colleagues when AI tools are used in educational processes  
**Example:** Rani explains to students when homework feedback was AI-assisted vs. entirely human-generated  
**Rationale:** Builds trust and helps learners understand the educational process

## Practical Human Agency Strategies

@competencyHighlight(Before Using AI:)

- Define clear objectives for AI assistance
  
- Understand the AI tool's capabilities and limitations
    
- Establish criteria for evaluating AI outputs
  
- Plan how to verify AI-generated content  

@competencyHighlight(During AI Interaction:)

- Provide specific, detailed prompts

- Ask follow-up questions to test AI understanding

- Request AI to explain its reasoning when possible

- Remain skeptical of overconfident responses

@competencyHighlight(After AI Response:)

- Fact-check claims against authoritative sources

- Consider whether outputs align with educational objectives

- Evaluate potential bias or inappropriate content

- Adapt or reject AI suggestions based on professional judgment

---

# 🔬 Practical Example: Human Agency in Action

@competencyHighlight(The Scenario: Creating a Circuit Analysis Quiz)

**AI Prompt:** "Create a multiple-choice question testing students' understanding of Ohm's Law."

**AI Response:**
*"What is Ohm's Law?  
(a) Voltage = Current / Resistance  
(b) Voltage = Current × Resistance  
(c) Voltage = Resistance / Current  
(d) Voltage = Current + Resistance"*

## Rani's Human Agency Analysis

@competencyHighlight(✅ What the AI Did Well:)

- Focused on the requested topic (Ohm's Law)
- Provided multiple-choice format
- Included correct answer (option b)

@competencyHighlight(⚠️ Areas Needing Human Oversight:)

1. **Question Quality:** The question tests memorization, not understanding
2. **Distractor Issues:** Option (d) is obviously wrong—adding voltage and current makes no physical sense
3. **Learning Assessment:** Doesn't evaluate students' ability to apply Ohm's Law

@competencyHighlight(🔧 Rani's Human Improvements:)

**Revised Question:**
*"A circuit has a resistance of 10Ω and carries a current of 2A. Using Ohm's Law, what is the voltage across the resistor?  
(a) 5V  
(b) 12V  
(c) 20V  
(d) 0.2V"*

**Improvements Made:**

- Tests application, not just recall
- Uses realistic values from electronics work
- All distractors represent plausible calculation errors
- Aligns with hands-on learning objectives

@competencyHighlight(The Lesson)

**AI as Starting Point, Human Expertise as Finisher**

Rani demonstrates perfect human agency: she leverages AI efficiency while applying professional judgment to ensure educational quality.


---

# 🧠 Interactive Knowledge Assessment

<div class="quiz-interactive">

**Test Your Understanding of AI Basics and Human Agency**

Let's reinforce key concepts through practical scenarios:

</div>

### Question 1: Recognizing AI Hallucinations

A student asks an AI tool to explain parallel circuits. The AI responds with mostly correct information but states: "Current in parallel circuits is always equal in each branch, following Kirchhoff's Current Law." As Rani, what should you do?

    [( )] Accept the AI's answer since it mentions Kirchhoff's Law
    [(X)] Correct this misinformation—in parallel circuits, voltage is equal across branches, not current
    [( )] Tell students to ignore all AI explanations
    [( )] Let students figure it out themselves through trial and error

<script>
if (@input === 1) {
  send.lia("✅ **Excellent!** You recognized the hallucination. In parallel circuits, voltage is equal across branches while current divides based on resistance. This demonstrates perfect human agency—catching AI errors before they mislead students.");
} else {
  send.lia("❌ **Not quite right.** The AI statement contains a dangerous error: in parallel circuits, VOLTAGE is equal across branches, not current. Current divides based on each branch's resistance. Always verify AI technical explanations.");
}
</script>

### Question 2: Identifying Bias (Multiple Select)

Which scenarios demonstrate potential AI bias in educational settings? Select all that apply.

    [[X]] An AI writing evaluator consistently gives lower scores to essays with non-Western cultural references
    [[X]] A career guidance AI recommends technical trades more often to students from lower socioeconomic backgrounds
    [[ ]] An AI generates different quiz questions for each student based on their learning pace
    [[X]] An AI language tutor performs poorly with regional dialects not represented in its training data
    [[ ]] An AI creates varied problem contexts to maintain student interest

<script>
let correct = [0, 1, 3];
let selected = @input;

let isCorrect = correct.every(i => selected.includes(i)) && 
               selected.every(i => correct.includes(i));

if (isCorrect) {
  send.lia("✅ **Perfect understanding!** You identified bias scenarios where AI systematically disadvantages certain groups due to training data limitations or embedded assumptions. Personalization (option 3) and variety (option 5) are actually beneficial AI applications.");
} else {
  send.lia("❌ **Review needed.** Bias occurs when AI systematically treats groups unfairly, often due to skewed training data. Look for patterns where AI consistently disadvantages certain demographics or cultural backgrounds.");
}
</script>

### Question 3: Human Agency in Practice

Rani uses AI to generate a lesson plan for teaching voltage dividers. Which approach best demonstrates human agency?

    [( )] Use the AI-generated plan exactly as provided to save time
    [(X)] Review the plan, adapt it to her specific students' needs, and verify technical accuracy
    [( )] Reject AI assistance entirely to maintain full control
    [(X)] Combine AI suggestions with her professional expertise and curriculum requirements

<script>
let correct2 = [1, 3];
let selected2 = @input;

let isCorrect2 = correct2.every(i => selected2.includes(i)) && 
                selected2.every(i => correct2.includes(i));

if (isCorrect2) {
  send.lia("✅ **Outstanding!** You understand that human agency means leveraging AI efficiency while maintaining professional judgment and final decision-making authority.");
} else {
  send.lia("❌ **Think deeper.** Human agency isn't about avoiding AI entirely, but about maintaining control over educational decisions while benefiting from AI assistance. The teacher's expertise guides the process.");
}
</script>
---

# 🤔 Professional Reflection

<div class="reflection-section">

**Critical Thinking Exercise**

Consider your current or planned use of AI in TVET education. Address these human agency questions:

1. **Risk Assessment:** What specific hallucinations or biases might affect AI tools in your subject area?

2. **Quality Control:** How will you verify AI-generated content before using it with students?

3. **Decision Authority:** In what situations should you trust AI suggestions vs. rely on your professional judgment?

4. **Student Education:** How will you teach students to collaborate with AI while maintaining critical thinking?

5. **Ethical Responsibility:** What standards will guide your use of AI in educational contexts?

**Action Planning:**
- Choose one AI tool you'd like to explore for your teaching
- Define specific quality check procedures for that tool
- Plan how to maintain human agency while using it effectively

</div>

---

# 📚 Resources for Deeper Learning

@competencyHighlight(🛠️ Tools for Understanding AI Bias)

@aiDemo(Test AI bias in image recognition, Google's Teachable Machine, https://teachablemachine.withgoogle.com/)
@aiDemo(Explore AI decision-making, MIT's Moral Machine, http://moralmachine.mit.edu/)
@aiDemo(Understanding AI limitations, AI Explainer Tools, https://pair-code.github.io/what-if-tool/)

@competencyHighlight(📖 Professional Development)

**Recommended Courses:**

- **Ethics in AI Design** - Understanding bias and fairness in educational AI
- **Critical AI Literacy** - Developing skills to evaluate AI systems
- **Human-AI Collaboration** - Best practices for maintaining human agency

---

# 🔗 Course Navigation & Next Steps

@competencyHighlight(🎯 Key Takeaways)

**You now understand:**  

✅ Essential AI terminology and system types  

✅ How to recognize AI hallucinations and bias  

✅ Principles of maintaining human agency in AI-enhanced education  

✅ Practical strategies for responsible AI use in TVET contexts  


## 🚀 Preparing for Module 3: AI Tools and Applications

**Coming Next:** Hands-on exploration of specific AI tools for TVET education  
**Preview Topics:**

- Comparative analysis of popular AI platforms
- Selecting appropriate tools for specific educational tasks  
- Practical integration strategies
- Building your personal AI toolkit

**Recommended Preparation:**

- Identify one specific teaching challenge where AI might help
- Create accounts on 2-3 AI platforms (ChatGPT, Claude, Perplexity)
- Begin documenting your AI experiments and observations

## 📚 Complete Learning Sequence

1. [AI Orientation](https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/Self_Learning_Nuggets_AI_Basics/refs/heads/main/01_AI_Orientation_V4.md) - ✅ Completed: Foundation and motivation
2. **AI Basics & Human Agency** - ✅ Current: Technical foundations  
3. [AI Tools and Applications](https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/Self_Learning_Nuggets_AI_Basics/refs/heads/main/03_AI_Tools_V4.md) - 🔜 Exploring practical AI tools
4. [AI-Assisted Teaching and Prompting](https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/Self_Learning_Nuggets_AI_Basics/refs/heads/main/04_Prompting_V4.md) - 🔜 Advanced AI integration
5. [Ethics and Quality in AI Education](https://liascript.github.io/course/?https://raw.githubusercontent.com/OVGU-VET-TechEd/Self_Learning_Nuggets_AI_Basics/refs/heads/main/05_Ethics_V4.md) - 🔜 Responsible AI use


---

# 🎉 Module Completion

@humanAgency(Remember: You are the educational expert. AI is your assistant, not your replacement. Your professional judgment, understanding of your students, and commitment to quality education guide every decision. AI amplifies your capabilities—it never substitutes your expertise.)

<div class="contact-info">
**📧 Support & Feedback:**
Email: tvet.ai@education.org  
🌐 Course Portal: [GitHub Repository](https://github.com/OVGU-VET-TechEd/Self_Learning_Nuggets_AI_Basics/)  
📋 Feedback Form: [English](https://umfrage.zwh.de/c/unescoengl) | [Deutsch](https://umfrage.zwh.de/c/unescodeut)
</div>

> *"Understanding AI's capabilities and limitations empowers educators to harness its benefits while protecting student learning. Human agency ensures technology serves education, not the reverse."*

---

# 🏁 Course Completion

<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="650" viewBox="0 0 1280 720" role="img" aria-labelledby="title desc">
  <title id="title">AI Basics Completion - Human Agency Success</title>
  <desc id="desc">Congratulations slide celebrating successful completion of AI Basics and Human Agency module.</desc>

  <!-- Background -->
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#0b2447"/>
    </linearGradient>
  </defs>

  <rect width="1280" height="720" fill="url(#bgGrad)"/>

  <!-- Main content panel -->
  <rect x="80" y="80" rx="24" ry="24" width="1120" height="560" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.06)" stroke-width="1"/>

  <!-- Left accent bar -->
  <rect x="100" y="120" width="16" height="480" rx="8" fill="#10b981" opacity="0.95"/>

  <!-- Headline -->
  <text x="180" y="200" font-family="Inter, Arial, sans-serif" font-size="42" font-weight="700" fill="#ffffff">
    AI Basics Mastered: You're in Control!
  </text>

  <!-- Divider line -->
  <line x1="180" y1="220" x2="1060" y2="220" stroke="rgba(255,255,255,0.06)" stroke-width="2"/>

  <!-- Success message -->
  <text x="180" y="300" font-family="Inter, Arial, sans-serif" font-size="26" fill="#e6f0ff">
    You've built strong AI foundations while maintaining human agency.
  </text>
  
  <text x="180" y="340" font-family="Inter, Arial, sans-serif" font-size="22" fill="#bfe6d9">
    Ready to explore specific AI tools and applications with confidence.
  </text>

  <!-- Key achievement -->
  <text x="180" y="400" font-family="Inter, Arial, sans-serif" font-size="20" fill="#dffcf6">
    🎯 Key Achievement: Balancing AI efficiency with educational judgment
  </text>

  <!-- Next steps -->
  <text x="180" y="450" font-family="Inter, Arial, sans-serif" font-size="18" fill="#dffcf6">
    Next: Discover practical AI tools for TVET education in Module 3
  </text>

  <!-- Footer badge -->
  <g transform="translate(180,520)">
    <circle cx="0" cy="0" r="28" fill="#0ea5a3" opacity="0.95"/>
    <text x="48" y="8" font-family="Inter, Arial, sans-serif" font-size="16" fill="#dffcf6">
      Human Agency • AI Literacy • TVET Excellence
    </text>
  </g>

  <!-- Decorative elements -->
  <g transform="translate(980,140) scale(1.2)" fill="none" stroke="#ffffff" stroke-opacity="0.08" stroke-width="2">
    <circle cx="40" cy="40" r="28"/>
    <circle cx="100" cy="40" r="18"/>
    <path d="M60 20v40M20 40h40" stroke-linecap="round"/>
  </g>
</svg>

<!-- UNEVOC -->
<div style="position: fixed; bottom: 1px; left: 20px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/UNESCO-UNEVOC_logo.png?raw=true" alt="UNEVOC Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">UNEVOC</div>
</div>

<!-- ASSET -->
<div style="position: fixed; bottom: 1px; left: 180px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/ASSET_icon.png?raw=true" alt="ASSET Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">ASSET</div>
</div>

<!-- HWK Blume -->
<div style="position: fixed; bottom: 1px; left: 340px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/HWK_Blume.png?raw=true" alt="HWK Blume Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 7px;">HWK Blume</div>
</div>

<!-- GIZ -->
<div style="position: fixed; bottom: 1px; left: 500px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/giz-logo.gif?raw=true" alt="GIZ Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">GIZ</div>
</div>

<!-- UoVT -->
<div style="position: fixed; bottom: 1px; left: 660px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/UoVT_Logo.png?raw=true" alt="UoVT Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">UoVT</div>
</div>

<!-- OVGU -->
<div style="position: fixed; bottom: 1px; left: 820px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/Masub27/Intro/blob/main/ovgu.png?raw=true" alt="OVGU Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">OVGU</div>
</div>

<!-- HRDC -->
<div style="position: fixed; bottom: 1px; left: 980px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/hrdc_logo.png?raw=true" alt="HRDC Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">HRDC</div>
</div>

<!-- MITD -->
<div style="position: fixed; bottom: 1px; left: 1140px; opacity: 0.9; z-index: 1000; text-align: center; width: 100px;">
  <img src="https://github.com/OVGU-VET-TechEd/ASSET_UNESCO_Coinitiative/blob/main/media/mitd_logo.png?raw=true" alt="MITD Logo" style="height: 60px; width: auto; border-radius: 10px;" />
  <div style="font-size: 0.8em; color: #555; margin-top: 5px;">MITD</div>
</div>
