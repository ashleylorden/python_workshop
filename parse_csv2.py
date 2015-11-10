import csv
# regex is a powerful tool to parse values from blobs of text
import re

csv_file = 'workshop_details.csv'

with open(csv_file, 'rb') as data:
    reader = csv.reader(data)

    # Skip header row
    next(reader, None)

    # initialize some variables to use in the loop
    total_time = 0
    num_times_tallied = 0

    for row in reader:
        # calculate average time people want to spend on workshop
        # try to get an integer from the string
        try:
            hours_text = row[3]
            # this regex statement will find numerical values (\d+) in the text
            hours_int = int(re.search(r'\d+', hours_text).group())
            # at this point, if there was not a number in the string,
            # forcing it to int(None) would error so we'll jump to except clause.

            # I know I have an integer if I made it here, so save that value
            total_time += hours_int
            num_times_tallied += 1
        except:
            # Use string formatting to insert values into a statement
            print 'Could not find number of hours in "{}"'.format(row[3])

average_hours = total_time/num_times_tallied
print 'Average length requested for python workshop: {} hours; {} votes'.format(
    average_hours, num_times_tallied
)
