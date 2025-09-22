import zipfile
import os

path01 = r'C:\Users\path01'
path02 = r'C:\Users\path02'

#find the first .zip file in path01
def find_zip_file(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.zip'):
                return os.path.join(root, file)
    return None

#extract files
zip_file_path = find_zip_file(path01)

if zip_file_path:
    print(f"Found ZIP file: {zip_file_path}")
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            for file_name in zip_ref.namelist():
                if "PA" in file_name:
                    zip_ref.extract(file_name, path01)
                    print(f"Extracted {file_name} to {path01}")
                elif "SND" in file_name:
                    zip_ref.extract(file_name, path02)
                    print(f"Extracted {file_name} to {path02}")
        os.remove(zip_file_path)
        print(f"Removed original ZIP: {zip_file_path}")
    except zipfile.BadZipFile:
        print(f"Error: {zip_file_path} is not a valid ZIP file.")
else:
    print("No ZIP file found in PAD directory.")


def extract_and_clean(directory):
    #extract the .zip files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(root, file)
                try:
                    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(directory)
                        print(f"Extracted {file} into {directory}")
                    os.remove(zip_path)
                    print(f"Removed {file} from {directory}")
                except zipfile.BadZipFile:
                    print(f"Error: {zip_path} is not a valid ZIP file.")
    
    #remove the .xml files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml'):
                xml_path = os.path.join(root, file)
                os.remove(xml_path)
                print(f"Removed XML file: {file} from {directory}")


extract_and_clean(path01)
extract_and_clean(path02)