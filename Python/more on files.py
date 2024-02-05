#Copying Files
print("Copying Files" '\n')

#copys file without metadata information
#shutil.copy(src,dst)

#copys file with MetaData information
#shutil.copystat(src,dst)

#Python Modules - built-in modules

import shutil #copying
src = "test.txt"
dst = "test-copy.txt"
shutil.copy(src, dst)

import os #Operating system - renaming file
os.rename("test-copy.txt", "renaming-test-copy.txt")

import os #Operating system - delete a file
os.remove ("renaming-test-copy.txt")
