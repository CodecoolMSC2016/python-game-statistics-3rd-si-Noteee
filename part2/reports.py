# 1
def get_most_played(file_name):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    most_played_title = ""
    played_list = []
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    for i in data_2dlist:
        played_list.append(float(i[1]))
    max_of_played_list = max(played_list)
    for i in data_2dlist:
        if float(i[1]) == max_of_played_list:
            most_played_title = i[0]
    return most_played_title

# 2
def sum_sold(file_name):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    played_list = []
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    for i in data_2dlist:
        played_list.append(float(i[1]))
    return sum(played_list)

# 3
def get_selling_avg(file_name):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    played_list = []
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    for i in data_2dlist:
        played_list.append(float(i[1]))
    return sum(played_list) / len(played_list)

# 4
def count_longest_title(file_name):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    title_list = []
    longest = 0
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    for i in data_2dlist:
        title_list.append(list(i[0]))
    for i in title_list:
        if len(i) > longest:
            longest = len(i)
        else:
            continue
    return longest

#5
def get_date_avg(file_name):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    year_list = []
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    for i in data_2dlist:
        year_list.append(float(i[2]))
    return round(sum(year_list) / len(year_list))

#6
def get_game(file_name, title):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    game_props = []
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    for i in data_2dlist:
        if i[0] == title:
            game_props.append(i[0])
            game_props.append(float(i[1]))
            game_props.append(int(i[2]))
            game_props.append(i[3])
            game_props.append(i[4])
            return game_props
    raise ValueError("theres no games matching that title")

# bonus1
def count_grouped_by_genre(file_name):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    genres = {}
    for i in range(len(data_2dlist)):
        if data_2dlist[i][3] not in genres:
            genres.update({data_2dlist[i][3]: genres.get(data_2dlist[i][3], 0) + 1})
        else:
            genres.update({data_2dlist[i][3]: genres.get(data_2dlist[i][3]) + 1})

    return genres
# bonus2
def get_date_ordered(file_name):
    fr = open(file_name, "r")
    data = fr.read().split("\n")
    data = filter(None, data)
    data_2dlist = []
    for i in data:
        data_2dlist.append(i.strip("\n").strip(" ").split("\t"))
    data_2dlist = sorted(data_2dlist, key=lambda v: v[0])
    data_2dlist = sorted(data_2dlist, key=lambda v: int(v[2]), reverse=True)
    list_of_titles = []
    for i in data_2dlist:
        list_of_titles.append(i[0])
    return list_of_titles

if __name__ == "__main__":
    main()
# Report functions
