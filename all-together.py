import time








def mcdmultiplication()  :
  #introduction
  print("  ")

  print("welcome to the maths cheating device (for multiplication) ")

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
  timest=raw_input("what timestable do you want?")

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
    answer=inttimest*x

    print(str(x)+"x"+timest+"="+str(answer))


















def mcdpowerof()  :
  #for the power of



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


def mcddivision()  :
  #for division


  #introduction
  print("  ")

  print("welcome to the maths cheating device (for division) ")

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
  timest=raw_input("what number do you want to divide by ")

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
    answer=inttimest*x

    print(str(answer)+"÷"+timest+"="+str(x))









def mcdsubtraction()  :
  #for subtracting



  #introduction
  print("  ")

  print("welcome to the maths cheating device (for subtraction) ")

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
  timest=raw_input("what number do you want to minus by ")

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
    answer=inttimest-x

    print(str(x)+"-"+timest+"="+str(answer))







def mcdaddition()  :
  #for addition






  #introduction
  print("  ")

  print("welcome to the maths cheating device (for addition) ")

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


#start
print("""   

                            o o
    o      o         o      o  o
  o  o   o o        o       o   o
 o     o    o      o        o   o
o            o     o        o  o
                     o      o o     (for all ones)

""")


#login
needspassword=True
while needspassword==True:

  #username/password input
  username=raw_input("username:")
  password=raw_input("password:")

  #repeat
  if username!="m c d" or password!="m c d":
    print("   ")
    print ("incorrect username/password")
  else:
    needspassword=False

    print("   ")

    print("   ")

    print("   ")

    print("   ")

    print("options")

    print("   ")

    print("type the number that is next to the option you want to choose")

    print("   ")

    print("""1.multiplication
    2.power of
    3.division
    4.subtraction
    5.addition

    """)

    selection=raw_input("what type do you want to use")

    if selection=="1"  :
      mcdmultiplication()





    if selection=="2"  :
      mcdpowerof()



          

    if selection=="3"  :
      mcddivision()





    if selection=="4"  :
      mcdsubtraction()





    if selection=="5"  :
      mcdaddition()




































































































































































































