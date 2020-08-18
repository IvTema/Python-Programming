# https://stepik.org/lesson/3380/step/1?thread=solutions&unit=963

games = []
team_names = []
winners = []
zero_zero = []
losers = []
goal_total = {}
final_out = {}
game_number = int(input())         # кол-во игр всего
for i in range(game_number):
    games += [input().split(";")]  # полный список всех игр
for j in range(game_number):
    team_names += [games[j][0]]    # все названия команд без пропусков для "всего игр"
    team_names += [games[j][2]]
for k in range(game_number):
    if int(games[k][1]) > int(games[k][3]):
        winners += [games[k][0]]               # спискок команд победителей
        losers += [games[k][2]]                # список команд проигравших
    elif int(games[k][1]) < int(games[k][3]):
        winners += [games[k][2]]
        losers += [games[k][0]]
    else:
        zero_zero += [games[k][0]]             # список команд в ничью
        zero_zero += [games[k][2]]
for z in range(game_number):                   # Суммарно очков по командам словарь goal_total
    if games[z][0] in goal_total:
        if games[z][1] > games[z][3]:
            goal_total[games[z][0]] = int(goal_total[games[z][0]]) + 3
        if games[z][1] == games[z][3]:
            goal_total[games[z][0]] = int(goal_total[games[z][0]]) + 1
    if games[z][0] not in goal_total:
        if games[z][1] > games[z][3]:
            goal_total[games[z][0]] = 3
        if games[z][1] < games[z][3]:
            goal_total[games[z][0]] = 0
        if games[z][1] == games[z][3]:
            goal_total[games[z][0]] = 1
    if games[z][2] in goal_total:
        if games[z][1] < games[z][3]:
            goal_total[games[z][2]] = int(goal_total[games[z][2]]) + 3
        if games[z][1] == games[z][3]:
            goal_total[games[z][2]] = int(goal_total[games[z][2]]) + 1
    if games[z][2] not in goal_total:
        if games[z][1] < games[z][3]:
            goal_total[games[z][2]] = 3
        if games[z][1] > games[z][3]:
            goal_total[games[z][2]] = 0
        if games[z][1] == games[z][3]:
            goal_total[games[z][2]] = 1
for u in goal_total:
    final_out[u] = []
    final_out[u].append(team_names.count(u))
    final_out[u].append(winners.count(u))
    final_out[u].append(zero_zero.count(u))
    final_out[u].append(losers.count(u))
    final_out[u].append(goal_total[u])
for key, value in final_out.items():
    print(key, ':', sep=(''), end=(''))
    print(*value)