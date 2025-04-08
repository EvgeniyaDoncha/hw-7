from zipfile import ZipFile

with ZipFile("tmp/топы ВБ (2).zip") as zip_file:
    print(zip_file.namelist())
    text = zip_file.read('╤é╨╛╨┐╤ï ╨Æ╨æ (2).xlsx')
    print(text)
    zip_file.extract('╤é╨╛╨┐╤ï ╨Æ╨æ (2).xlsx', path="tmp")
