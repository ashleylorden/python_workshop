import csv
# handy module to time executions of python code
import timeit

csv_file = 'workshop_details.csv'

with open(csv_file, 'rb') as data:
    reader = csv.reader(data)
    next(reader, None)

    # initialize some variables to use in the loop
    all_dates = []

    for row in reader:
        # find out how often a certain workshop date was chosen
        # convert a string with items separated by commas to a list of those items
        date_choices = row[4].split(', ')
        # save this list in a big list to use later
        all_dates.append(date_choices)

# now, calculate how often a date was chosen
date_to_check = 'Tue 11/10 6pm'

# breaking sections of code that complete a single purpose into functions or methods
# is a good practice.


# we could loop through the list to calculate this:
def calculate_votes_iterative():
    num_votes = 0
    for dates_chosen in all_dates:
        if date_to_check in dates_chosen:
            num_votes += 1
    return num_votes


# Python list comprehension is a tool to do the same thing as a loop over a list
def calculate_votes_list_comprehension():
    list_of_entries_for_selected_date = [
        date_to_check for dates_chosen in all_dates if date_to_check in dates_chosen
    ]
    return len(list_of_entries_for_selected_date)


# the reduce function can also extract data from a list
def calculate_votes_reduce():
    return reduce(
        lambda count, dates_chosen: count + (date_to_check in dates_chosen), all_dates, 0
    )


# a generator may be more efficient
def calculate_votes_sum():
    return sum(1 for dates_chosen in all_dates if date_to_check in dates_chosen)


# or, to simplify further
def calculate_votes_sum2():
    return sum(date_to_check in dates_chosen for dates_chosen in all_dates)


# check that these methods all work to return the same result
def test_calculate_votes():
    expected_result = 17
    assert calculate_votes_iterative() == expected_result
    assert calculate_votes_list_comprehension() == expected_result
    assert calculate_votes_reduce() == expected_result
    assert calculate_votes_sum() == expected_result
    assert calculate_votes_sum2() == expected_result

test_calculate_votes()

'''
how do we know which one to use since they all perform the same action?
code readability is really important, so it should be easy to read and understand
some of these create extra data we have to store in memory, that's a downside
generally the 'best' choice is the one that runs the fastest
if you're not working with very large datasets, it doesn't matter much so choose what you like
if you are expecting this list to be very very long, you can time them to see which performs:
'''

print 'Iterative: {}'.format(timeit.timeit(calculate_votes_iterative, number=100000))
print 'Comprehension: {}'.format(timeit.timeit(calculate_votes_list_comprehension, number=100000))
print 'Reduce: {}'.format(timeit.timeit(calculate_votes_reduce, number=100000))
print 'Sum: {}'.format(timeit.timeit(calculate_votes_sum, number=100000))
print 'Sum 2: {}'.format(timeit.timeit(calculate_votes_sum2, number=100000))

# So iterative is the fastest and is also simple to read and doesn't use additional memory.
# Sum is the second fastest so if you prefer more compact code you could choose that one.
