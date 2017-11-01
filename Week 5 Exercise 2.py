number_of_pupils = int(input('Enter the amount of pupils: '))
if number_of_pupils < 0:
    print('Input invalid, enter a number that is not less than 0.')
if number_of_pupils == 0:
        print('Input invalid, enter a number that is more than 0.')
        print(number_of_pupils)
        football_teams = number_of_pupils / 5
        print(football_teams)
        x = football_teams
        x = int(x)
        children_in_teams = x * 5
        children_left_out = number_of_pupils - children_in_teams
        print(children_left_out)