#The data we need to retrieve:
# 1. The total number of votes cast 
# 2. A complete list of candidates who recieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

#import dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize a new list for candidate options
candidate_options = []

# Initialize a new dict for candidate votes
candidate_votes = {}

#Winning Cadidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count. 
        total_votes += 1

         # print the candidate name from each row 
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            #tinitialize vote count 
            candidate_votes[candidate_name] = 0

        #count each vote
        candidate_votes[candidate_name] += 1
        
 #save the results to text file
with open(file_to_save, 'w') as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)




    #interate through candidate list
    for candidate_name in candidate_votes:

        #get the vote count of each candidate
        votes = candidate_votes[candidate_name]

        #Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print the candidate name and percentage of votes

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        # Save the canddiate results to our text file.
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage): 
            winning_count = votes 
            winning_percentage = vote_percentage
            winning_candidate = candidate_name 

        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

    # save the winning candidate's name to the text file.
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)




