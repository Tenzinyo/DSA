def activity(startTime,endTime):
  startTime=[]
  endTime=[]
  max=0
  for i in startTime:
    for j in endTime:
      if endTime[j]>=startTime[i] and endTime[j]<endTime[j+1]:
        max = endTime[j];
        
  
