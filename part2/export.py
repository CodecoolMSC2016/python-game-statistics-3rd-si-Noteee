import reports as r
def export():
    fw = open("reports.txt", "w")
    fw.writelines([str(r.count_grouped_by_genre("game_stat.txt")) + "\n",
                   str(r.get_date_ordered("game_stat.txt")) + "\n",
                   str(r.get_most_played("game_stat.txt")) + "\n",
                   str(r.sum_sold("game_stat.txt")) + "\n",
                   str(r.get_selling_avg("game_stat.txt")) + "\n",
                   str(r.count_longest_title("game_stat.txt")) + "\n",
                   str(r.get_date_avg("game_stat.txt")) + "\n",
                   str(r.get_game("game_stat.txt", "Diablo III")) + "\n"])
export()
