import pandas as pd

# Ask the user for the input Excel file path
input_excel_path = input("Enter the path to the input Excel file: ")

# Ask the user for the output Excel file path
output_excel_path = input("Enter the path to save the output Excel file: ")

try:
    # Read the input Excel file
    df = pd.read_excel(input_excel_path)

    # Check if the 'Email' column exists in the DataFrame
    if 'Email' not in df.columns:
        print("Column 'Email' not found in the Excel file.")
    else:
        # Extract names from email addresses and handle None values
        def extract_name(email):
            if pd.notna(email):
                return email.split('@')[0]
            else:
                return None

        df['Name'] = df['Email'].apply(extract_name)

        # Add a sequence number as a new column
        df['Sequence'] = range(1, len(df) + 1)

        # Reorder the columns to have 'Sequence' first
        df = df[['Sequence', 'Name', 'Email']]

        # Save the DataFrame with names and sequence numbers to a new Excel file
        df.to_excel(output_excel_path, index=False)

        print(f"Names extracted and saved to {output_excel_path}")

except FileNotFoundError:
    print(f"File not found: {input_excel_path}")
except Exception as e:
    print(f"An error occurred: {e}")
