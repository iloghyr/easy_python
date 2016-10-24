import os 

def listFile(path):
	for val in os.listdir(path):
		path = os.path.join(path, val)
		print path
		if os.path.isdir(path):
		 	listFile(path)
		

#listFile(r'D:\\')


def Test2(rootDir): 
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        print path 
        if os.path.isdir(path): 
            Test2(path) 

Test2(r'D:\\')
# for apk in os.listdir('./'):
#     if os.path.isfile(apk):
#         print apk
#     if os.path.isdir(apk):
#     	print 'asdf'

        