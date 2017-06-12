import numpy.random as random

random.seed(1234)

n_tests = 10000

win_doors = random.randint(0, 3, n_tests)

change_mind_wins = 0
insist_wins = 0

for win_door in win_doors:
	first_try = random.randint(0, 3)

	remaining_choices = [i for i in range(3) if i != first_try]

	wrong_choices = [i for i in range(3) if i != win_door]

	if first_try in wrong_choices:
		wrong_choices.remove(first_try)

	screened_out = random.choice(wrong_choices)
	remaining_choices.remove(screened_out)

	change_mind_try = remaining_choices[0]

	if (change_mind_try == win_door):
		change_mind_wins += 1
	else:
		insist_wins += 1

print(
    'You win {1} out of {0} tests if you changed your mind\n'
    'You win {2} out of {0} tests if you insist on the initial choice'.format(
        n_tests, change_mind_wins, insist_wins
        )
)