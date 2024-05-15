import os
import filecmp
import csv

def compare_folders(folder1, folder2, results, parent_folder1="", parent_folder2=""):
    """
    Compare the contents of two folders recursively and store the results in the results list.

    Args:
        folder1 (str): Path to the first folder.
        folder2 (str): Path to the second folder.
        results (list): List to store comparison results.
        parent_folder1 (str): Relative path of the parent folder for folder1 (used for recursion).
        parent_folder2 (str): Relative path of the parent folder for folder2 (used for recursion).
    """
    folder1_items = set(os.listdir(folder1))
    folder2_items = set(os.listdir(folder2))

    # Union of all items in both folders
    all_items = folder1_items.union(folder2_items)

    for item in all_items:
        path1 = os.path.join(folder1, item)
        path2 = os.path.join(folder2, item)

        # Relative paths for output
        relative_path1 = os.path.join(parent_folder1, item)
        relative_path2 = os.path.join(parent_folder2, item)

        # Check if item is missing in folder1
        if item not in folder1_items:
            results.append([relative_path1, relative_path2, "Missing in folder1", "", "", "", ""])
            continue

        # Check if item is missing in folder2
        if item not in folder2_items:
            results.append([relative_path1, relative_path2, "", "Missing in folder2", "", "", ""])
            continue

        # If both items are directories, compare them recursively
        if os.path.isdir(path1) and os.path.isdir(path2):
            compare_folders(path1, path2, results, relative_path1, relative_path2)
        # If both items are files, compare their properties
        elif os.path.isfile(path1) and os.path.isfile(path2):
            size1 = os.path.getsize(path1)
            size2 = os.path.getsize(path2)

            mtime1 = os.path.getmtime(path1)
            mtime2 = os.path.getmtime(path2)

            content_differs = not filecmp.cmp(path1, path2, shallow=False)

            # Append results with detailed comparison
            results.append([
                relative_path1, relative_path2,
                "Identical" if size1 == size2 else "Size differs",
                "Identical" if mtime1 == mtime2 else "Modification time differs",
                "Identical" if not content_differs else "Content differs",
                size1, size2,
                mtime1, mtime2
            ])
        else:
            # One is a file and the other is a directory
            results.append([relative_path1, relative_path2, "One is file, other is directory", "", "", "", ""])

def write_results_to_csv(results, csv_file):
    """
    Write the comparison results to a CSV file.

    Args:
        results (list): List of comparison results.
        csv_file (str): Path to the output CSV file.
    """
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow([
            "Path in Folder1", "Path in Folder2", 
            "File Size Comparison", "Modification Time Comparison", 
            "Content Comparison", "Size in Folder1", "Size in Folder2",
            "Modification Time in Folder1", "Modification Time in Folder2"
        ])
        # Write the comparison results
        writer.writerows(results)

# Example usage
folder1 = r"C:\Users\memen\Downloads\copyTest1"  # Use raw string for Windows paths
folder2 = r"C:\Users\memen\Downloads\copyTest2"  # Use raw string for Windows paths
csv_file = r"C:\Users\memen\Documents\GitHub\ordinal-scripts\comparison_results.csv"  # Use raw string for Windows paths

# List to store the comparison results
results = []
# Compare the folders
compare_folders(folder1, folder2, results)
# Write the results to a CSV file
write_results_to_csv(results, csv_file)

print(f"Comparison results have been written to {csv_file}.")

