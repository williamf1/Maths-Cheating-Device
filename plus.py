import time


#start
print("""   

                             o o
   o      o           o      o  o
  o  o   o o        o        o   o
 o     o    o      o         o   o
o            o       o       o  o
                       o     o o     (for +)

""")


#login
needspassword=True
while needspassword==True:

  #username/password input
  username=raw_input("username:")
  password=raw_input("password:")

#repeat
  if username!="m c d" or password!="maths cheating device":
    print("   ")
    print ("incorrect username/password")
  else:
    needspassword=False
  



#introduction
print("  ")

print("welcome to the maths cheating device (for +) ")

print("  ")


#how to
time.sleep(1)
print("follow the instructions to get your answers")

print("  ")




#contact
time.sleep(1)
print("if you need help contact:ken.faulkner.gh@gmail.com")

print("  ")

time.sleep(1)





#input for calculator
timest=raw_input("what number do you want to plus by ")

loop=raw_input("up to what number?")



#waiting to give answers
print("calculating. ")
time.sleep(0.5)
print("calculating.. ")
time.sleep(0.5)
print("calculating... ")
time.sleep(0.5)
print("calculating. ")
time.sleep(0.5)
print("calculating.. ")
time.sleep(0.5)
print("calculating... ")
time.sleep(1)
print("finished")
time.sleep(1)




#calculator
inttimest=int(timest)

for x in range(int(loop)+1) :
  answer=inttimest+x

  print(str(x)+"+"+timest+"="+str(answer))
