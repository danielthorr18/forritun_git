def check_bricks(small, big, goal):
  big_needed = goal // 5
  small_needed = goal % 5
  
  if big >= big_needed:
    return small >= small_needed 
  return small >= (goal - big * 5)