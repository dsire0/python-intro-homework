onedotlist= ["Java", "Python", "Ruby"]
twodotlist  = ["Java", "Javascript", "Rust", "Ruby"]
onedotlist = set(onedotlist)
twodotlist = set(twodotlist)

onedotunion = onedotlist.union(twodotlist)
print(onedotunion)
onedotintersection = onedotlist.intersection(twodotlist)
print(onedotintersection)
onedotdifference = onedotlist.difference(twodotlist)
print(onedotdifference)