import os
import argparse

def join_files(source_directory, output_file, extensions):

    if not os.path.isdir(source_directory):
        print(f"Error: Directory '{source_directory}' not found.")
        return
    
    # Count files matching the extensions
    file_count = sum(1 
                     for _, _, files in os.walk(source_directory) 
                     for file in files if file.endswith(extensions))

    if file_count == 0:
        print(f"No files found with extensions: {', '.join(extensions)}")
        return

    if file_count > 50:
        extensions_str = ", ".join(extensions)
        response = input(f"Found {file_count} files with extensions '{extensions_str}'. Continue? (y/n): ")
        if response.lower() != 'y':
            print("Bye.")
            return

    with open(output_file, 'w', encoding='utf-8') as outfile:
        print(f"Combining {file_count} file(s) into '{output_file}'...")
        for root, _, files in os.walk(source_directory):
            files.sort()  # Ensure predictable order
            for file in files:
                # Check if the file ends with any of the extensions
                if file.endswith(extensions):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, source_directory)
                    subfolder = os.path.dirname(relative_path)

                    if subfolder == "":
                        subfolder_display = " (root directory)"
                    else:
                        subfolder_display = f" (in subfolder: {subfolder})"

                    title = f"--- File: {file}{subfolder_display} ---\n\n"
                    outfile.write(title)
                    print(f"Adding: {relative_path}")

                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read())
                        outfile.write("\n\n")
                    except Exception as e:
                        outfile.write(f"Error reading file '{file_path}': {e}\n\n")
                        print(f"Error reading file '{file_path}': {e}")

    extensions_str = ", ".join(extensions)
    print(f"\nAll files with extensions {extensions_str} have been combined into '{output_file}'")
    print("Bye.")


def main():
    parser = argparse.ArgumentParser(
        description="Combine files with specific extensions into one output file."
    )
    parser.add_argument(
        "-s", "--source",
        default=os.getcwd(),
        help="Source directory (default: current working directory)"
    )
    parser.add_argument(
        "-e", "--ext",
        nargs='+',
        default=["md"],
        help="File extension(s) to search for, without the dot (e.g., md py txt). (default: md)"
    )
    parser.add_argument(
        "-o", "--output",
        default="combined_files.txt",
        help="Output file path (default: combined_files.txt)"
    )

    args = parser.parse_args()

    is_default_output = (args.output == "combined_files.txt")
    if is_default_output and len(args.ext) == 1:
        args.output = f"combined_{args.ext[0]}.txt"


    clean_extensions = [f".{ext.lstrip('.')}" for ext in args.ext]





    join_files(args.source, args.output, tuple(clean_extensions))

if __name__ == "__main__":
    main()