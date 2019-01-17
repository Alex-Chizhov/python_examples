import os
import os.path


# Get current working directory
os.getcwd()

# Change working directory
os.chdir('c:\\new_folder')

# Get list of files and subdirectories
os.listdir('c:\\new_folder')
os.listdir('.')
os.listdir('folder1')

# Find out is folder or file
os.path.isfile('folder1')
os.path.isdir('text.txt')

# Get list of files with filter
os.chdir('C:/Users/Alex/Documents')
list(filter(lambda f: f.endswith('.mp4'), os.listdir('.')))

# Create directory
os.chdir('c:\\new_folder')
os.mkdir('new_test_dir')

# Create subdirectories
os.makedirs('test_dir1\\test_dir2\\test_dir3')

# Remove empty directory
os.rmdir('test_dir1\\test_dir2\\test_dir3')

# Remove not empty directorytest_dir1
import shutil
shutil.rmtree('test_dir1')

# Copy file
shutil.copy('text.txt', 'folder1')

# Remove file
os.remove('folder1\\text.txt')

# We can use // or \
os.listdir('c:\\new_folder')
os.listdir('c:/new_folder')