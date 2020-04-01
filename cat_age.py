
cat_age = input('Please enter cat age')

cat_age = int(cat_age)

if cat_age >= 0:
    if cat_age < 2:
        print('what a cute kitten!')
    elif cat_age < 9:
        print('What an old cat')
        if cat_age == 7:
            print('And 7 is such a good age!')
    else:
        print('Boring cat')
