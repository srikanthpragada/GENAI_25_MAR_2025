def top_5_names_by_length(file_path="names.txt"):
    with open(file_path, "r") as file:
        names = file.read().splitlines()
    
    # Sort names by length in descending order, then alphabetically for ties
    sorted_names = sorted(names, key=lambda name: (-len(name), name))
    
    # Get the top 5 names
    return sorted_names[:5]

# Example usage
if __name__ == "__main__":
    top_names = top_5_names_by_length()
    print("Top 5 names by length:")
    for name in top_names:
        print(name)