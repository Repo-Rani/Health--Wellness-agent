from agents.tool import function_tool
@function_tool()
def workout_plan(goal: str = "weight loss", experience_level: str = "beginner") -> dict:
    """
    Suggests a workout plan tailored to user's goals and fitness level.
    """
    base_plan = {
        "Monday": "Cardio (30 mins)",
        "Tuesday": "Full-body strength (20 mins)",
        "Wednesday": "Rest or yoga",
        "Thursday": "Upper body (30 mins)",
        "Friday": "Lower body (30 mins)",
        "Saturday": "HIIT or dance workout (25 mins)",
        "Sunday": "Light stretching & walk"
    }
    return {
        "Goal": goal,
        "Experience": experience_level,
        "Workout Plan": base_plan
    }
