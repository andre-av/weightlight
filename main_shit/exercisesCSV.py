import csv

header = ["name", "primary muscles", "secondary muscles", "tertiary muscles"]

def create_exercises_csv():
    with open("exercises.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()

def add_exercise_to_csv(name, primary_muscles: str, secondary_muscles: str, tertiary_muscles: str):
    with open("exercises.csv", "r") as f:
        reader = csv.reader(f)
        next(reader) # Skip header.
        exercise_names = [row[0] for row in reader]
        if name in exercise_names:
            print(f"Exercise '{name}' already exists in exercises.csv")
            return
    with open("exercises.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, primary_muscles, secondary_muscles, tertiary_muscles])


# create_exercises_csv()
# add_exercise_to_csv("deadlift", "lower back, glutes, hamstrings", "quadriceps, upper traps", "abs")
# add_exercise_to_csv("bench press", "lower pectorals", "triceps, upper pectorals, anterior deltoids", "")
# add_exercise_to_csv("pronated pullups", "lats", "middle traps", "biceps, posterior deltoids")

