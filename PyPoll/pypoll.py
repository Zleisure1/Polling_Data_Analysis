import os
import csv

os.chdir(os.path.dirname(__file__)) #changed directory to source of this main.py file  
csvpath = os.path.join( '..', 'Resources', 'election_data.csv')

#print(csvpath) #WORKS
with open(csvpath, newline="") as csvfile:
 csvreader = csv.reader(csvfile, delimiter=',')
 next(csvreader)
 pypoll_list = list(csv.reader(csvfile))
 #print(pypoll_list)
 #print(pypoll_list[0:10])
 total_votes = len(list(pypoll_list))
 candidate_list = []
 vote_count = []

for row in pypoll_list:
    if row[2] not in candidate_list:    #if candidate name not in candidate list then
        candidate_list.append(row[2])   #add candidate name to candidate list
        index = candidate_list.index(row[2])  #assigns index # to value
        vote_count.append(1)    #adds 1 vote to vote count list 
    else:
        index = candidate_list.index(row[2]) #assigns index # to value; each candidate will have a unique index #
        vote_count[index] +=1  #adds 1 and overwrites to vote count list by index #
candidate_0_percentagenum = (vote_count[0]/total_votes)*100
candidate_1_percentagenum = (vote_count[1]/total_votes)*100
candidate_2_percentagenum = (vote_count[2]/total_votes)*100
candidate_3_percentagenum = (vote_count[3]/total_votes)*100
winner = max(vote_count)
index = vote_count.index(winner)
winning_candidate = candidate_list[index]
#candidate_0_percentage = {candidate_0_percentagenum: .3f}
#######  OUTPUT RESULTS  ##################
#print([candidate_list]) only 4 candidates received votes
#print(vote_count)   #[2218231, 704200, 492940, 105630]
#print(f'{candidate_0_percentagenum:.3f}')
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f'{candidate_list[0]}: {candidate_0_percentagenum:.3f}% ({vote_count[0]}) ')   ##Khan
print(f'{candidate_list[1]}: {candidate_1_percentagenum:.3f}% ({vote_count[1]}) ')   ##Correy
print(f'{candidate_list[2]}: {candidate_2_percentagenum:.3f}% ({vote_count[2]}) ')    ##Li
print(f'{candidate_list[3]}: {candidate_3_percentagenum:.3f}% ({vote_count[3]}) ')    ##O'Tooley
print("-------------------------")
print(f'Winner: {winning_candidate}')
###############################################
### Creates output text file with election results   ####
output = open("pypoll.txt", "w")
line1 = "Election Results"
line2 = "-------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = "-------------------------"
line5 = str(f'{candidate_list[0]}: {candidate_0_percentagenum:.3f}% ({vote_count[0]}) ')
line6 = str(f'{candidate_list[1]}: {candidate_1_percentagenum:.3f}% ({vote_count[1]}) ')
line7 = str(f'{candidate_list[2]}: {candidate_2_percentagenum:.3f}% ({vote_count[2]}) ')
line8 = str(f'{candidate_list[3]}: {candidate_3_percentagenum:.3f}% ({vote_count[3]}) ')
line9 = "-------------------------"
line10 = str(f'Winner: {winning_candidate}')
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7, line8, line9, line10))
