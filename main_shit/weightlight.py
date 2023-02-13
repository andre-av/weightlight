from typing import List
import datetime
import csv




class ExerciseSet:
    def __init__(self, name, weight, reps, rir, importance, date_done = datetime.datetime.now()):
        self.__name = name
        self.__weight = weight
        self.__reps = reps
        self.__rir = rir # Reps in reserve.
        self.__importance = importance # 1 for primary, 2 for secondary, 3 for tertiary.
        self.__date_done = date_done 

    @property
    def all_attributes(self):
        return [self.__name, self.__weight, self.__reps, self.__rir, self.__importance, self.__date_done.strftime("%c")]
    @property
    def name(self):
        return self.__name
    @property
    def weight(self):
        return self.__weight
    @property
    def reps(self):
        return self.__reps
    @property
    def rir(self):
        return self.__rir
    @property
    def importance(self):
        return self.__importance
    @property
    def date_done(self):
        return self.__date_done

class MuscleGroup:
        
    def __init__(self, name):

        self.__name = name
        self.__exercise_sets = [] # Array of ExerciseSet's

    @property
    def name(self):
        return self.__name
    @property
    def exercise_sets(self):
        return self.__exercise_sets
    
    @property
    def latest_set(self):
        return self.exercise_sets[-1]
    @property
    def all_sets_attributes(self): 
        sets_attributes = []
        for set in self.exercise_sets:
            sets_attributes.append(set.all_attributes)
        return sets_attributes
    @property
    def amount_sets_done(self, days = 28): # TODO like this, or kwargs?
        prim_sum = 0
        sec_sum = 0
        tert_sum = 0
        for set in self.exercise_sets:
            if set.date_done > datetime.datetime.now() - datetime.timedelta(days=days):
                prim_sum += 1 if set.importance == 1 else 0
                sec_sum += 1 if set.importance == 2 else 0
                tert_sum += 1 if set.importance == 3 else 0
        return prim_sum, sec_sum, tert_sum
    
    def incrementSets(self, exercise_name, weight, reps, rir, importance, date = datetime.datetime.now()):
        self.exercise_sets.append(ExerciseSet(exercise_name, weight, reps, rir, importance, date))


class WorkoutProgram:
    def __init__(self):

        self.__muscles = {}
        with open("musclegroups.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                self.__muscles[row[0]] = MuscleGroup(row[0])
    
    @property
    def muscles(self):
        return self.__muscles
    
    def doExerciseSet(self, exercise_name, weight, reps, rir, date_done = datetime.datetime.now()):
        def searchExercise(exercise_name):
            with open('exercises.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['name'] == exercise_name:
                        primary_muscles = row['primary muscles'].split(',') 
                        secondary_muscles = row['secondary muscles'].split(',') 
                        tertiary_muscles = row['tertiary muscles'].split(',') 
                        return primary_muscles, secondary_muscles, tertiary_muscles
            return None

        prim_sec_tert = searchExercise(exercise_name)
        if prim_sec_tert is not None: 
            primary_muscles, secondary_muscles, tertiary_muscles = prim_sec_tert
            for muscle in primary_muscles:
                if muscle in self.muscles:
                    self.muscles[muscle].incrementSets(exercise_name, weight, reps, rir, 1, date_done)
            for muscle in secondary_muscles:
                if muscle in self.muscles:
                    self.muscles[muscle].incrementSets(exercise_name, weight, reps, rir, 2, date_done)
            for muscle in tertiary_muscles:
                if muscle in self.muscles:
                    self.muscles[muscle].incrementSets(exercise_name, weight, reps, rir, 3, date_done)
                    
    @property
    def all_muscles_sets(self):
        for muscle in self.muscles.values():
            print(f'{muscle.name}: {muscle.amount_sets_done}')



program = WorkoutProgram()
program.doExerciseSet("deadlift", 20, 5, 1)
print("all sets done:")
print(program.all_muscles_sets)

# program.doExerciseSet("deadlift", 20, 5, 1)
# program.doExerciseSet("bench press", 20, 5, 1)
# program.doExerciseSet("pronated pullups", 0, 12, 0)
# program.doExerciseSet("pronated pullups", 0, 8, 1)
# program.doExerciseSet("pronated pullups", 0, 7, 0)
# print(program.muscles["glutes"].all_sets_attributes)
# print(program.muscles["glutes"].amount_sets_done)
