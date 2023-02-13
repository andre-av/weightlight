import csv

def create_musclegroups_csv(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        # Legs
        writer.writerow(['quadriceps'])
        writer.writerow(['glutes'])
        writer.writerow(['hamstrings'])
        writer.writerow(['calves'])
        # Pull
        writer.writerow(['lats'])
        writer.writerow(['lower back'])
        writer.writerow(['biceps'])
        writer.writerow(['upper traps'])
        writer.writerow(['middle traps'])
        writer.writerow(['posterior deltoids'])
        writer.writerow(['forearms pull'])
        # Push
        writer.writerow(['upper pectorals'])
        writer.writerow(['lower pectorals'])
        writer.writerow(['anterior deltoids'])
        writer.writerow(['mid deltoids'])
        writer.writerow(['triceps'])
        writer.writerow(['forearms push'])
        # Abs
        writer.writerow(['obliques'])
        writer.writerow(['abs'])

def add_musclegroup_to_csv(filename, muscle_group):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([muscle_group])

create_musclegroups_csv("musclegroups.csv")