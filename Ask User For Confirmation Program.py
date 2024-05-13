def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while retries > 0:
        ok = input(prompt)
        if ok.lower() in ('y', 'ye', 'yes'):
            return True
        if ok.lower() in ('n', 'no', 'nop', 'nope'):
            return False
        retries -= 1
        print(complaint)
    raise IOError('Refusenik user')

reply = ask_ok('Now answer these questions: ')
if reply:
    print("Number of people (age +12): ")
    print("Number of children (age 2-11): ")
    print("Number of infants (age -2): ")
else:
    print('Goodbye!')

print("PROGRAM TERMINATED")