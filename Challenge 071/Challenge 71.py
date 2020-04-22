# Today’s challenge is for all of our analysts and data scientists who used SQL in a past (or their current) lifetime! Using the schematic above, 
# can you recreate all the SQL joins with the Alteryx Join Tool and the datasets we have provided?

# Source: https://community.alteryx.com/t5/Weekly-Challenge/Challenge-71-Recreate-SQL-Joins-in-Alteryx/td-p/61226

import pandas as pd

df_a = pd.read_csv("./challenge_71a_input.csv")
df_b = pd.read_csv("./challenge_71b_input.csv")

df_a
df_b

# Left join
df_left = df_a.merge(df_b, how="left", left_on='Supervisor Key', right_on='Key')
df_left

# Left outer join
df_left_outer = df_a.merge(df_b, how="outer", left_on='Supervisor Key', right_on='Key', indicator = True)
df_left_outer = df_left_outer[df_left_outer["_merge"] == "left_only"]
df_left_outer

# Right join
df_right = df_a.merge(df_b, how="right", left_on='Supervisor Key', right_on='Key')
df_right

# Right outer join
df_right_outer = df_a.merge(df_b, how="outer", left_on='Supervisor Key', right_on='Key', indicator = True)
df_right_outer = df_right_outer[df_right_outer["_merge"] == "right_only"]
df_right_outer

# Inner join
df_inner = df_a.merge(df_b, how="inner", left_on='Supervisor Key', right_on='Key')
df_inner

# Outer join
df_outer = df_a.merge(df_b, how="outer", left_on='Supervisor Key', right_on='Key', indicator = True)
df_outer = df_outer[df_outer["_merge"] != "both"]
df_outer

# Full join
df_full = df_a.merge(df_b, how="outer", left_on='Supervisor Key', right_on='Key')
df_full
