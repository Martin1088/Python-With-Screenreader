def Settings(**kwargs):
       return {
           'flags': ['-x', 'python'],
           'interpreter_path': 'python3',
           'sys_path': [
               'home/m049k/.local/lib/python3.10/',
               # Add other paths as needed
           ],
           'completion': {
               'auto_import': True,
               'extra_imports': [
                   'g', 'flask', 'SQLAlchemy'
               ],
           },
       }
