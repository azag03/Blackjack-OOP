def is_number(testValue):
    """Returns True if testValue is a number and False otherwise."""
    testValue = str(testValue).strip()
    isNumber = True

    if testValue in ['', '+', '-', '.']:
        isNumber = False

    positionCounter = 0
    plusMinusCounter = 0
    decimalCounter = 0
    legalValues = '+-.0123456789'
    while positionCounter < len(testValue):
        if testValue[positionCounter] not in legalValues:
            isNumber = False
        if testValue[positionCounter] in ['+', '-']:
            plusMinusCounter += 1
        if plusMinusCounter > 1:
            isNumber = False
        if testValue[positionCounter] == '.':
            decimalCounter += 1
        if decimalCounter > 1:
            isNumber = False
        positionCounter += 1
    return isNumber


def get_integer(prompt="Enter your guess:"):
    """Ask the user a question and verify that they enter an integer and return it."""
    if prompt[-1] != ' ':
        prompt += ' '
    userGuess = input(prompt)
    #
    # Modify the prompt in case the user doesn't input an integer
    #
    prompt += '(integers only) '
    while not is_integer(userGuess):
        userGuess = input(prompt)
    userGuess = int(float(userGuess))
    return userGuess


def get_integer_between(lowerLimit, higherLimit, prompt="Enter your guess:"):
    """Ask the user a question and verify that they enter an integer and return it."""
    if prompt[-1] != ' ':
        prompt += ' '
    userGuess = get_integer(prompt)
    #
    # Modify the prompt in case the user doesn't input an integer
    #
    prompt += f"(between {lowerLimit} and {higherLimit})"
    while userGuess < lowerLimit or userGuess > higherLimit:
        userGuess = get_integer(prompt)
    return userGuess


def is_integer(userGuess):
    """Returns True if testValue is an integer and False otherwise."""

    userGuess = str(userGuess).strip()
    isInteger = True

    if userGuess in ['', '-', '+', '.']:
        isInteger = False

    positionCounter = 0
    plusMinusCounter = 0
    decimalCounter = 0
    legalValues = '+-.0123456789'
    while positionCounter < len(userGuess):
        if userGuess[positionCounter] not in legalValues:
            isInteger = False
        if userGuess[positionCounter] in ['+', '-']:
            plusMinusCounter += 1
        if plusMinusCounter > 1:
            isInteger = False
        if userGuess[positionCounter] == '.':
            legalValues = '0'
            decimalCounter += 1
        if decimalCounter > 1:
            isInteger = False
        positionCounter += 1
    return isInteger


def get_boolean(prompt):
    """Asks the user a yes or no question and returns 'yes' or 'no'. Will ask the user for clarification if it can't
    figure out what they mean."""
    #
    # If there isn't a space at the end of the prompt, add a space to the end.
    #
    if prompt[-1] != " ":
        prompt = prompt + " "
    answer = input(prompt)
    answer = answer.lower()
    if answer in ['yes', 'y', 'sure', 'yep', 'si', 'da', 'ja', 'you bet', 'ok']:
        answer = True
    elif answer in ['no', 'n', 'nope', 'nyet', 'nein']:
        answer = False
    else:
        #
        # If we can't figure out what their answer means, ask them what it means.
        #
        newPrompt = 'Does ' + answer + ' mean yes or no? '
        answer = get_boolean(newPrompt)
    print()
    return answer
