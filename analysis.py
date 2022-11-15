import csv

#generating a list of dictionaries from 'states_all.csv'
with open ('states_all.csv', 'r') as data:
    reader = csv.DictReader(data)
    list_data = list(reader)

#finding and displaying the number of rows the data contains
data_length = len(list_data)
print(data_length)

#filtering list_data into state_data to only contain data for New York
state_data = [state for state in list_data if state["STATE"] == "NEW_YORK"]


#filtering out state_data to only contain dictionaries where "AVG_MATH_4_SCORE" is not an empty string
state_data = [state for state in state_data if state ["AVG_MATH_4_SCORE"] != ""]

print(state_data)

#displaying how many rows the data containes after filtering
print(len(state_data))

# function that returns a list that contains data according to two given parameters state and column
# when retrieving data with the column key, dictionaries with an empty value at the key are not added to the list
def filter(state, column):
 return [sta for sta in list_data if sta["STATE"] == state and sta[column] != ""]
    

#Lab part 2

# I created a list of all available years of state of New York, from previously filtered dictionaries
years = [state["YEAR"] for state in state_data if state["YEAR" ] != ""]
print(years)


def percent_change(lst, year1, year2):
    '''
    Function that extracts specific values with key "AVG_MATH_4_SCORE" for 2 years given as parameters. It returns the percentage change for the given years
    

    Parameters:
    -----------
    lst: The list of dictionaries is already filtered according to the state I chose - New York, and to nonempty value with key "AVG_MATH_4_SCORE"
    year1: specific year we need value of "AVG_MATH_4_SCORE"
    year2: specific year we need value of "AVG_MATH_4_SCORE"

    Returns:
    --------
    float: percentage change between two years
    '''
    val1 = [state["AVG_MATH_4_SCORE"] for state in lst if state["YEAR"] == year1]
    val2 = [state["AVG_MATH_4_SCORE"] for state in lst if state["YEAR"] == year2]
    
    val1 = float(val1[0])
    val2 = float(val2[0])
    return round((val1 - val2)/val1 * 100, 2)


# list that will hold dictionaries of each pair of years with percentage change for each pair
perchange_years = []

# we send each pair of years to the percent_change function and store it into dictionary, that gets added to the list
for i in range(0, len(years)):
    if i+1 <= len(years) - 1:
        year1 = years[i]
        year2 = years[i + 1]
        perchange_years.append({"range": year1+'-'+year2, "percentage_change": str(percent_change(state_data,year1,year2))})

print(perchange_years)