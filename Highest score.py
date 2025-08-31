score_list = [45, 67, 89, 23, 90, 56, 78]

def highest_score(scores):
    highest=score_list[0]   # Start with the first score

    for score in score_list:
        if score>=highest:
            highest= score      # Replace highest

    return highest

print(highest_score(scores=score_list))
