from agents.tool import function_tool
@function_tool()
def schedule_checking(day: str = "Sunday", time: str = "10:00 AM") -> dict:
    """
    Returns a confirmation message for weekly check-in schedule.
    """
    return {
        "message": f"✅ Progress check scheduled every {day} at {time}. Stay on track!"
    }
