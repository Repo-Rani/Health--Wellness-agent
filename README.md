# 🧠 Health & Wellness Planner Agent 🏋️‍♀️🍎

A powerful AI-driven digital assistant built using the **OpenAI Agents SDK**, designed to help users achieve their health and wellness goals through personalized meal plans, workout routines, and progress tracking — all through **natural language conversation**.

This agent can understand user needs, generate structured plans, stream responses in real-time, and even intelligently hand off to specialized sub-agents like a **Nutrition Expert** or **Injury Support Assistant**.

---

## 🌟 Features

✅ Collect and understand fitness & dietary goals  
✅ Generate 7-day meal and workout plans  
✅ Real-time streaming conversation via `Runner.stream()`  
✅ Context-aware memory of previous chats  
✅ Schedule weekly check-ins  
✅ Track progress updates  
✅ Delegate to expert agents based on user needs  
✅ Guardrails for validated, safe, and structured interaction  
✅ Optional lifecycle hook support for logging & tracking

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| `GoalAnalyzerTool` | Converts free-text goals into structured format |
| `MealPlannerTool` | Provides async 7-day meal plans with dietary preferences |
| `WorkoutRecommenderTool` | Suggests fitness plans based on goals and history |
| `CheckinSchedulerTool` | Schedules weekly progress check-ins |
| `ProgressTrackerTool` | Logs progress and updates user session state |

---

## 🤖 Specialized Agents (via Handoff)

| Agent Name | Trigger |
|------------|---------|
| `EscalationAgent` | When user wants to speak with a human trainer |
| `NutritionExpertAgent` | For complex diets (e.g., diabetes, allergies) |
| `InjurySupportAgent` | For injury-based workout modifications |

---

## 📦 Project Structure

health_wellness_agent/
├── main.py # Entry point
├── agent.py # Main agent with tools & handoffs
├── context.py # Shared user context (state)
├── guardrails.py # Input/output validation
├── hooks.py # Optional lifecycle hooks
├── tools/
│ ├── goal_analyzer.py
│ ├── meal_planner.py
│ ├── workout_recommender.py
│ ├── scheduler.py
│ └── tracker.py
├── agents/
│ ├── escalation_agent.py
│ ├── nutrition_expert_agent.py
│ └── injury_support_agent.py
├── utils/
│ └── streaming.py # Real-time stream utility
└── README.md 


---

## 🧑‍💻 How to Clone and Run

### 1️⃣ Clone this repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

⚙️ Technologies Used
Python 3.10+

OpenAI Agents SDK

Pydantic

asyncio for concurrent tools

Optional: Chainlit for frontend (can be added)
