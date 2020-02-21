# providing the input file to the reducer file
s = open("01.txt","r")
# creating the new file to store the output values
r = open("02.txt", "w")

thisKey = ""
thisValue = 0.0
count =0


# Iterating the data in the loop to only create the required files.
for line in s:
  data = line.strip().split('\t')
  stock, stockvolume = data

  if stock != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = stock 
    thisValue = float(stockvolume)
  
  # applied  the aggregation function - minimum
  if(float(stockvolume) < float(thisValue)):
      thisValue =float(stockvolume)

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()

