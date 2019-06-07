import time


#start
print("""   

                             o o
   o      o           o      o  o
  o  o   o o        o        o   o
 o     o    o      o         o   o
o            o       o       o  o
                       o     o o     (for the power of)

""")


#login
needspassword=True
while needspassword==True:

  #username/password input
  username=raw_input("username:")
  password=raw_input("password:")

#userpass codes
  if username!="m c d" or password!="maths cheating device":
    print("   ")
    print ("incorrect username/password")
  else:
    needspassword=False
  



#introduction
print("  ")

print("welcome to the maths cheating device (for the power of) ")

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
base=raw_input("base  number?")

power=raw_input("to the power of")



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
answer=int(base)

for x in range(int(power)-1) :
  answer=answer*int(base)
print("answer"+str(answer))






  










