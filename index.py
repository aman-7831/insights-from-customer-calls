import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the Excel file
file_path = "Customer Call List.xlsx"
df = pd.read_excel(file_path)

# Make a copy for cleaning
df_cleaned = df.copy()

# Step 1: Standardize column names (remove spaces)
df_cleaned.columns = df_cleaned.columns.str.strip().str.replace(' ', '_')

# Step 2: Drop completely empty rows
df_cleaned.dropna(how='all', inplace=True)

# Step 3: Handle missing values
df_cleaned['Phone_Number'] = df_cleaned['Phone_Number'].fillna('Unknown')
df_cleaned['Last_Name'] = df_cleaned['Last_Name'].fillna('Unknown')
df_cleaned['Do_Not_Contact'] = df_cleaned['Do_Not_Contact'].fillna('No')

# Step 4: Drop duplicates
df_cleaned.drop_duplicates(inplace=True)

# Step 5: Remove unnecessary columns
if 'Not_Useful_Column' in df_cleaned.columns:
    df_cleaned.drop(columns=['Not_Useful_Column'], inplace=True)

# Step 6: Save cleaned data to Excel
output_excel = "Refined_Customer_Call_List.xlsx"
df_cleaned.to_excel(output_excel, index=False)

# Step 7: Set seaborn style
sns.set(style="whitegrid")

# Plot 1: Paying vs Non-Paying Customers
plt.figure(figsize=(6,4))
sns.countplot(data=df_cleaned, x='Paying_Customer')
plt.title('Paying vs Non-Paying Customers')
plt.xlabel('Paying Customer')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("Paying_vs_NonPaying.png")
plt.close()

# Plot 2: Do Not Contact Distribution
plt.figure(figsize=(6,4))
sns.countplot(data=df_cleaned, x='Do_Not_Contact')
plt.title('Do Not Contact Preference')
plt.xlabel('Do Not Contact')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("Do_Not_Contact_Distribution.png")
plt.close()

# Plot 3: Top 10 First Names
plt.figure(figsize=(8,5))
top_names = df_cleaned['First_Name'].value_counts().head(10)
sns.barplot(x=top_names.index, y=top_names.values)
plt.title('Top 10 Most Common First Names')
plt.xlabel('First Name')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Top_10_First_Names.png")
plt.close()

print("✅ Data cleaning are completed and plots are also saved.")
