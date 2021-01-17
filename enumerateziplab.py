projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for project,leader in list(zip(projects,leaders)):
    print(f'The leader of {project} is {leader}')

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for p,l,d in list(zip(projects,leaders,dates)):
    print(f'The leader of {p} started {d} is {l}')


for x, (p,l,d) in enumerate(zip(projects,leaders, dates)):
    print(f'{x+1}- The leader of {p} started {d} is {l}')