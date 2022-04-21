# An implimentation of the algorithm described in figure 1 here.
# https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.84.5691&rep=rep1&type=pdf

def greedyAlpha(jobsSorted, alpha=0.414):
  jobsToDo = []
  for job in jobsSorted:
    costToAdd=0
    toRemove = []
    for jobDo in jobsToDo:
      jobTimeConflict = job.start < jobDo.end
      jobRepeat = job.ride == jobDo.ride
      if jobTimeConflict or jobRepeat:
        costToAdd += jobDo.val
        toRemove.append(jobDo)
    if alpha*job.val>costToAdd:
      for jobRemove in toRemove:
        jobsToDo.remove(jobRemove)
      jobsToDo.append(job)
  return jobsToDo

