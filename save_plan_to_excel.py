def save_plan_to_excel(plan_text: str, file_path="diet_plan.xlsx"):
    import pandas as pd
    days = plan_text.strip().split("Day ")[1:]
    rows = []

    for day_text in days:
        lines = day_text.strip().splitlines()
        day_num = lines[0].strip(":")
        current_meal = None
        meal_data = {}

        for line in lines[1:]:
            if line.startswith("Meal"):
                if meal_data:
                    rows.append(meal_data)
                    meal_data = {}
                current_meal = line.strip()
                meal_data = {"Day": f"Day {day_num}", "Meal": current_meal}
            elif "Dish:" in line:
                meal_data["Dish"] = line.split("Dish:")[1].strip()
            elif "Time:" in line:
                meal_data["Time"] = line.split("Time:")[1].strip()
            elif "Calories:" in line:
                meal_data["Calories"] = line.split("Calories:")[1].strip()
            elif "Reason:" in line:
                meal_data["Purpose"] = line.split("Reason:")[1].strip()

        if meal_data:
            rows.append(meal_data)

    df = pd.DataFrame(rows)
    df.to_excel(file_path, index=False)
