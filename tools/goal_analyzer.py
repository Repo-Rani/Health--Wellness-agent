from agents.tool import function_tool
@function_tool()
def analyze_goals(goal_description: str) -> dict:
    """
    Parse user's natural language goals and return a structured dictionary.
    """
    if "weight loss" in goal_description.lower():
        return {
            "goal_type": "Weight Loss",
            "target_duration": "3 months",
            "focus_area": "Full Body",
            "additional_info": "Moderate exercise"
        }
    return {
        "goal_type": "General Fitness",
        "target_duration": "unspecified",
        "focus_area": "unspecified",
        "additional_info": "Need more details"
    }
