tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    if len(klasses) < len(tutors):
        diff = len(tutors) - len(klasses)
        while diff:
            klasses.append(None)
            diff -= 1
    for tut, klass in zip(tutors, klasses):
    #print(type(t_k))
        yield (tut, klass)
        

print(check_gen(tutors, klasses))
generator = check_gen(tutors, klasses)
## добавьте здесь доказательство, что создали именно генератор
print(type(generator))

for _ in range(len(tutors)):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
