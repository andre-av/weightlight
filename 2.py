
from typing import List
from datetime import date
import csv


class MuscleGroup:
    def __init__(self, name):
        self.primary = 0
        self.secondary = 0
        self.tertiary = 0
        self.name = name

    def add_primary_sets(self, sets):
        self.primary += sets

    def add_secondary_sets(self, sets):
        self.secondary += sets

    def add_tertiary_sets(self, sets):
        self.tertiary += sets

class WorkoutProgram:
    def __init__(self):
        self.muscle_groups = {
            "quads": MuscleGroup("quads"),
            "glutes": MuscleGroup("glutes"),
            "hamstrings": MuscleGroup("hamstrings"),
            "calves": MuscleGroup("calves"),
            "lats": MuscleGroup("lats"),
            "biceps": MuscleGroup("biceps"),
            "traps": MuscleGroup("traps"),
            "mid traps": MuscleGroup("mid traps"),
            "posterior deltoids": MuscleGroup("posterior deltoids"),
            "forearms pull": MuscleGroup("forearms pull"),
            "pectorals": MuscleGroup("pectorals"),
            "anterior deltoids": MuscleGroup("anterior deltoids"),
            "mid deltoids": MuscleGroup("mid deltoids"),
            "triceps": MuscleGroup("triceps"),
            "forearms push": MuscleGroup("forearms push"),
            "traps": MuscleGroup("traps"),
            "obliques": MuscleGroup("obliques"),
            "lower back": MuscleGroup("lower back"),
            "abs": MuscleGroup("abs"),
            "obliques": MuscleGroup("obliques")
        }
        self.exercises = {}
    
    def add_exercise(self, exercise_name, primary_muscles, secondary_muscles, tertiary_muscles):
        self.exercises[exercise_name] = {"primary_muscles": primary_muscles, "secondary_muscles": secondary_muscles, "tertiary_muscles": tertiary_muscles}
    
    def do_exercise(self, exercise_name, sets, reps):
        exercise = self.exercises.get(exercise_name)
        if exercise is None:
            print(f"Exercise {exercise_name} not found.")
            return
        for muscle in exercise["primary_muscles"]:
            self.muscle_groups[muscle].add_primary_sets(sets)
        for muscle in exercise["secondary_muscles"]:
            self.muscle_groups[muscle].add_secondary_sets(sets)
        for muscle in exercise["tertiary_muscles"]:
            self.muscle_groups[muscle].add_tertiary_sets(sets)
    
    def get_week_sets(self):
        week_sets = {}
        for muscle in self.muscle_groups:
            week_sets[muscle] = self.muscle_groups[muscle].get_week_sets()
        return week_sets

program = WorkoutProgram()
program.add_exercise("pull-ups", ["lats"], ["mid traps"], ["biceps"])
program.add_exercise("dips", ["triceps", "pectorals"], ["anterior deltoids"], ["mid deltoids"])
# program.add_exercise("squats", ["quads", "glutes", "hamstrings"], ["erector spinae"], ["calves"])
program.do_exercise("pull-ups", 3, 10)
program.do_exercise("dips", 4, 8)
# program.do_exercise("squats", 5, 5)
print(program.get_week_sets())