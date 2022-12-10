
# CSV Reader 

Compare two CSV files using pandas

# Important Pandas Function you should know before using this function
## (Used [ChatGPT](https://chat.openai.com/chat)) to generate below text.
* To compare two Excel sheets with different numbers of rows and find the differences using Python, you can use the pandas library. Pandas is a powerful tool for working with data in Python, and it makes it easy to work with Excel files. Here's an example of how you could compare two Excel sheets with different numbers of rows and find the differences using Python and pandas:

* First, you'll need to install the pandas library if you don't already have it. You can do this by running pip install pandas at the command line.

* Next, you'll need to load the two Excel sheets that you want to compare into pandas dataframes. You can do this using the pandas.read_excel() function. For example:

```python
import pandas as pd

# Load the first Excel sheet into a dataframe
df1 = pd.read_excel('sheet1.xlsx')

# Load the second Excel sheet into a dataframe
df2 = pd.read_excel('sheet2.xlsx')
```

* Once you have the dataframes loaded, you can compare them to find the differences. One way to do this is to use the pandas.merge() function to merge the two dataframes on a common column, such as the primary key. For example:


```python
# Merge the two dataframes on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID')
```

* After merging the dataframes, you can compare the values in the columns to find the differences. One way to do this is to use the pandas.DataFrame.eq() method to compare the values in each column, and then use the pandas.DataFrame.any() method to find rows where the values are not equal. For example:

```python
# Compare the values in each column
differences = merged_df.eq(df1, axis=0)

# Find rows where the values are not equal
differences = differences[differences.any(axis=1)]
```
* Finally, you can use the pandas.DataFrame.loc() method to select the rows that have differences, and then print or save the data to a new Excel sheet. For example:
```python
# Select the rows that have differences
differences = merged_df.loc[differences.index]

# Print the rows with differences
print(differences)

# Save the differences to a new Excel sheet
differences.to_excel('differences.xlsx')
```




## Quick Start CSV Reader 🧑🏻‍💻


Clone the project

```bash
  git clone https://github.com/VinayPrajapatiRigi/csv-reader.git
```

Go to the project directory

```bash
  cd CSV_Comparator
```

Install dependencies



## Libraries used to create CSV Comparator 

 - [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
 - [pandas](https://pandas.pydata.org/docs/)
 - [xlwings](https://docs.xlwings.org/en/stable/)
 


## Documentation

[Documentation](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)





## Tech Stack

**Server:** Python




## Features

- Compare to CSV with Different or Same Number of Rows and Find Differences



## Feedback

If you have any feedback, please reach out to me at vinay@rigi.club


## Authors

- [vinay@rigi.club]

