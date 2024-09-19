import csv
import os

directory = 'meet' #not sure if this is correctly getting to the folder
output_file = "LamplighterInvite23.html"

# Loop through files in the directory
for file_name in os.listdir(directory):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        # Open or process the file
    csv_file = file_name
# Open the CSV file and extract the data
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

# Extract the metadata
meet_name = data[0][0]  # Meet Name
meet_date = data[1][0]  # Meet Date
team_results_link = data[2][0]  # Team results link

# Start processing athlete results from row 7 onwards
athlete_results = data[7:]  # Athlete data starts at index 7
athletes = []

# Add each athlete's information to the list
for row in athlete_results:
    if len(row) > 1:  # Avoid empty rows
        athlete_place = row[0]  # Place
        athlete_name = row[1]  # Team (treated as athlete name)
        athlete_time = row[2]  # Score (treated as time)

        athlete_info = {
            'place': athlete_place,
            'name': athlete_name,
            'time': athlete_time
        }

        athletes.append(athlete_info)

# Print the extracted data for validation
print("Meet Name:", meet_name)
print("Meet Date:", meet_date)
print("Team Results Link:", team_results_link)
print("Race Comments:", race_comments)
print("Athlete Results:", athletes)



#replacing the values in the HTML
# html_content = 
# f'''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <link rel = "stylesheet" href = "css/reset.css">
#     <link rel = "stylesheet" href = "css/style.css">
#     <title>{meet_name} Country Meet</title>
# </head>
# <body>
#     <header>
#         <h1>{meet_name}</h1>
#         <h2>{meet_date}</h2>
#     </header>
#     <!-- Section for overall team results -->
#     <section id="team-results">
#         <h2>Overall Team Results</h2>
#         <p><a href="{team_results_link}">Team results are available here.</a></p>
#     </section>
#     <!-- Section for athlete table -->
#     <section id="athlete-results">
#         <h2>Athlete Results</h2>
#         <table id="athlete-table">
#             <thead>
#                 <tr>
#                     <th>Name</th>
#                     <th>Time</th>
#                     <th>Place</th>
#                     <th>Image</th>
#                     <th>Feedback</th>
#                 </tr>
#             </thead>
#             <tbody>
# '''
# Add each athlete's information to the table
for athlete in athletes:
    athlete_name = athlete[5]  # Column F - athlete-name
    # print(f"name {athlete_name}")
    athlete_place = athlete[7]  # Column G (updated) - athlete-place
    # print(f"place {athlete_place}")

