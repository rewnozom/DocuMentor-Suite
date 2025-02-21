import os

def list_files(directory, extension=None):
    files = []
    for file in os.listdir(directory):
        if extension:
            if file.endswith(extension):
                files.append(os.path.join(directory, file))
        else:
            files.append(os.path.join(directory, file))
    return files
