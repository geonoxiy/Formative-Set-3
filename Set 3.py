def relationship_status(from_member, to_member, social_graph):

    Follower = social_graph[from_member]["following"]
    FollowedBy = social_graph[to_member]["following"]

    if to_member in Follower and from_member in FollowedBy:
        result = "friends"
    elif to_member in Follower:
        result = "follower"
    elif from_member in FollowedBy:
        result = "followed by"
    else:
        result = "no relationship"
    return result

def tic_tac_toe(board):

    for sublist in board:
        for i in range(len(sublist)):
            if sublist[i] == 'X':
                sublist[i] = int(1)
            elif sublist[i] == 'O':
                sublist[i] = int(0)
            else:
                sublist[i] = int(5)

    # HORIZONTAL

    horizontal = [sum(sublist) for sublist in board]
    
    # VERTICAL

    check_vertical =  list(zip(*board))
    vertical = [sum(sublist) for sublist in check_vertical]

    # DIAGONAL - NEGATIVE SLOPE

    listnumber_diagonal1 = 0
    check_diagonal1 = []

    while listnumber_diagonal1 < len(board):
        diagonal_sublist1 = board[listnumber_diagonal1][listnumber_diagonal1]
        listnumber_diagonal1 += 1
        check_diagonal1.append(diagonal_sublist1)

    # DIAGONAL - POSITIVE SLOPE

    listnumber_diagonal2 = 0
    check_diagonal2 = []

    while listnumber_diagonal2 < len(board):
        diagonal_sublist2 = board[listnumber_diagonal2][len(board) - 1 - listnumber_diagonal2]
        listnumber_diagonal2 += 1
        check_diagonal2.append(diagonal_sublist2)

    # FINAL DIAGONAL

    check_diagonal = [check_diagonal1, check_diagonal2]
    diagonal = [sum(sublist) for sublist in check_diagonal]

    # FINAL CHECKER

    if len(board) in diagonal or len(board) in vertical or len(board) in horizontal:
        result = "X"
    elif 0 in diagonal or 0 in vertical or 0 in horizontal:
        result = "O"
    else:
        result = "NO WINNER"
            
    return result


