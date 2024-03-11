from datetime import date
import os
import shutil
import subprocess
import time
from PyPDF2 import PdfWriter, PdfReader
import customtkinter

startTime = time.time() #logging runtime

# Variable initialization

date = date.today().strftime("%#m-%d-%Y")
downloads = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/RRC/Downloads')
main = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/RRC/')
filterListPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents/RRC/filterlist.txt')
archive = main + '/archive/'
todays = archive + date + '/'
normalTodays = os.path.normpath(todays).replace("\\","/")
 
os.system('cls') # clear console

if not os.path.exists(downloads):
    print('CREATING DOWNLOADS FILE...')
    os.makedirs(downloads)

if not os.path.exists(filterListPath):
    print('CREATING FILTER FILE...')
    newFile = open(filterListPath, "x")
    newFile.close()

if not os.path.exists(archive):
    print('CREATING ARCHIVE FILE...')
    os.makedirs(archive)

if not os.path.exists(todays):
    print('CREATING TODAYS FILE...')
    os.makedirs(todays)

filterListTxt = open(filterListPath, "r")
filterText = filterListTxt.read()
filterListTxt.close()

def openFilterDialog():
    def close():
        newWindow.update()
        filterListTxt = open(filterListPath, "r")
        filterText = filterListTxt.read()
        filterListTxt.close()
        newWindow.destroy()
    
    def saveButtonClicked():
        text = filterTextBox.get("0.0", "end")
        print(text)
        file1 = open(filterListPath, 'w')
        file1.write(text)
        file1.close()
        filterTextBox.destroy()

    newWindow = customtkinter.CTkToplevel(app)
    newWindow.title("Edit Filter")
 
    newWindow.geometry("400x400")

    closeDialogButton = customtkinter.CTkButton(newWindow, text="Close", command = close)
    closeDialogButton.pack()

    saveFilterButton = customtkinter.CTkButton(newWindow, text="Save Filter", command = saveButtonClicked)
    saveFilterButton.pack()

    #filterTextBox.insert("0.0", ("\n".join(filterText)))
    filterTextBox = customtkinter.CTkTextbox(newWindow)
    filterTextBox.insert("0.0", filterText)
    filterTextBox.pack()

def handleClick():
# Program begins
    print ('Program begins-^&y_^^^__^-----------')
    nid = 0
    wid = 0

    txt = open(filterListPath, "r")
    txtToArray = txt.read().splitlines()
    print(txtToArray)
    txt.close()


    startButton.configure(text="Run")

    os.chdir(downloads)
    print('Working in ' + os.getcwd() + "...")

