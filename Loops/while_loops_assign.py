#Question 1: You are about to interview a number of candidates for a job offer at the company you work at or at your company. There are a number of repetitive operations that you need to do.
#Identify and list the Repetitive operations
#Describe how you will use the while() loop in each operation
#Implement the while() loops in python code


# Candidate Information Input
candidate_list = []
while True:
    candidate_name = input("Enter candidate name (or 'exit' to finish): ")
    if candidate_name.lower() == 'exit':
        break
    candidate_details = {'name': candidate_name}
    candidate_list.append(candidate_details)

# Questionnaire and Scoring
questions = ["Tell me about your relevant experience.",
             "How do you handle challenging situations?",
             "What are your strengths and weaknesses?"]

candidate_idx = 0
while candidate_idx < len(candidate_list):
    candidate = candidate_list[candidate_idx]
    print(f"Interviewing {candidate['name']}:")
    
    question_idx = 0
    while question_idx < len(questions):
        candidate_response = input(questions[question_idx] + " ")
        # Store candidate's responses for further evaluation
        
        question_idx += 1

    # Scoring
    score = 0
    # Calculate score based on responses and criteria
    candidate['score'] = score

    candidate_idx += 1

# Selection Criteria Check
threshold = 7
selected_candidates = []
candidate_idx = 0
while candidate_idx < len(candidate_list):
    candidate = candidate_list[candidate_idx]
    if candidate['score'] >= threshold:
        selected_candidates.append(candidate['name'])
    candidate_idx += 1

# Interviewer's Remarks
candidate_idx = 0
while candidate_idx < len(candidate_list):
    candidate = candidate_list[candidate_idx]
    candidate['remarks'] = input(f"Remarks for {candidate['name']}: ")
    candidate_idx += 1

# Follow-up Actions
candidate_idx = 0
while candidate_idx < len(candidate_list):
    candidate = candidate_list[candidate_idx]
    decision = input(f"Select {candidate['name']} for the next round? (yes/no): ")
    candidate['decision'] = decision
    candidate_idx += 1


