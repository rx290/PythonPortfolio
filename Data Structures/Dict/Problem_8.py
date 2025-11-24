""" Write a Python script to concatenate following dictionaries to create a new one. 

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}""" 

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic4={7:10, 8:20}
dic5={9:30, 10:40}
dic6={13:50,15:60}

dic7={17:10, 20:20}
dic8={22:30, 24:40}
dic9={27:50,30:60}

concatenated_dic = dic1 | dic2 |dic3
print(concatenated_dic)

concatenated_dic2 = {**dic4,**dic5,**dic6}
print(concatenated_dic2)
