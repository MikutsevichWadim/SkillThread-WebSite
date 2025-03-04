import os

def export_modules_to_file(output_filename="modules_content.txt", excluded_directories=None, allowed_extensions=None):
	"""
	Exports the content of text files in the current directory and its subdirectories
	(excluding specified directories) to a single output file.

	Args:
		output_filename (str, optional): The name of the output file. Defaults to "modules_content.txt".
		excluded_directories (list of str, optional): A list of directory names to exclude.
													Defaults to None (no directories excluded).
		allowed_extensions (list of str, optional): A list of file extensions to include (e.g., ['.py', '.txt']).
													 If None, all files are considered (with extension filtering).
	"""
	
	if excluded_directories is None:
		excluded_directories = []
	if allowed_extensions is None:
		allowed_extensions = ['.py', '.txt', '.ini', '.conf', '.json', '.html', '.css', '.js', '.md', '.rst'] # Common text file extensions
	
	with open(output_filename, 'w', encoding='utf-8') as outfile:
		for root, dirs, files in os.walk('.'):  # Start walking from the current directory
			
			# Robustly exclude directories by checking if the current root path starts with any excluded directory
			if any(root.startswith(os.path.join('.', excluded_dir)) for excluded_dir in excluded_directories):
				continue  # Skip this entire directory and its subdirectories
			
			for filename in files:
				if not any(filename.lower().endswith(ext) for ext in allowed_extensions):
					continue # Skip files that don't have allowed extensions
				
				filepath = os.path.join(root, filename)
				
				try:
					with open(filepath, 'r', encoding='utf-8') as infile:
						content = infile.read()
						
						outfile.write(f"-------------------- File: {filepath} --------------------\n")
						outfile.write(content)
						outfile.write("\n\n") # Add some spacing between files
				
				except Exception as e:
					outfile.write(f"Error reading file: {filepath} - {e}\n\n")
	
	print(f"Content of modules exported to: {output_filename}")

if __name__ == "__main__":
	# Example usage: Exclude directories and specify allowed file extensions
	exclude_dirs = [".venv",'alembic', "__pycache__", ".git", ".idea"] # Directories to exclude
	allowed_file_extensions = ['.py', '.txt', '.ini'] # Only export these file types (add more if needed)
	export_modules_to_file(excluded_directories=exclude_dirs, allowed_extensions=allowed_file_extensions)
