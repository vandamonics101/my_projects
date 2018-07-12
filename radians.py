


def PlayerAgeFunction():
   VALID = True
   while VALID == True:
      PlayerAge = int(raw_input('ENTER YOUR AGE: '))
      if PlayerAge == type(int):
          VALID = False
     elif PlayerAge != type(int):
         print 'THAT IS NOT A NUMBER.'
   return PlayerAge
