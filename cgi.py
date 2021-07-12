import cgitb
import shutil
cgitb.enable()


if 'file' in form:
   filefield = form['file']
   if not isinstance(filefield, list):
      filefield = [filefield]

   for fileitem in filefield:
       if fileitem.filename:
          fn = secure_filename(fileitem.filename)
          # save file
          with open('/var/www/domain.com/files/' + fn, 'wb') as f:
              shutil.copyfileobj(fileitem.file, f)