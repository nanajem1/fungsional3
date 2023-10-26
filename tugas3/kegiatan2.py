data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

integer_data = []

for item in data:
    parts = item.split()
    integers = list(filter(lambda x: x.isdigit(), parts))
    integer_data.append(integers)

for item in integer_data:
    print(item)