s = open("sorteddata.txt","r")

r = open("reduced_data.txt", "w")

thisKey = ""

thisValue = 0.0

ctr = 0

for line in s:

  data = line.strip().split('\t')

  item, cost = data

  if item != thisKey:

    if thisKey:

      # output the last key value pair result

      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys

    thisKey = item

    thisValue = 0.0  

  # apply the aggregation function

  thisValue += float(cost)

# output the final entry when done

r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()

r.close()