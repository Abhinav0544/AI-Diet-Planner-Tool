from llama_helper import ask_llama

def build_diet_prompt(user_context: str, cuisine: str = None) -> str:
    cuisine_text = f"Preferred Cuisine: {cuisine}." if cuisine else ""
    return f"""
You are a certified nutritionist and AI health expert.

Using the following user profile:
{user_context}
{cuisine_text}

Generate a clean and structured 7-day diet plan in this format:

Day 1:
Meal 1: 
- Dish: [Name of dish]
- Time: [e.g., 8:00 AM]
- Calories: [e.g., 350]
- Reason: [e.g., Provides sustained energy for the morning.]

Meal 2: 
- Dish: ...
- Time: ...
- Calories: ...
- Reason: ...

Day 2:
...

Ensure:
- Calorie count per day is close to {user_context.split("Suggested Daily Calorie Limit:")[-1].strip()} kcal.
- Dish names should be real, regional if applicable, and nutritious.
- Avoid repetition.
- Use clear formatting as shown above.
- Meals should align with user’s diet type and health conditions.
- Return ONLY the diet plan (no intro, no conclusion).
IMPORTANT: Your response MUST include diet plans for ALL 7 days (Day 1 through Day 7), without skipping any day.


Let's begin:
"""


def generate_diet_plan(user_description: str, cuisine: str = None, max_tokens=2048) -> str:
    prompt = build_diet_prompt(user_description, cuisine)
    response = ask_llama(prompt, max_tokens=max_tokens)
    return response

