# This week’s challenge is to parse out City, State and ZIP code from some unformatted input data. 
# The data is in a nonstandard format - it is missing commas and some city names are two words 
# and some city name are only one word, making parsing a challenge.   
# You need to be able to parse out the city name, state, and zip code if available.

# Source: https://community.alteryx.com/t5/Weekly-Challenge/Challenge-54-Data-Prep-Address-Parsing/td-p/44255

Your goal is to create a process that will transform the data into a data table with separated columns for City, State, and ZIP.


# %% 
import pandas as pd

# %%
df = pd.read_csv("./challenge_54_input.csv")
df

# %%
df["Zip"] = df["Address Text"].str.extract(r'(\d{5})', expand = True)
df

# %%
df["State"] = df["Address Text"].str.extract(r'([A-Z]{2})', expand = True)
df

# %%
street_synonyms = ["Circle", "Street", "Drive", "Road", "Avenue", "Ave", "St"]


# %%
def find_city(address, state, street_synonyms):
    for syn in street_synonyms:
        if syn in address:
            # remove street
            city = address.split(syn)[-1]
            # remove State and postcode
            city = city.split(state)[0]
            return city


df['City'] = df.apply(lambda x: find_city(x['Address Text'], x['State'], street_synonyms), axis=1)
df
