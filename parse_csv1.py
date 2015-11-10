# Import statements allow us to use helpful libraries
import csv

# Constants make the code easier to read and edit
# (for instance, if the filename changes I only have to edit in one place)
csv_file = 'workshop_details.csv'

# Open CSV file
with open(csv_file, 'rb') as data:
    # Consume the data in the csv
    reader = csv.reader(data)
    # Iterate through each item in the data
    for row in reader:
        # Print data from the row to verify it's working
        print row[1]
        '''
        Notice Python treats each row like a list:
        [Timestamp, Username, What level of experience do you have?, ...]
        so if you want to access column A - Timestamp, use row[0];
        column B - Username, row[1] etc.
        '''
