size=400
grid_len=4
grid_padding=4
win_score=2048
background_color_game="#92877d"
background_color_cell_empty="#9e948a"

BACKGROUND_COLOR_DICT = {2: "#eee4da", 4: "#ede8c8", 8: "#f2b179",16: "#f59563", 32: "#f67c5f", 64: "#f65e3b",
                         128: "#edcf72", 256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
CELL_COLOR_DICT = {2: "#776e65", 4:"#776e65", 8: "#f9f6f2", 16: "#f9f6f2",32: "#f9f6f2", 64: "#f9f6f2",
                   128: "#f9f6f2", 256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2",2048: "#f9f6f2"}
FONT = ("Verdana", 40, "bold")
key_up="Up"
key_down="Down"
key_right="Right"
key_left="Left"
ai_key="'p'"
# Feel free to meddle with the following parameters.Increasing them increases time per move, along with the probability of winning.
max_depth=50 # how deep you want the algorithm to check the board.(recommended- 20-80)
searches_per_move=50 # how many random samples to be generated at each level (recommended- 20-80)
