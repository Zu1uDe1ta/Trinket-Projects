from turtle import * 

"""
write(0) 
forward(20) 
write(1) 
forward(20) 
write(2) 
forward(20) 
write(3) 
forward(20) 
write(4) 
forward(20) 
write(5) 
forward(20) 
"""

goto(-140, 140)

for step in range(6): 
  write(step)
  forward(20)