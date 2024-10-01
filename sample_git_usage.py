# sample_git_usage.py

def write_initial_content(filename):
    """Write initial content to a file."""
    with open(filename, 'w') as file:
        file.write("Hello, Git class!\nThis is the first line of our file.\n")


def append_content(filename, new_content):
    """Append new content to the existing file."""
    with open(filename, 'a') as file:
        file.write(new_content + '\n')


def main():
    filename = 'example.txt'

    # Step 1: Write initial content
    write_initial_content(filename)

    # Step 2: Append new content
    append_content(filename, "Here's an additional line, tracked by Git.")


if __name__ == "__main__":
    main()
