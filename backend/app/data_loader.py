import pandas as pd
import tiktoken

def load_data(path="data.csv"):
    # List of columns to keep
    columns_to_keep = ["Alias","Name",'Short Description','Approval group','Managed by','Support group','Assigned to',
    'Managed By Group','Problem Manager Group','Problem Owner Group','Product Owner Executive','Product Owner'
    ,'Service Executive ','Service Owner','Service Team']
    #df = pd.read_csv(path)
    df = pd.read_excel(path)
    df = df[columns_to_keep]
    df.fillna("", inplace=True)  # Fill NaN with "Unknown"
    # Create combined column
    df["Text"] = (
         "name: " + df["Name"].str.strip() +
        "; alias: " + df["Alias"].str.strip() +
        "; description: " + df['Short Description'].str.strip()[:1000] + 
        "; serviceOwner: " + df['Service Owner'].str.strip() +
        "; serviceTeam: " + df['Service Team'].str.strip() +
        "; serviceExecutive: " + df['Service Executive '].str.strip() +
        "; productOwner: " + df['Product Owner'].str.strip() +
        "; productOwnerExecutive: " + df['Product Owner Executive'].str.strip() +
        "; problemOwnerGroup: " + df['Problem Owner Group'].str.strip() +
        "; problemManagerGroup: " + df['Problem Manager Group'].str.strip() +
        "; managedByGroup: " + df['Managed By Group'].str.strip() +
        "; assignedTo: " + df['Assigned to'].str.strip() +
        "; approvalGroup: " + df['Approval group'].str.strip()
    )
    df['Text'] = df['Text'].astype(str)
    rows_count = df.shape[0]
    print("Number of rows in the DataFrame:", rows_count)
    encoding = tiktoken.get_encoding("cl100k_base")
    df["n_tokens"] = df.Text.apply(lambda x: len(encoding.encode(x)))
    return df
