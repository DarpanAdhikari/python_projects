import os
import shutil

file_extensions = {
    'pdf': 'PDFs', 'jpg': 'Images', 'png': 'Images', 'jpeg': 'Images',
    'gif': 'Images', 'bmp': 'Images', 'cf2': 'Images', 'cfa': 'Images',
    'txt': 'Text Documents', 'doc': 'Documents', 'docx': 'Documents',
    'odt': 'Documents', 'rtf': 'Documents', 'odp': 'Presentations',
    'ppt': 'Presentations', 'pptx': 'Presentations', 'zip': 'Archives',
    'rar': 'Archives', '7z': 'Archives', 'iso': 'Operating Systems',
    'py': 'Python Scripts', 'c': 'C Code', 'cpp': 'C Code', 'java': 'Java Code',
    'js': 'JavaScript Code', 'html': 'HTML Code', 'css': 'CSS Code',
    'sql': 'SQL Scripts', 'csv': 'CSV Files', 'tsv': 'TSV Files',
    'xlsx': 'Excel Files', 'xls': 'Excel Files', 'mp3': 'Audio Files',
    'mp4': 'Video Files', 'wav': 'Audio Files', 'avi': 'Video Files',
    'flv': 'Video Files', 'mkv': 'Video Files', 'mov': 'Video Files',
    'wmv': 'Video Files',
}


def organize_files(directory):
    directory = os.path.abspath(directory)

    if not os.path.exists(directory):
        print("Error: The directory does not exist.")
        return

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            file_extension = file.split('.')[-1].lower()  # Ensure lowercase extension
            folder_name = file_extensions.get(file_extension, 'Other_Files')
            destination = os.path.join(directory, folder_name)

            if not os.path.exists(destination):
                os.makedirs(destination)

            shutil.move(file_path, os.path.join(destination, file))  # Move file


while True:
    directory = input('Enter the directory path: ').strip().strip('"')
    organize_files(directory)

    another = input("Do you want to organize another directory? (yes/no): ").strip().lower()
    if another != 'yes':
        print("Exiting...")
        break
