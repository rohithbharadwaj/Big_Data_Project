#recuder takes the input values from 01.txt and does the aggregate function and stores in the 02.txt file
s = open("01.txt","r")
r = open("02.txt", "w")

thisKey = ""
thisValue = 0.0
#count =0

for line in s:
  data = line.strip().split('\t')
  stock, stockvolume = data

  if stock != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = stock 
    thisValue = 0.0
  
  
  # apply the aggregation function which takes the sum values from eachs stock category and storing in the file 02.txt
  #if(float(stockvolume) > float(thisValue)):
    thisValue += float(stockvolume)

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()

