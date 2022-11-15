# edu-analysis
Analysis of changes in US education through years.

From the given data file I only extract data for the state of New York, where "AVG_MATH_4_SCORE" is not empty (state_data)

From the filtered list of dictionaries I created a list of available years (years)

Using list years and state_data, I calculated percentage change for "AVG_MATH_4_SCORE" for each pair of available years.

The result was stored into the list of dictionaries perchange_years.

It allows us to observe how the grades for "AVG_MATH_4_SCORE" were changing through years in the state of New York