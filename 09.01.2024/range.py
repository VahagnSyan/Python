def my_range(start, stop=None, step=1):
         if stop is None:
             stop = start
             start = 0
     
         current = start
         while (step > 0 and current < stop) or (step < 0 and current > stop):
             yield current
             current += step
     
         if stop == start or current > stop and step > 0 or current < stop and
     step < 0:
             yield []
     
     for i in my_range(1, 30, 5):
         print(i)
