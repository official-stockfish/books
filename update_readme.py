import json

json_file = "books.json"
readme_file = "README.md"

with open(json_file) as f:
    data = json.load(f)

headers = ["book", "total", "white", "black", "min_depth", "max_depth"]
header_md = "| " + " | ".join(headers) + " |"
separator_md = "| :--- | " + " | ".join(["---:"] * (len(headers) - 1)) + " |"

rows_md = []
for book in data:
    row_values = ["`" + book + "`"]
    row_values += [str(data[book][h]) for h in headers if h != "book"]
    rows_md.append("| " + " | ".join(row_values) + " |")

table_md = "\n".join([header_md, separator_md] + rows_md)

with open(readme_file) as f:
    readme = f.read()

start_marker = "<!-- TABLE_START -->"
end_marker = "<!-- TABLE_END -->"
source_line = f"<sub>*(Data sourced from [{json_file}]({json_file}).)*</sub>"

if start_marker in readme and end_marker in readme:
    before_table = readme.split(start_marker)[0]
    after_table = readme.split(end_marker)[1]
    new_readme = f"{before_table}{start_marker}\n{table_md}\n\n{source_line}\n{end_marker}{after_table}"
else:
    print(
        f"Warning: Markers {start_marker} and {end_marker} not found in {readme_file}."
    )
    exit(1)

if new_readme != readme:
    with open(readme_file, "w") as f:
        f.write(new_readme)
    print(f"Successfully updated table in {readme_file}.")
else:
    print(f"No changes needed.")
