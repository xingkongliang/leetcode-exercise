result = []

def backtrack(path, [option1, option2]):
    if 满足结束条件:
        result.add(path)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径，选择列表)
        撤销选择

