def Exrecursive(x,y):
  if (y == 0):
    return 1
  return x * Exrecursive(x, y - 1)

print (Exrecursive(2,3))        

# x * (x,y0-1)*(x,y1-1)*(x,y3-1)
# 2 * (2,2)   * (2,1)  * (2,0) 
# 2 *   2     *   2    *   1

