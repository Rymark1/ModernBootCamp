import csv


def update_users(fo, lo):
    cnt = 0
    with open("users.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data = []
        for row in reader:
            if row[0] == fo and row[1] == lo:
                cnt += 1
            else:
                data.append(row)

    with open("users.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data)
    return cnt


print(update_users("Grace", "Hopper"))
print(update_users("Colt", "Steele"))
print(update_users("Not", "Here"))
