sv = {
    "adam": 7.4,
    "eve": 9.2,
    "cemaz": 6.7,
    "john": 3.1,
}
def ranking(score):
    if score >= 9:
        return "sss"
    elif score >= 6.5:
        return "ss"
    elif score >= 5:
        return "s"
    else:
        return "F"
total_score = 0
for name, score in sv.items():
    rank = ranking(score)
    print(f"{name} : {score} : {rank}")
    total_score += score
average_score = total_score / len(sv)
print(f"Average Score: {average_score:.2f}")
    