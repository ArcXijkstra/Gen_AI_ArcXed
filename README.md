## 📘 Gen_AI_ArcXed – Agent-Based Personalized Learning Platform

### 📌 Overview
Gen_AI_ArcXed is a personalized education platform leveraging **multi-agent LLM-based systems** to simulate an intelligent tutor. The system provides adaptive feedback and dynamic study plans based on student self-evaluation, conceptual understanding, and syllabus mapping.

### 🎯 Objective
To automate and personalize the learning journey of students by using Generative AI to:
- Generate conceptual diagnostic questions.
- Evaluate student answers using LLMs.
- Recommend a chapter-wise study plan with adaptive feedback and revision timelines.

### 🧠 Key Components
- **Agent-Oriented Design**  
  Each task is handled by a dedicated AI agent built using a modular prompt-based system.

- **Dynamic Question Generator**  
  For each chapter and subject, two conceptual questions are generated using:
  - The syllabus structure.
  - Student's self-rated knowledge.

- **Answer Evaluator**  
  Evaluates student responses and estimates subject-wise understanding (0–10 scale) using context-aware reasoning.

- **Study Plan Generator**  
  Produces a structured, JSON-based weekly plan including:
  - Time estimates.
  - Topic priorities.
  - Confidence levels.
  - Resource recommendations.

### 📊 Output Format
Each module generates structured JSON output, making the results easy to visualize, monitor, or plug into external dashboards.
