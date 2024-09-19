import csv
import os

directory = 'meets'
output_file = "index.html"

# Create the HTML content
page = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <title>Cross Country Coaching Events</title>
</head>
<body>

<header>
    <h1>Cross Country Events Tracker</h1>
</header>

<main>
    
    <section id="meets-section">
        <h2>Cross Country Meet Summaries</h2>

        <h3>{{meet_name}}</h3>
        <h4>{{meet_date}}</h4>

        <h5>Overall Team Results</h5>
        <p><a href="{{team_results_link}}">Team results are available here.</a></p>
    
        <p>{{team_name}}: {{team_score}}</p>
        <figure>
            <img src="{{image_url}}" alt="Athlete at {{meet_name}}">
            <figcaption>Gallery 

            """



# Loop through files in the directory
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path) and file_name.endswith('.csv'):
        csv_file = file_path  # Correct file path handling

        # Open the CSV file and extract the data
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)

        # Ensure there are enough rows to prevent index errors
        if len(data) < 7:
            print(f"Error: CSV file {csv_file} doesn't contain enough rows for valid data extraction.")
            continue

        # Extract metadata based on CSV structure
        meet_name = data[0][0] if len(data[0]) > 0 else "Unknown Meet"  # Meet Name
        meet_date = data[1][0] if len(data[1]) > 0 else "Unknown Date"  # Meet Date
        team_results_link = data[2][0] if len(data[2]) > 0 else "#"  # Team results link
        team_name = data[3][0] if len(data[3]) > 0 else "Unknown Team"  # Team Name
        team_score = data[4][0] if len(data[4]) > 0 else "N/A"  # Team Score
        image_url = data[5][0] if len(data[5]) > 0 else "default_image.jpg"  # Image URL
        

        html_content = page.format(
            meet_name=meet_name,
            meet_date=meet_date,
            team_results_link=team_results_link,
            team_name=team_name,
            team_score=team_score,
            image_url=image_url
        )

        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

            # # Start processing athlete results from row 7 onwards
            # athlete_results = data[7:]  # Athlete data starts at index 7
            # athletes = []

            # # Add each athlete's information to the list
        # for row in athlete_results:
        #     if len(row) > 5:  # Ensure there's enough data in each row
        #         athlete_place = row[0]  # Place
        #         athlete_name = row[2]  # Athlete name (assuming it's in the third column)
        #         athlete_time = row[4]  # Time (assuming it's in the fifth column)

        #         athlete_info = {
        #             'place': athlete_place,
        #             'name': athlete_name,
        #             'time': athlete_time
        #         }
        #         athletes.append(athlete_info)


print(f"Meet Name: {meet_name}")
print(f"Meet Date: {meet_date}")
print(f"Team Results Link: {team_results_link}")
# print(f"Athlete Results: {athletes}")