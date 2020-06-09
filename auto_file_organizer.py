import os

file_names= os.listdir() 

file_names.remove('auto_file_organizer.py') # so that our script is not hampered

def make_folders(folder_name): # makes folders if they are not created already.
    if not os.path.exists(folder_name):
        
        os.makedirs(folder_name)


def file_move(folder_name,files): # moves the files to their respective folders
    for file in files:
        
        os.replace(file,f"{folder_name}/{file}")


if __name__ == "__main__":   

    #You can customize the extensions and add more . I added the most used ones.add()

    img_extensions=['png','jpeg','jpg','gif','tiff','psd','ai','raw']
    
    audio_extensions=['mp3','wav','waptt','3ga','wpl','flac','rec','aac','ogg']
    
    video_extensions=['mp4','mkv','mov','avi','wvm']

    web_extensions=['css','html','htm','json','js','php']

    doc_extensions=['pdf','docx','doc','xml','ppt','word','xlsx','txt']


    #Time to get the actual files

    image_files=[files for files in file_names if os.path.splitext(files)[1][1:].lower() in img_extensions]

    audio_files=[files for files in file_names if os.path.splitext(files)[1][1:].lower() in audio_extensions]

    video_files=[files for files in file_names if os.path.splitext(files)[1][1:].lower() in video_extensions]

    web_files =[files for files in file_names if os.path.splitext(files)[1][1:].lower() in web_extensions]

    doc_files=[files for files in file_names if os.path.splitext(files)[1][1:].lower() in doc_extensions]

    other_files=[]

    for files in file_names:
        if (files not in image_files) and (files not in audio_files) and (files not in video_files) and (files not in web_files)  and (files not in doc_files) and os.path.isfile(files):
            other_files.append(files)

    
    
    make_folders('Images')
    make_folders('Videos')
    make_folders('Music')
    make_folders('Documents')
    make_folders('Web')
    make_folders('Others')



    file_move("Images",image_files)
    file_move("Music",audio_files)
    file_move("Videos",video_files)
    file_move("Web",web_files)
    file_move("Documents",doc_files)
    file_move("Others",other_files)