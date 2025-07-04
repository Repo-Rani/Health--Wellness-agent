from agents.tool import function_tool
@function_tool()
def update_progress(metric: str, value: str) -> dict:
    """
    Updates and returns the user's tracked metric.
    """
    return {
        "status": "success",
        "updated_metric": metric,
        "new_value": value,
        "message": f"📊 Your {metric} has been updated to {value}!"
    }
