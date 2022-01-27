from datetime import date
import os

date = date.today().strftime("%#m-%d-%Y")

print(date) #log

### Use Windows explorer Preview pane to quickly check pages

os.chdir('C:/Users/admin/Documents/work/Downloads')
print('Working in ' + os.getcwd() + "...")

if not os.path.exists('C:/Users/admin/Documents/work/' + date + '/'):
    print('CREATING FILE...')
    os.makedirs('C:/Users/admin/Documents/work/' + date + '/')


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

os.chdir('C:/Users/admin/Documents/work/' + date + '/')

print('Working in ' + os.getcwd() + "...") #log

print("------------DONE---------")
