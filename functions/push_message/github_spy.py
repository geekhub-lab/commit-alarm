from github import Github
from datetime import datetime, timedelta


# 최근 24시간 내 커밋 있으면 True, 없으면 False 반환
def committed_in_a_day(email, pw):
    g = Github(email, pw)

    repo_list = []
    for repo in g.get_user().get_repos():
        repo_list.append(repo)

    last_commit_list = []
    delta = datetime.now() - timedelta(days=1)
    for index, repo in enumerate(repo_list):
        print str(index+1) + " of " + str(len(repo_list)) + " repo name: " +repo.name
        try:
            last_commit_list.extend(repo.get_commits(since=delta, author=g.get_user().login).get_page(0))
        except:
            pass

    print "\n commits below:"
    for index, item in enumerate(last_commit_list):
        print "user: " + item.commit.committer.name + " msg: " + item.commit.message

    if len(last_commit_list) == 0:
        return False
    else:
        return True


