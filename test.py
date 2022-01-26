# from tkinter import*
# import tkinter as tk
# import tkinter.simpledialog
# import configparser
# import os.path

# def onChange(i):     
#     btn_list[i].config(text='Updating...',bg='red')  
#     btn_list[i].grid(in_=root,row=rw[i],column=2)
#     ans=tk.simpledialog.askfloat('Updating....', 'What is the current price?')
#     if ans:
#         btn_list[i].config(text='RM {:,.2f}'.format(ans))
#         btn_list[i].config(bg='yellow')
#         c=str(ans)
#         #fw=open('dataUpdate.txt','w')
#         #fw.write(c)
#         #fw.close()
#         #----------------------------------------------
#         # Here you can call update(section, key value) 
#         update('Section1', 'number%s' % i, c)
#         #----------------------------------------------


# root=Tk()

# Title=['Item','Unit','Price']
# Item=['Kopi O','Teh O','Teh Tarik']
# Unit= '1 cup'
# cl=[0,1,2]
# rw=[1,2,3]
# btn_list=[]

# #------------------------------------------------------------------------
# config = configparser.RawConfigParser()

# def init():
#     'Create a configuration file if does not exist'
#     config.add_section('Section1')
#     config.set('Section1', 'number1', '1')
#     config.set('Section1', 'number2', '0.8')
#     config.set('Section1', 'number3', '0.2')
#     with open('dataUpdate.cfg', 'w') as output:
#         config.write(output)

# #------------------------------------------------------------------------
# # check if dataUpdate.cfg exist if not create it   
# if not os.path.exists('dataUpdate.cfg'):
#     init()

# # Read configurations using section and key to get the value
# config.read('dataUpdate.cfg')
# number = [config.getfloat('Section1', 'number%s' % (i)) for i in range(3)]
# #------------------------------------------------------------------------




# #------------------------------------------------------------
# def update(section, key, value):
#     #Update config using section key and the value to change
#     #call this when you want to update a value in configuation file
#     # with some changes you can save many values in many sections
#     config.set(section, key, value )
#     with open('dataUpdate.cfg', 'w') as output:
#         config.write(output)
# #------------------------------------------------------------


# for k in range(3):
#     btnT1=tk.Button(root,text=Title[k],width=12,bg='light green')
#     btnT1.grid(in_=root,row=0,column=cl[k])

# for x in range(3):
#     btnT2=tk.Button(root,text=Item[x],width=12)
#     btnT2.grid(in_=root,row=rw[x],column=0)

# for y in range(3):
#     btnT3=tk.Button(root,text=Unit,width=12)
#     btnT3.grid(in_=root,row=rw[y],column=1)             

# for z in range(3):
#     btnT4=tk.Button(root,text=('RM {:,.2f}'.format(number[z])),bg='yellow',width=12,\
#                 command=lambda i=z:onChange(i))
#     btnT4.grid(in_=root,row=rw[z],column=2)
#     btn_list.append(btnT4)

# root.mainloop() q