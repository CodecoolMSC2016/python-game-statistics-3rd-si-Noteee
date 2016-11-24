#1
def count_games(file_name):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    fr.close()
    counter = 0
    for i in data:
        counter += 1
    return counter
#2
def decide(file_name, year):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    for i in data_2dlist:
        if int(i[2]) == year:
            return True
    return False
#3
def get_latest(file_name):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    latestyear = 0
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    for i in data_2dlist:
        if int(i[2]) > latestyear:
            latestyear = int(i[2])
    for i in data_2dlist:
        if latestyear == int(i[2]):
            return i[0]
#4
def count_by_genre(file_name, genre):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    counter = 0
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    for i in data_2dlist:
        if i[3] == genre:
            counter += 1
    return counter
#5
def get_line_number_by_title(file_name, title):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    for i in range(len(data_2dlist)):
        if data_2dlist[i][0] == title:
            return i+1
    raise ValueError("Could not find it")

#bonus1
def  sort_abc(file_name):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    game_names = []
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    for i in sorted(data_2dlist):
        game_names.append(i[0])
    return game_names

#bonus2
def get_genres(file_name):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    game_genres = []
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    for i in (data_2dlist):
        game_genres.append(i[3])
    return sorted(list(set(game_genres)), key=lambda v: v.lower())

#bonus3
def when_was_top_sold_fps(file_name):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    shooter_list = []
    sold_max = 0
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    for i in (data_2dlist):
        if i[3] == "First-person shooter":
            shooter_list.append(i)
    for i in shooter_list:
        if sold_max < float(i[1]):
            sold_max = float(i[1])
    for i in shooter_list:
        if sold_max == float(i[1]):
            return int(i[2])

# Report functions

if __name__ == "__main__":
    main()


