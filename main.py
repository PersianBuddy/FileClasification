import os
import shutil

classified_directory = os.path.join(os.path.curdir, 'classified')
if not os.path.exists(classified_directory):
    os.mkdir(classified_directory)
direcotories_list = [os.path.curdir]

while direcotories_list:
    current_directory = direcotories_list.pop()
    # search for all files and directories in current dierctory
    direcotory_content = os.listdir(current_directory)
    for directory_name in direcotory_content:
        if directory_name == '.git' or directory_name == 'classified':
            continue
        elif os.path.isdir(os.path.join(current_directory, directory_name)):
            direcotories_list.append(os.path.join(current_directory, directory_name))

        # if it's a file classify it
        else:
            file_path = os.path.join(current_directory, directory_name)
            file_extention = os.path.splitext(file_path)[1]
            # file with no extention
            if file_extention =='':
                other_extention_path = os.path.join(classified_directory, 'other')
                if not os.path.exists(other_extention_path):
                    os.mkdir(other_extention_path)
                # check if file exist
                file_new_path = os.path.join(other_extention_path, directory_name)
                same_name_count = 0
                while os.path.exists(file_new_path):
                    same_name_count += 1
                    new_file_name = f'renamed{same_name_count}-{directory_name}'
                    file_new_path = os.path.join(other_extention_path, new_file_name)
                
                shutil.copy(file_path, file_new_path)
            # files with extentions
            else:
                with_extention_files_path = os.path.join(classified_directory, file_extention)
                if not os.path.exists(with_extention_files_path):
                    os.mkdir(with_extention_files_path)
                # check if file exist
                file_new_path = os.path.join(with_extention_files_path, directory_name)
                same_name_count = 0
                while os.path.exists(file_new_path):
                    same_name_count += 1
                    new_file_name = f'renamed{same_name_count}-{directory_name}'
                    file_new_path = os.path.join(with_extention_files_path, new_file_name)
                
                shutil.copy(file_path, file_new_path)
