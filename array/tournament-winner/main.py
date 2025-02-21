def tournamentWinner(competitions, results):
    # Write your code here.
    endResults = {}
    for player in range(len(competitions)):
        print(competitions[player], results[player])
        if results[player] == 1:
            print('Team ' + competitions[player][0] + ' won.')
            if competitions[player][0] in endResults:
                endResults[competitions[player][0]] += 3
            else:
                endResults[competitions[player][0]] = 3
        else:
            print('Team ' + competitions[player][1] + ' won.')
            if competitions[player][1] in endResults:
                endResults[competitions[player][1]] += 3
            else:
                endResults[competitions[player][1]] = 3

    print(max(endResults, key=endResults.get))
    return max(endResults, key=endResults.get)
