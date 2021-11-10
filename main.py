# main.py file

#* This imports our app (website) from our market folder (specifically from our __init__.py file) so that it can run on our local host.
from market import app

#* This controls if the current file is our main file.
if __name__ == "__main__":
    # If the above statement is correct, it runs our website in debugmode.
    app.run(debug = True)

# The below example only works if you have Better Comments installed and enabled.
#! This is an alert
#? This is a query
#* Highlighting for important information
#TODO: Learn what TODO means
## Removed comment
# Regular comment