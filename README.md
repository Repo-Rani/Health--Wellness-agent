Health & Wellness Planner Agent
Welcome to the Health & Wellness Planner Agent, an AI-powered assistant designed to help users achieve their fitness and dietary goals through personalized meal plans, workout recommendations, and progress tracking. Built with the OpenAI Agents SDK and integrated with Chainlit for a seamless, chatbot-like user experience, this project showcases a modular, scalable, and interactive AI system.
🌟 Features

Multi-Turn Conversations: Engage in natural language interactions to set and refine health goals.
Personalized Plans: Generate 7-day meal plans and workout routines tailored to user preferences (e.g., vegetarian, keto) and fitness goals.
Context Management: Persist user data across sessions using a Pydantic-based UserSessionContext.
Guardrails: Validate inputs (e.g., "lose 5kg in 2 months") and ensure structured JSON outputs for reliability.
Agent Handoffs: Seamlessly delegate to specialized agents for nutrition, injury support, or human coach escalation.
Real-Time Streaming: Stream responses for an engaging, real-time chat experience via Chainlit.
Progress Tracking: Log user progress and schedule weekly check-ins.
Lifecycle Hooks: Optional logging of agent and tool events for debugging and analytics.
Bonus Feature: Generate PDF progress reports (optional, using reportlab).

📂 Project Structure
health_wellness_agent/
├── main.py                    # Entry point with Chainlit UI integration
├── agent.py                   # Main Health & Wellness Agent logic
├── context.py                 # UserSessionContext for state management
├── guardrails.py              # Input/output validation logic
├── hooks.py                   # Lifecycle hooks for logging
├── tools/                     # Tool implementations
│   ├── goal_analyzer.py       # Parse user goals
│   ├── meal_planner.py        # Generate meal plans
│   ├── workout_recommender.py # Suggest workout plans
│   ├── scheduler.py           # Schedule progress check-ins
│   ├── tracker.py             # Track user progress
├── agents/                    # Specialized agent implementations
│   ├── escalation_agent.py    # Handle human coach requests
│   ├── nutrition_expert_agent.py # Address complex dietary needs
│   ├── injury_support_agent.py # Adjust plans for injuries
├── utils/                     # Utility functions
│   └── streaming.py           # Streaming response handler
└── README.md                  # Project documentation

🚀 Getting Started
Prerequisites

Python 3.8 or higher
Git (for cloning the repository)
A terminal or command prompt

Installation

Clone the Repository:
git clone https://github.com/your-username/health-wellness-agent.git
cd health-wellness-agent


Set Up a Virtual Environment (recommended):
python -m venv venv


On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate


Install Dependencies:
pip install openai-agents chainlit pydantic reportlab

Note: The openai-agents package is assumed to be the SDK for this project. If unavailable, check the assignment or SDK documentation for alternatives. reportlab is optional for PDF generation.

Run the Application:
chainlit run main.py

Open http://localhost:8000 in your browser to interact with the agent.


🧭 Usage

Launch the App: Start the Chainlit server with the command above.
Interact via Chat:
Set a goal: "I want to lose 5kg in 2 months"
Specify diet: "I'm vegetarian"
Request workouts: "Give me a workout plan"
Report progress: "Update my progress: Lost 1kg"
Handle special cases: "I have knee pain" or "I'm diabetic"
Escalate: "I want to talk to a human coach"


View Responses: The agent streams responses in real-time, providing meal plans, workout suggestions, or handoffs to specialized agents.

🔧 Tools and Agents
Tools

GoalAnalyzerTool: Parses goals (e.g., "lose 5kg in 2 months") into structured format.
MealPlannerTool: Generates a 7-day meal plan based on dietary preferences.
WorkoutRecommenderTool: Suggests workouts tailored to user goals.
CheckinSchedulerTool: Schedules weekly progress check-ins.
ProgressTrackerTool: Logs user progress updates.

Specialized Agents

EscalationAgent: Connects users to a human coach.
NutritionExpertAgent: Handles complex dietary needs (e.g., diabetes, allergies).
InjurySupportAgent: Adjusts plans for physical limitations or injuries.

🔒 Guardrails

Input Validation: Ensures goals follow the format "lose/gain X kg/lbs in Y months/weeks" and validates dietary preferences.
Output Validation: Tools return structured JSON or Pydantic models for consistency.

🔄 Streaming
Real-time responses are streamed using Runner.stream from the OpenAI Agents SDK, integrated with Chainlit for a smooth chat experience.
📊 Example Interaction
User: I want to lose 5kg in 2 months
Agent: {"status": "success", "goal": {"quantity": 5.0, "metric": "kg", "duration": "2 months"}}

User: I'm vegetarian
Agent: {"status": "success", "meal_plan": ["Vegetarian Meal 1", ..., "Vegetarian Meal 7"]}

User: I have knee pain
Agent: Workout plan adjusted for injury: knee pain

User: I'm diabetic
Agent: Nutrition plan tailored for diabetes created.

User: Schedule a checkin
Agent: {"status": "success", "next_checkin": "2025-07-19 22:00:00"}

🛠️ Bonus Features

PDF Progress Reports: Generate a PDF summary of user progress (requires reportlab).
Streamlit Alternative: Swap Chainlit for Streamlit by modifying main.py (see implementation details in the project code comments).

🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

📝 License
This project is licensed under the MIT License. See the LICENSE file for details.
🙌 Acknowledgments

Built with the OpenAI Agents SDK and Chainlit.
Inspired by real-world AI-driven health and wellness applications.
Thanks to the open-source community for tools like Pydantic and reportlab.


For issues or suggestions, please open an issue on the GitHub repository. Happy coding and stay healthy! 💪
