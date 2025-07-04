from agents.tool import function_tool
@function_tool()
async def meal_plan(diet_type: str = "balanced") -> dict:
    """
    Suggests a meal plan based on dietary preference.
    """
    return {
        "Monday": "Grilled chicken with veggies (500 kcal)",
        "Tuesday": "Lentil soup and whole grain bread (450 kcal)",
        "Wednesday": "Tofu stir-fry with brown rice (520 kcal)",
        "Thursday": "Salmon salad with avocado (480 kcal)",
        "Friday": "Vegetable pasta (500 kcal)",
        "Saturday": "Chickpea curry and rice (530 kcal)",
        "Sunday": "Zucchini noodles and pesto (460 kcal)",
        "Diet Type": diet_type
    }
