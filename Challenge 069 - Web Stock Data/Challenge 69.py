import pandas as pd
import requests
import io

data = requests.get("https://s3-us-west-1.amazonaws.com/community.uploads/mushrooms.csv")
data_decode = data.content.decode('utf8')
df = pd.read_csv(io.StringIO(data_decode))
df
