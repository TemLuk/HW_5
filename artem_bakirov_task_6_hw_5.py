set1 = {1, 2, 3}
set1.add(4)
set1.clear()
set2 = set1.copy()
set1.difference(set2)
set1.discard(2)
set1.intersection(set2)
set1.isdisjoint([2, 3])
set1.issubset([4])
set1.issuperset([1, 3])
set1.pop()
set1.remove(3)
set1.union(set2)
set1.update(set2)
