# Apriori-for-weekly-homework
This is for the Datamining homework in University of Helsinki.

####Question: 

Using your Apriori-code, identify the largest course combination (largest number of courses) with support over 0.04. Type in the combination to your learning diary, reflect upon the previous three tasks, and provide a link to your source code.

Checklist, make sure that your algorithm has all the following

- It uses the course codes (integers) as the representation for courses, not strings.

- Candidate generation merges only frequent k-1 itemsets that share all but the last item, to avoid generating unnecessary candidates (ex. 2)

- Candidate pruning that may remove some of the generated candidates even before looking at their support counts (ex. 4)
- More efficient support counting than iterating through the whole dataset for each itemset (ex. 5)
