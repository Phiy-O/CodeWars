def validate_hello(greetings):
    #your code here
    words = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    
    for word in words:
        if word in greetings.lower():
            return True
    return False
