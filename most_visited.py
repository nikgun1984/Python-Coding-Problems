from collections import defaultdict, Counter
from itertools import combinations


class MostVisited:

    def most_visited_pattern(self, username, timestamp, website):
        by_user = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            by_user[u].append(w)

        cnt = Counter()
        for x in by_user.values():
            cnt += Counter(set(combinations(x, 3)))

        return min(cnt, key=lambda k: (-cnt[k], k))


obj = MostVisited()

names = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"]
timestamps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sites = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]

a = obj.most_visited_pattern(names, timestamps, sites)
print(a)
