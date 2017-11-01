usernme = input('Enter your User Name: ')
pwrd = input('Enter a password between 6-12 characters: ')
conpwrd = input('Confirm your password: ')
banned_words = ('Password' 'password' 'sesame' 'Sesame' 'Letmein' 'LetMeIn' 'Qwerty' 'Cheese')
if pwrd in banned_words:
        print('That password is not allowed, please choose a different one.')
elif pwrd == conpwrd and len(pwrd) >= 6 and len(pwrd) <= 12:
        print('Password changed')
else:
        print('Passwords do not fit requirements, re-enter.')