# Renaming
    if not len(os.listdir()) == 0:
        for file in os.listdir():
            for key in txtToArray: # filter W3As
                if key in file:
                    try:
                        wid += 1
                        os.rename(file,'{}{} #{}.pdf'.format("W3A ", date, wid))
                        print(file + ' -> ' '{}{} #{}'.format("W3A ", date, wid)) #log
                    except FileNotFoundError:
                        continue
            if 'Noti' in file:
                nid += 1
                os.rename(file,'{}{} #{}.pdf'.format("DN ", date, nid))
                print(file + ' -> ' '{}{} #{}'.format("DN ", date, nid)) #log
        print("------------Files Renamed---------")
        myLabel.configure(text="Files ready to be processed", text_color="green")
    else:
        print('No files to work with')
        myLabel.configure(text="No files to work with", text_color="red")

    pages_to_keep = [0, 1, 2, 3] # 4 pagers
    pages_to_keep2 = [0, 3] # 4 pagers trimmed to 2 pages
    delete_list = []

    def handleFourPagers(x): # im cringe
        fourPageCopyHandler = PdfWriter()
        shutil.copyfile(x, normalTodays  + '/' + x)
        print('Made a copy of ' + x)
        for i in pages_to_keep2:
            p = pdfObj.getPage(i)
            fourPageCopyHandler.addPage(p)
        fileName = os.path.splitext(x)[0]
        with open(normalTodays  + '/' + fileName + ' - Copy.pdf', 'wb') as f:
            fourPageCopyHandler.write(f)
        print('Trimmed ' + x+ ' into a 2 page W3A for Drillinginfo -')
        delete_list.append(x)

    for file in os.listdir():
        with open(file, "rb") as f:
            pdfObj = PdfReader(f)
            pagecount = len(pdfObj.pages)
            print(str(pagecount) + " pages in file : " + file)

            if pagecount == 2: # 2 page W3A
                page = pdfObj.pages[0]
                twoPageHandler = PdfWriter()
                twoPageHandler.add_page(page)
                with open(normalTodays + '/' + file, 'wb') as f:
                    twoPageHandler.write(f)
                print('Trimmed ' + file + ' down to 1 page -')
                delete_list.append(file)

            if pagecount > 4: # Produce normal 4 page W3As
                fourPageHandler = PdfWriter()
                for i in pages_to_keep:
                    page = pdfObj.pages[i]
                    fourPageHandler.add_page(page)
                with open(normalTodays  + '/' + file, 'wb') as f:
                    fourPageHandler.write(f)
                print('Trimmed ' + file + ' down to 4 pages')
                fourPageTrimNoti = customtkinter.CTkLabel(app, text='Trimmed ' + file + ' down to 4 pages')
                fourPageTrimNoti.pack()

                fileName = os.path.splitext(file)[0]
                print("After trimming " + str(pagecount) + " pages in file : " + file)  # at this point it still says the pagecount is 5, this backs up that "file" is still the shit one...
                delete_list.append(file)
                #handleFourPagers(file) # i'm sending the shit one to the function. i need to send the actual trimmed 4 pager which is lost in memory atm

            if pagecount == 4: # Take 4 page W3As and trim pages 2 and 3
                fourPageCopyHandler = PdfWriter()
                shutil.copyfile(file, normalTodays  + '/' + file)
                print('Made a copy of ' + file)
                for i in pages_to_keep2:
                    p = pdfObj.pages[i]
                    fourPageCopyHandler.add_page(p)
                fileName = os.path.splitext(file)[0]
                # TODO: is this making copies or no? no its not, only for the ones that are already 4 pages... i need to call fourPagehandler inside the 4+ page handler function
                with open(normalTodays  + '/' + fileName + ' - Copy.pdf', 'wb') as f:
                    fourPageCopyHandler.write(f)
                print('Trimmed ' + file + ' into a 2 page W3A for Enverus -')
                delete_list.append(file)

    # cleanup function to delete all files in the folder
    if not len(os.listdir()) == 0:
        print ('Deleting... ' + str(delete_list))
        for i in delete_list:
            os.remove(i)

        FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
        sanitizedTodays = os.path.normpath(todays)
        subprocess.run([FILEBROWSER_PATH, sanitizedTodays])
        print ('there are already processed files in todays folder')

    # move renamed files to today's folder and open it in file explorer
    # otherwise if no files, open downloads folder
    if not len(os.listdir()) == 0: # if there are files in downloads folder
        file_names = os.listdir(downloads)
# TODO: this is moving files that failed to rename. need to add a conditional. LIST_TO_MOVE maybe? nah should add IF 'W3' or 'DN'
        for file_name in file_names:
            shutil.move(os.path.join(downloads, file_name), todays)
# this isnt running for some reason...
        print ('Moved renamed files...')

    elif len(os.listdir(todays)) == 0: # if no files in downloads + if Todays folder is empty
        FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
        sanitizedDownloads = os.path.normpath(downloads)
        subprocess.run([FILEBROWSER_PATH, sanitizedDownloads])
    else:
        print ('neither of these conditions happened idk')

# This implementation of execution time counts the time u spend starting at the UI, need to incorporate it within the handleDelete function
    # executionTime = (time.time() - startTime)
    # print('Runtime: ' + str(executionTime) + ' seconds')

# GUI

app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
myLabel = customtkinter.CTkLabel(app, text="Click start to begin...", pady=10, font=customtkinter.CTkFont(size=20, weight="bold"))
myLabel.pack()
startButton = customtkinter.CTkButton(app, text="Start", corner_radius=60, width=100, height=200, font=customtkinter.CTkFont(size=40, weight="bold"), command=handleClick)
startButton.pack(padx=20, pady=10)
startButton.place(relx=0.5, rely=0.5, anchor="center")

editFilterButton = customtkinter.CTkButton(app, text="Edit Filter", command=openFilterDialog)
editFilterButton.pack()

app.title("pdftool")
app.geometry("500x500")  # Width x Height

app.mainloop()