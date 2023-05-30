import os

def get_go_files(directory):
    go_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".go"):
                go_files.append(os.path.join(root, file))
    return go_files


def get_dependencies():
    dependencies = []
    with open('dependencies.txt', 'r') as file:
        for line in file:
            # Split the line in lib and version
            lib = line.strip()

            # Check if there are any lib
            if lib != '':
                # Append the first element to the list
                dependencies.append(lib)
    return dependencies


# print(get_dependencies())
# print(get_go_files(os. getcwd()))

def count_string_occurrences(directory=os.getcwd()):
    search_strings = get_dependencies()
    occurrence_count = {string: 0 for string in search_strings}
    go_files = get_go_files()

    for file_path in go_files:
        with open(file_path, 'r') as file:
            contents = file.read()
            for search_string in search_strings:
                occurrence_count[search_string] += contents.count(search_string)

    return occurrence_count

def write_dictionary_to_file(dictionary, file_path):
    with open(file_path, 'w') as file:
        for key, value in dictionary.items():
            line = f"{key}: {value}\n"
            file.write(line)

result = count_string_occurrences()
sorted_result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

write_dictionary_to_file(sorted_result, 'result.txt')