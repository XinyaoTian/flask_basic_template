# Flask basic template Helper

### Before coding...

Remember to use this command to enter Virtual Environment(VE) before you are going to code.

    $ source VE/bin/activate 
    
### Blueprint has been imported!
Specify the functions of each module when you designing this application.

If you forgot the principle of Blueprint, just review app/errors and app/main.
Also, don't forget the factory model in app/\_\_init__.py
    
### I18n & L10n
To translate your web page into multiple languages, your should use flask_babel.

Mention all the texts printed on your web page.Using _() or _l() to mark all the strings in this project.
Like these:

    _('Welcome to my blog!')

Having marked all the texts, use those three reinforcement commands below to init, update
and compile texts that need to be translated(And babel.cfg is really important when initiating).

    $ flask translate init <lang-code>
    $ flask translate update
    $ flask compile
    
### Error handler : Mail and logging
Remember to set e-mail username and password in .flaskenv before deploying on the production server.

The log file will be automatically delete(Max 10 files, delete from earlier one), so don't bother with storage problems.
   
    

### Other topic will be updated later...