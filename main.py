# Importing the necessary packages

import pandas as pd
import os
import glob
import re as re
import numpy as np

# Getting all the CSVs in the current working directory
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))
csv_files

# Looping through the CSVs and extracting any value matching the regex of 10 digits

df_list = []
df_output_new = pd.DataFrame()
n = 0
for csv in csv_files:
  try:
    df_csv = pd.read_csv(csv, encoding = 'unicode_escape')
    for col in df_csv.columns:
      for mob_no in re.findall('\d{10}', str(df_csv[col])):
        df_list.append(mob_no)
  except UnicodeDecodeError:
    print (f"Error in file {csv_files[n]}")
  finally:
    n += 1

# Storing the list directly into the final CSV

np.savetxt("final.csv", df_list, delimiter="'", fmt ='% s')
