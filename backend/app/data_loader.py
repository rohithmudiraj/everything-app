import pandas as pd
import tiktoken

def load_contacts_data(path):
    # List of columns to keep
    csv_columns_to_keep = [
        "name", "u_alias", "short_description", "change_control", "managed_by", "support_group",
        "assigned_to", "managed_by_group", "u_problem_manager_group", "u_problem_owner_group",
        "u_product_owner_exe", "u_product_owners", "u_service_executive", "owned_by", "u_service_team"
    ]
    # Read CSV
    df = pd.read_csv(path,encoding="ISO-8859-1")

    # Filter only necessary columns
    df = df[csv_columns_to_keep]
    df.fillna("", inplace=True)
    # Build text representation
    def build_text(row):
        parts = []
        def add_part(label, value):
            if pd.notna(value) and str(value).strip():
                parts.append(f"{label}: {str(value).strip()}")
        add_part("name", row.get("name"))
        add_part("alias", row.get("u_alias"))
        add_part("description", row.get("short_description")[:1500])
        add_part("serviceOwner", row.get("owned_by"))
        add_part("serviceTeam", row.get("u_service_team"))
        add_part("serviceExecutive", row.get("u_service_executive"))
        add_part("productOwner", row.get("u_product_owners"))
        add_part("productOwnerExecutive", row.get("u_product_owner_exe"))
        add_part("problemOwnerGroup", row.get("u_problem_owner_group"))
        add_part("problemManagerGroup", row.get("u_problem_manager_group"))
        add_part("managedByGroup", row.get("managed_by_group"))
        add_part("managedBy",row.get("managed_by"))
        add_part("assignedTo", row.get("assigned_to"))
        add_part("approvalGroup", row.get("change_control"))
        return "; ".join(parts)

    # Apply to DataFrame
    df["Text"] = df.apply(build_text, axis=1)
    # Token count
    encoding = tiktoken.get_encoding("cl100k_base")
    df["n_tokens"] = df["Text"].apply(lambda x: len(encoding.encode(x)))
    print("Number of rows in the DataFrame:", df.shape[0])
    return df


def load_group_data(path):
     # List of columns to keep
    columns_to_keep = ["name","u_company","manager","u_group_category","description","u_location"]
    df = pd.read_csv(path,encoding="ISO-8859-1")
    df = df[columns_to_keep]
    df.fillna("", inplace=True)  # Fill NaN with ""
    def build_text(row):
        parts = []
        def add_part(label, value):
            if pd.notna(value) and str(value).strip():
                parts.append(f"{label}: {str(value).strip()}")
        add_part("name", row.get("name"))
        add_part("company", row.get("u_company"))
        add_part("manager", row.get("manager"))
        add_part("group_category", row.get("u_group_category"))
        add_part("description", row.get("description")[:1500])
        add_part("location", row.get("u_location"))
        return "; ".join(parts)
    # Apply the function to your DataFrame
    df["Text"] = df.apply(build_text, axis=1)
    rows_count = df.shape[0]
    print("Number of rows in the DataFrame:", rows_count)
    encoding = tiktoken.get_encoding("cl100k_base")
    df["n_tokens"] = df.Text.apply(lambda x: len(encoding.encode(x)))
    return df