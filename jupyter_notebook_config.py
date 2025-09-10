# Configuration file for jupyter-notebook.

# Get the config object
c = get_config()  # This line is required to access the config object

# Set options to allow access without a token
c.NotebookApp.token = ''
c.NotebookApp.password = ''
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.allow_origin = '*'
c.NotebookApp.open_browser = False

# Also set ServerApp options for newer Jupyter versions
c.ServerApp.token = ''
c.ServerApp.password = ''
c.ServerApp.ip = '0.0.0.0'
c.ServerApp.allow_origin = '*'
c.ServerApp.open_browser = False
