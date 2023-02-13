


# Workout
# Do exercise:
# for every set:
#   increment sum of sets for primary/secondary/tert muscle groups of exercise
#   eg. bench press: primary chest, secondary front delt, triceps
#       after 3 sets, chest has 3 primary sets, frontdelt and tris have 3 secondary

# as you go through week, you see which muscle groups have been worked enough/too much
#   eg. chest 30 sets, quads 0 
# you'll also see if you overdid sets to failure


# Later on in project:
#   see progress, based on reps&weight per set

from typing import List
from datetime import date
import csv


# class MuscleGroupList():
class MuscleGroup():
    
    def __init__(self, name):

        self.__name = name

        self.__sets = {}

        self.__sets["in_workout"] = {}
        self.__sets["in_week"] = {}

        # for period_type in self.__sets:
        #     period_type["primary"] = 0
        #     period_type["secondary"] = 0
        #     period_type["tertiary"] = 0
        #     period_type["to_failure"] = 0
        #     period_type["low_reps"] = 0
        #     period_type["mid_reps"] = 0
        #     period_type["high_reps"] = 0

        self.__sets["in_workout"]["primary"] = []
        self.__sets["in_workout"]["secondary"] = []
        self.__sets["in_workout"]["tertiary"] = []
        self.__sets["in_workout"]["to_failure"] = []
        self.__sets["in_workout"]["low_reps"] = []
        self.__sets["in_workout"]["mid_reps"] = []
        self.__sets["in_workout"]["high_reps"] = []

        self.__sets["in_week"]["primary"] = []
        self.__sets["in_week"]["secondary"] = []
        self.__sets["in_week"]["tertiary"] = []
        self.__sets["in_week"]["to_failure"] = []
        self.__sets["in_week"]["low_reps"] = []
        self.__sets["in_week"]["mid_reps"] = []
        self.__sets["in_week"]["high_reps"] = []

        # self.dates_done

    def printStats(self):
        print("Stats for", self.__name)
        for period in self.__sets:
            for set_type in self.__sets[period]:
                print(period, "\t", set_type, ":\t", self.__sets[period][set_type])

    def incrementSets(self, exercise_type:str, date): # TODO WHERE do I put this?
        self.__sets["in_workout"][exercise_type].append(date)
        self.__sets["in_week"][exercise_type].append(date)

    def resetSets(self, period_type:str): # Reset in_week or in_workout sets 
        for set_type in self.__sets[period_type]:
            self.__sets[period_type][set_type] = []


# TODO prettier way to store the list of muscles?
muscle_types = ["upper_chest","lower_chest","triceps","front_delts","mid_delts",
                "mid_back","lats","traps","biceps","rear_delt",
                "quads","hams","glutes","calves",
                "upper_abs","lower_abs","obliques",
                "neck","forearm_pull","forearm_push"]
muscle_list = {}
for muscle_type in muscle_types:
    muscle_list[muscle_type] = MuscleGroup(muscle_type)


class Exercise():

    # all = []
    
    def __init__(self, primary:List[str], secondary:List[str], tertiary:List[str]):
        self.__primary = primary
        self.__secondary = secondary
        self.__tertiary = tertiary

    @property
    def primaryMuscleList(self):
        return self.__primary

    @property
    def secondaryMuscleList(self):
        return self.__secondary
    
    @property
    def tertiaryMuscleList(self):
        return self.__tertiary
    
exercise_list = {}
# Push exercises
exercise_list["bench_press"] = Exercise(["upper_chest", "lower_chest"],
                                        ["front_delts", "triceps"], 
                                        [])
exercise_list["dips"] = Exercise(["lower_chest", "triceps"], 
                                ["front_delts"], 
                                [])
exercise_list["delt_press"] = Exercise(["mid_delts"],
                                        ["front_delts", "triceps"], 
                                        ["upper_chest"])
# ...
# Pull exercises
exercise_list["pullups"] = Exercise(["lats"],
                                    ["mid_back"], 
                                    ["biceps"])
# Leg exercises
# Misc exercises
# ...
    
class Set():
    # reps = 0
    # weight = 0
    # post_pause = 0

    def __init__(self, exercise:str, reps:int, weight:int, post_pause:int, thing:MuscleGroup):

        # TODO date in which exercise set was done
        # date = 

        primaries = exercise_list[exercise].primaryMuscleList
        secondaries = exercise_list[exercise].secondaryMuscleList
        tertiaries = exercise_list[exercise].tertiaryMuscleList

        for muscle in primaries:
            muscle_list[muscle].incrementSets("primary", 1)
            print(muscle)
        for muscle in secondaries:
            muscle_list[muscle].incrementSets("secondary", 1)
            print(muscle)
        for muscle in tertiaries:
            muscle_list[muscle].incrementSets("tertiary", 1)
            print(muscle)
        

class User():
    pass
    


set = Set('bench_press', 1, 1, 1)
# print(muscle_list["upper_chest"])

muscle_list["upper_chest"].printStats()

# print(exercise_list["bench_press"].primaryMuscleList)



# print("Enter exercises and sets for Monday")
# # get exercises: on site it will be a checklist of exercises, sets and reps
# thing = input()
# print("lol,", thing)




