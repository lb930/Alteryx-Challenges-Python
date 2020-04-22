# We have HTML data that is in a single field, the HTML contains an HTML Table.
# The input contains a series of name/value pairs within the description field. 
# The description field has a HTML table that contains 14 name/value contained within <td> tags. 
# Each pairing can be found on a different row (designated by the <tr> tag).
# The objective is to produce a table containing the 14 name/value pairs.

Source: https://community.alteryx.com/t5/Weekly-Challenge/Challenge-13-HTML-Table-Parsing/td-p/36741

import pandas as pd
import numpy as np

df = pd.read_csv(r"./challenge_13_input.csv")

# Splits the string into rows as we only want to keep rows containing the td tag
new_df = pd.DataFrame(df.Description.str.split('>').tolist(), index=df.RecordID).stack()
new_df = new_df.reset_index([0, 'RecordID'])
new_df.columns = ['RecordID', 'Description']
new_df

# Only keeps rows containing </td as those contain our names and values
new_df = new_df[new_df["Description"].str.contains("</td")]
new_df


# Drops first and last row as they don't contain relevant data
new_df.drop([9, 106], inplace = True)

# Create a function to reset the index as reset_index() isn't working
def reset_index_np(my_df):
    my_df.index = np.arange(len(my_df))
    return my_df

# Resets the index (drop index wasn't working)
reset_index_np(new_df)
new_df

# Cleans the strings before the df is split into 2 parts
new_df["Description"] = new_df["Description"].str.replace("</td", "")
#Replace empty string with NaN
new_df["Description"] = new_df["Description"].replace(r"^\s*$", np.nan, regex=True)
new_df

# Split DataFrame into two dfs based on even and odd indices
name = new_df.iloc[::2]
value = new_df.iloc[1::2]
    
# Reset index for the two new dfs
reset_index_np(name)
name
reset_index_np(value)
value

# 'Join' name and value dfs onto each other based on row position
output = pd.concat([name, value], axis=1, ignore_index = True)
output

# Remove columns which don;t contain any data
output.drop(columns = [0, 2], inplace = True)

# Rename columns
output.rename(columns = {1: "name", 3: "value"}, inplace = True)
output
