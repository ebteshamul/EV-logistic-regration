input_file = "Electric_Vehicle_Population_Data_copy.csv"
output_file = "Cleaned_EV_Data.csv"

# We'll keep the header (line 1) + 59,999 rows of data
limit = 60000 

with open(input_file, 'rb') as f_in:
    with open(output_file, 'wb') as f_out:
        for i, line in enumerate(f_in):
            if i < limit:
                f_out.write(line)
            else:
                break # Stop processing once we hit the limit

print(f"Done! Created {output_file} with the first {limit} lines.")