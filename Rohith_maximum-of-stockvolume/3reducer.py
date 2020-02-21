s = open("01.txt","r")
r = open("02.txt", "w")

thisKey = ""
thisValue = 0.0
count =0

for line in s:
  data = line.strip().split('\t')
  stock, date = data

  if stock != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = stock 
    thisValue = float(date)
  
  # apply the aggregation function
  if(float(date) > float(thisValue)):
      thisValue =float(date)

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()

