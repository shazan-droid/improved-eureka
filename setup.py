from cx_Freeze import setup, Executable

# Replace 'app.py' with the name of your PyQt6 script
executables = [Executable('app.py')]

# Include any additional files or packages needed by your application
additional_files = ['config.json']  # Add the config.json file

# List of required packages/modules
packages = [
    'sys', 'PyQt6', 'tkinter', 'pandas', 'openpyxl', 'datetime', 'smtplib', 'email',
    'apscheduler', 'schedule', 'mariadb'
    # Add other required packages/modules here
]

options = {
    'build_exe': {
        'includes': packages,
        'include_files': additional_files,
        # Other options can be specified here as needed
    }
}

setup(
    name='MyApp',
    version='1.0',
    description='My PyQt6 Application',
    options=options,
    executables=executables
)
