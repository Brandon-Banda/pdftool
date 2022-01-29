from datetime import date
import os

date = date.today().strftime("%-m-%d-%Y")

print(date) #log

if not os.path.exists('/Users/Brandon/Desktop/work/' + date + '/'):
    print('CREATING FILE...')
    os.makedirs('/Users/Brandon/Desktop/work/' + date + '/')

os.chdir('/Users/Brandon/Desktop/work/' + date + '/')

print('Working in ' + os.getcwd() + "...") #log

W3A = "DOC"
nid = 0
wid = 0

for file in os.listdir():
    if W3A in file:
        ftype = "W3A "
        wid += 1
        os.rename(file,'{}{} #{}.pdf'.format(ftype, date, wid))
        print(file + ' -> ' '{}{} #{}'.format(ftype, date, wid)) #log
        # if pages = 2, delete page 2
        # if pages = 5, delete page 5
        # if pages = 4, setType = 4pager
            # COPY and delete pages 2, 3
    else:
        ftype = "DN "
        nid += 1
        os.rename(file,'{}{} #{}.pdf'.format(ftype, date, nid))
        print(file + ' -> ' '{}{} #{}'.format(ftype, date, nid)) #log
print("------------DONE---------")
