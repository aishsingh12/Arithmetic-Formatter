def arithmetic_arranger(problems,val=False):
  arranged_problems=''
    
  #checking for no. of problems
  if len(problems)>5:
      arranged_problems='Error: Too many problems.'
      return arranged_problems
    
  #checking for type of operators
  o=[i.split(" ")[1] for i in problems]
  if set(o) != {'+', '-'} and set(o) != {'+'} and set(o)!={'-'}:
      arranged_problems = "Error: Operator must be '+' or '-'."
      return arranged_problems
    
  # list of all operands in str format
  numbers = []  
  for i in problems:
      p = i.split()
      numbers.extend([p[0], p[2]])
        
  #check for digits and their length
  for i in numbers:
      if i.isdigit()==False:
          arranged_problems = "Error: Numbers must only contain digits."
          return arranged_problems
      if len(i)>4:
          arranged_problems = "Error: Numbers cannot be more than four digits."
          return arranged_problems 
    
  #list of ans
  #if val==True:
  ans=[eval(problems[i]) for i in range(len(problems))]
        
  #printing
  frow=''
  soln=''
  dash=''
  for i in range(0,len(numbers),2):
      space=max(len(numbers[i]),len(numbers[i+1]))+2
      frow+=numbers[i].rjust(space)
      dash+='-'*space
      soln+=str(ans[i//2]).rjust(space)
      if i != len(numbers) - 2:
          frow += ' ' * 4
          dash += ' ' * 4
          soln += ' ' * 4
  srow=''
  for i in range(1,len(numbers),2):
      space=max(len(numbers[i-1]),len(numbers[i]))+1
      srow+=o[i//2]
      srow+=numbers[i].rjust(space)
      if i != len(numbers) - 1:
          srow += ' ' * 4
  if val:
      arranged_problems='\n'.join((frow, srow, dash, soln))
  else:
      arranged_problems='\n'.join((frow,srow,dash))
  return arranged_problems