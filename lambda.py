# lambda <arguments>: <expresion>
def run():

    # def palindrome(string):
    #     return string == string[::-1]

    palindrome = lambda string: string == string[::-1]

    print(palindrome('ana'))

if __name__ == '__main__':
    run()