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

#displaying how many rows the data containes after filtering
print(len(state_data))

# function that returns a list that contains data according to two given parameters state and column
# when retrieving data with the column key, dictionaries with an empty value at the key are not added to the list
def filter(state, column):
    state_data = [sta for sta in list_data if sta["STATE"] == state and sta[column] != ""]
    return state_data

