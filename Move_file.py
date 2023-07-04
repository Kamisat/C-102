import os
import shutil

from_dir = "C:/Users/Admin/Downloads"

to = "C:/Users/Admin/Documents/JV/Projeto 102/Arquivos"



fileList = os.listdir(from_dir)

#print(fileList)




for file in fileList:

    name, extention = os.path.splitext(file)

    if extention == "":
        continue
    elif extention in [ ".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + "/" + file
        path2 = to
        path3 = to + "/" + file
        if os.path.exists(path2): 
            print("Movendo " + file + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Movendo " + file + "...")
            shutil.move(path1, path3)


redirecionar = input("Deseja redirecionar os arquivos para a pasta original?(y/n)")

finalList = os.listdir(to)


if redirecionar == "y":

    for file in finalList:

        name, extention = os.path.splitext(file)

        if extention == "":
            continue
        elif extention in [ ".txt", ".doc", ".docx", ".pdf"]:
            
            print("Redirecionando...")

            path1 = from_dir + "/" + file
            path3 = to + "/" + file

            shutil.move(path3,path1)