def Settings(**kwargs):
       return {
           'flags': ['-x', 'python'],
           'interpreter_path': 'python3',
           'sys_path': [
               '/usr/lib/python3.8',
               # Add other paths as needed
           ],
           'completion': {
               'auto_import': True,
               'extra_imports': [
                   'sqlite3', 'g', 'flask', 
               ],
           },
       }
