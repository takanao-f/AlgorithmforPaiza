# SNSのログからフォロー操作を復元
# ログ
# 1 1 2  ユーザ１がユーザ２をフォローする
# 2 6   ユーザ6がその時点でユーザ６をフォローしている全員をフォローする
# 3 8   8がフォローしている各ユーザxに対して、ユーザｘがフォローしているユーザを全てフォローする

# 機能１フォロー
USER_SUM, OPERATION = map(int, input().split())
graph = []

def follow(user, follow_user):
    graph[user][follow_user] = True

# 機能２フォロー返し
def follow_rep(user):
    follower = []
    for user_num in range(0,USER_SUM):
        if graph[user_num][user]:
            follower.append(user_num)
    for new_follower in follower:
        follow(user, new_follower);        
    
# 機能３フォローフォロー
def follow_to_follow(user):
    new_follows = []    
    for user_num in range(0,USER_SUM):
        if graph[user][user_num]:
            for user_num2 in range(0,USER_SUM):
                if graph[user_num][user_num2]:
                    new_follows.append(user_num2)      
    for new_follow in new_follows:
        follow(user, new_follow)        
    

if __name__ == '__main__':
    
    # 隣接行列の作成
    graph = [[False] * 6 for _ in range(USER_SUM)]
    
    # オペレーション読み込み
    for log_num in range(0, OPERATION):
        operate_command = list(map(int, input().split()))
        user = operate_command[1] - 1
        command = operate_command[0]
        if command == 1:
            follow(user, operate_command[2]-1)
        if command == 2:
            follow_rep(user)
        if command == 3:
            follow_to_follow(user)
    # 結果出力
    for line in graph:
        print(line)
        
