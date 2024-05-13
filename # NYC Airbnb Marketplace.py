# NYC Airbnb Marketplace 

import pandas as pd 
import numpy as np 

tsv_path = (r"C:\Users\ivic2\Downloads\airbnb_last_review.tsv")
excel_path = (r"C:\Users\ivic2\Downloads\airbnb_room_type.xlsx")
csv_path = (r"C:\Users\ivic2\Downloads\airbnb_price.csv")

tsv_df = pd.read_csv(tsv_path, sep='\t')
excel_df = pd.read_excel(excel_path)
csv_df = pd.read_csv(csv_path)

# Merge the three data frames together into one
listings = pd.merge(csv_df, excel_df, on = 'listing_id')
listings = pd.merge(listings, tsv_df, on = 'listing_id')

#earliest and most recent reviews in two seperate variables
listings['last_reviewed_date'] = pd.to_datetime(listings['last_review'], format = '%B %d %Y')
first_reviewed = listings['last_reviewed_date'].max()
last_reviewed = listings['last_reviewed_date'].min()

print(first_reviewed)
print(last_reviewed)

# How many of the listings are private rooms?

roomtype = 'room_type'

# Filter rows where the column value matches the regex pattern
filtered_df = excel_df[excel_df[roomtype].str.contains('Private room', case = False)]

# Print the filtered DataFrame
print(filtered_df)

# Private Rooms count 
listings['room_type'] = listings['room_type'].str.lower()
private_room_count = listings[listings['room_type']== 'private room'].shape[0]
print(private_room_count)

# Average listing price 
listings['price_numeric'] = listings['price'].str.replace(' dollars', '').astype(float)
avg_price = listings['price_numeric'].mean()

# Combine the new variables into one DataFrame called review_dates with four columns in the following order: first_reviewed, last_reviewed, nb_private_rooms, and avg_price. 
# The datafram should only contain one row of values.

review_dates = pd.DataFrame({
    'firs_reviewed': [first_reviewed],
    'last_reviewed': [last_reviewed],
    'nb_private_rooms': [private_room_count],
    'avg_price': [round(avg_price, 2)]
})

print(review_dates)



