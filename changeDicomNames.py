from pathlib import Path

def add_extension_to_files(folder_path, extension):
    folder_path = Path(folder_path)
    for file_path in folder_path.glob('*'):
        if not file_path.suffix:
            new_path = file_path.with_suffix('.' + extension)
            file_path.rename(new_path)

if __name__ == '__main__':
    add_extension_to_files('.', 'dic')