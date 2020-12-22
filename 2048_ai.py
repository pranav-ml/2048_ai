from logics import *

def mcst_move(board,number_of_searches,depth):
    possible_moves=[move_up,move_left,move_down,move_right]
    move_scores=[0 for _ in range(4)]
    for first_move_ind in range(4):
        first_board=[x[:] for x in board]
        first_board,is_valid,first_score=possible_moves[first_move_ind](first_board)
        if is_valid:
            first_board=add_new_tile(first_board)
            move_scores[first_move_ind]+=first_score
        else:
            continue
        for _ in range(number_of_searches):
            mov_no=1
            search_board=[x[:] for x in first_board]
            valid=True
            while valid and mov_no<depth:
                search_board,valid,search_score=random_move(search_board)
                if valid:
                    search_board=add_new_tile(search_board)
                    move_scores[first_move_ind]+=search_score
                    mov_no+=1
    best_move_ind=move_scores.index(max(move_scores))

    best_board,valid,_=possible_moves[best_move_ind](board)
    return best_board,valid

