def run():
    palindrome = lambda str: str.lower() == str.lower()[::-1]
    print(palindrome('Ana'))

if __name__ == '__main__':
    run()