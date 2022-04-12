def get_boolean(prompt):
    """Asks the user a yes or no question and returns 'yes' or 'no'.
    Will ask the user for clarification if it can't figure out what they mean."""
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
        newPrompt = 'Does '+answer+' mean yes or no? '
        answer = get_boolean(newPrompt)
    return answer