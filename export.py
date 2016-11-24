import reports as r
def export():
    fw = open("answers.txt", "w")
    fw.writelines([str(r.count_games("game_stat.txt")) + "\n",
                   str(r.decide("game_stat.txt", 2000)) + "\n",
                   str(r.get_latest("game_stat.txt")) + "\n",
                   str(r.count_by_genre("game_stat.txt", "Real-time strategy")) + "\n",
                   str(r.get_line_number_by_title("game_stat.txt", "Minecraft")) + "\n",
                   str(r.sort_abc("game_stat.txt")) + "\n",
                   str(r.get_genres("game_stat.txt")) + "\n",
                   str(r.when_was_top_sold_fps("game_stat.txt")) + "\n"])


export()

# Export functions
