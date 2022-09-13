from collections import defaultdict

def solution(genres, plays):
    # Make album group by genre
    album = defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        album[genre].append([i, play])
    
    # Count sum for each genre
    genre_sum = []
    for genre, play_list in album.items():
        play_sum = [sum(i) for i in zip(*play_list)][1]
        genre_sum.append([genre, play_sum])

   # Rank genre
    genre_sum_sorted = sorted(genre_sum, key=lambda x: x[1], reverse=True)
    genre_rank = [genre for genre, play_sum in genre_sum_sorted]

    answer = []
    for genre in genre_rank:
        play_list = album[genre]
        best_two = sorted(play_list, key=lambda x: x[1], reverse=True)
        best_two = best_two[:2]
        if len(best_two) == 2:
            if best_two[0][1] == best_two[1][1]:
                best_two = sorted(best_two, key=lambda x: x[0])
        answer.extend([idx for idx, play in best_two])
    
    return answer