import csv
# datetime is a very common module that helps work with date and time formats
from datetime import datetime

csv_file = 'workshop_details.csv'


# Object Oriented refers to using objects, which are instances of a class.
# To use OOP style we need to set up a class first, then we'll use it to structure our data.
class PythonWorkshopper(object):
    '''
    Attributes about a python workshop attendee, specified in a survey
    including what they'd like to accomplish in the workshop
    '''
    def __init__(self, username, timestamp, experience, goals):
        # email address of attendee
        self.username = username
        # datetime object of when survey was submitted
        self.time_submitted_survey = timestamp
        # string provided by attendee describing experience level
        self.experience_level = experience
        # list of strings, each of which is a skill the attendee would like to practice
        self.workshop_goals = goals

    '''
    some methods (a method is a function within a class) do things without any additional input
    using self, you can access everything defined within the class
    'self' is a parameter to every method, which means those methods can only be called on an instance of the class
    ocassionally methods are 'static' which means self is not required. Those can be called without an instance.
    '''
    def favorite_day_of_week(self):
        # datetime objects allow us to manipulate dates in many ways
        return self.time_submitted_survey.strftime('%A')

    def ambition_level(self):
        # a comment starting with 'TODO' is a common way to leave a note for something that will be addressed
        # TODO: resolve error case if goals is longer than 3
        levels = ['', 'slightly ambitious', 'somewhat ambitious', 'highly ambitious']
        return levels[len(self.workshop_goals)]

    # Methods can also do something without returning anything.
    def add_awesome(self):
        self.workshop_goals.append('be awesome')

    # This method requires an additional parameter be provided.
    def is_a_goal(self, proposed_skill):
        return proposed_skill in self.workshop_goals

    @staticmethod
    def learns_cool_python_things():
        return True

# notice that without instantiating the class, we can call static methods:
print PythonWorkshopper.learns_cool_python_things()


# now let's use the data from the CSV to create instances of the class for each person who signed up.
def load_data_from_csv():
    workshop_attendees = []
    with open(csv_file, 'rb') as data:
        reader = csv.reader(data)
        next(reader, None)
        for row in reader:
            # Convert from a string to a datetime object
            timestamp = datetime.strptime(row[0], '%m/%d/%Y %H:%M:%S')
            # Keep this as a string
            experience = row[2]
            # Convert to a list of strings, the separator between each item being ', '
            goals = row[5].split(', ')
            # Create an instance of the class using this information
            instance = PythonWorkshopper(row[1], timestamp, experience, goals)
            # Store those instances somewhere
            workshop_attendees.append(instance)
    return workshop_attendees


# we have a list of objects -- each instance of the PythonWorkshopper class is a PythonWorkshopper object.
def print_attendee_info(workshop_attendees):
    for workshopper in workshop_attendees:
        goal_today = 'Do stuff with data from a CSV'
        # Notice how I can call the object to get its attributes directly (like username), or call methods on it
        if workshopper.is_a_goal(goal_today):
            print 'Workshop attendee {} loves CSVs, {}s, and is {}'.format(
                workshopper.username, workshopper.favorite_day_of_week(), workshopper.ambition_level()
            )
        else:
            workshopper.add_awesome()

# Call the functions to perform the actions
attendee_list = load_data_from_csv()
print_attendee_info(attendee_list)
