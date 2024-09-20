import os
import csv

# Directory containing the CSV files
directory = 'meets'
output_file = 'index.html'

# Create the HTML content template
html_start = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
    <title>Cross Country Meet Summaries</title>
</head>
<body>

<header>
    <h1>Cross Country Meet Summaries</h1>
</header>

<main>
    <section id="meets-section">
"""

html_end = """
    </section>
</main>

<footer>
    <p>Cross Country Meet Summaries &copy; 2024</p>
</footer>

</body>
</html>
"""

# Prepare to store all meet summaries
html_content = html_start

# Function to find the index of a row by its content
def find_row_index(rows, keywords):
    for i, row in enumerate(rows):
        if ','.join(row).strip().lower() == keywords.strip().lower():
            return i
    return None

# Loop through files in the directory
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path) and file_name.endswith('.csv'):
        csv_file = file_path

        # Open the CSV file and extract the data
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Parse metadata from the first few lines of the CSV file
        meet_name = rows[0][0]
        meet_date = rows[1][0]
        meet_link = rows[2][0]

        # Find the index for team results
        team_results_start_index = find_row_index(rows, 'Place,Team,Score')

        # Skip the file if the required headers are not found
        if team_results_start_index is None:
            print(f"Skipping {file_name}: Could not find required headers.")
            continue

        # Adjust start index for team results
        team_results_start_index += 1

        # Add the meet header and link to the HTML
        html_content += f"""
        <div class="meet">
            <h2>{meet_name}</h2>
            <h3>{meet_date}</h3>
            <p><a href="{meet_link}">Full results available here.</a></p>
        """

        # Add team results to HTML
        html_content += """
        <section class="team-results">
            <h4>Team Results</h4>
            <table>
                <thead>
                    <tr>
                        <th>Place</th>
                        <th>Team</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody>
        """

        # Loop through the team results and stop when the individual athlete header is encountered
        for row in rows[team_results_start_index:]:
            if len(row) < 3:
                continue  # Skip incomplete rows

            # Stop if the row contains the athlete data header
            if ','.join(row).strip().lower() == 'place,grade,name,athlete link,time,team,team link,profile pic':
                break

            # Add the team results to the HTML
            html_content += f"""
                    <tr>
                        <td>{row[0]}</td>
                        <td>{row[1]}</td>
                        <td>{row[2]}</td>
                    </tr>
            """

        html_content += """
                </tbody>
            </table>
        </section>
        </div>
        """

# After processing all the meets, finalize the HTML content
html_content += html_end

# Write the complete HTML content to the output file
with open(output_file, 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)


