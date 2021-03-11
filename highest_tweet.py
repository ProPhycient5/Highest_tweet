n=int(input())              #no. of test cases
         
a=0
while a<n:
  m=int(input())             #no. of test input
  players=[]
  for _ in range(m):         #keeping all inputs 
    name, id= input().split()
    players.append(name)
  a=+1
  
  my_dict={}             #keeping all name & tweet occurence in dict
  for i in players:
    num=players.count(i)
    if i not in my_dict.keys(): 
      my_dict.update({i:num})
  
  
  most=max(my_dict.values())
  my_list_val=list(my_dict.values())
  my_list_key=list(my_dict.keys())
  
  if my_list_val.count(most) == 1:  #for single highest tweets
    idx=my_list_val.index(most)
    print(f'{my_list_key[idx]} {most}')

  
  else:                         #for multiple highest tweets
    my_dict2=my_dict.copy()
    for k, v in my_dict2.items():
      if v != most:
        my_dict.pop(k)

    for _ in sorted(my_dict):
      print(f'{_} {most}')
