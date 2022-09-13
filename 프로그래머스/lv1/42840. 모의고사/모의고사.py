def solution(answers):
    p1 = [1, 2, 3, 4, 5] * 2000
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    len_answer = len(answers)
    p1 = p1[:len_answer]
    p2 = p2[:len_answer]
    p3 = p3[:len_answer]

    p1_grade = sum([1 for p, a in zip(p1, answers) if p == a])
    p2_grade = sum([1 for p, a in zip(p2, answers) if p == a])
    p3_grade = sum([1 for p, a in zip(p3, answers) if p == a])

    grade_max = max(p1_grade, p2_grade, p3_grade)
    best = [i+1 for i, grade in enumerate([p1_grade, p2_grade, p3_grade]) if grade == grade_max]
    
    return best