import os
from hurry.filesize import size,alternative

# reference this local directory -> .
# or specify filepath -> C:\\
path = r'C:\Program Files (x86)'
print(path)

dir_sizes = {}
for r, d, f in os.walk(path, False):
   sizes = sum(os.path.getsize(os.path.join(r,f)) for f in f+d)
   sizes += sum(dir_sizes[os.path.join(r,d)] for d in d)
   dir_sizes[r] = sizes
      # int of bytes --> human-readable str
   sizes = size(sizes,system=alternative)
      # print size of every subdirectory
   #print ("{} is ".format(r) + str(sizes)) 

print('\n\n\nfirst level subfolders:\n')

print('Total path size is %s' %size(dir_sizes.get(path),system=alternative))
list_subfolder = [f.path for f in os.scandir(path) if f.is_dir()]
sorted_subf = []
for i in range(len(list_subfolder)):
   sorted_subf.append([list_subfolder[i],dir_sizes.get(list_subfolder[i])])
sorted_subf.sort(key=lambda x:x[1],reverse=True)
for i in range(len(sorted_subf)):
   print('%s: %s' %(sorted_subf[i][0],size(sorted_subf[i][1],system=alternative)))
