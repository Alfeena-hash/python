f=open("test.txt","w")
f.write("sample file\n")
f.write("this sample\n\n")
f.open("test.txt","r")
str=f.read()
print("read string:",str)
f.close()
print(f.name,"is close")
       
