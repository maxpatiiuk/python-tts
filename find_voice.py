import utilites

voices_to_try = []  # leave empty to try all
# voices_to_try = [5, 18, 34]


engine = utilites.get_speech_engine(use_default_voice=False)
voices = engine.getProperty('voices')


def sample_voice(voice_id):

    if voice_id not in voices:
        print('Voice number %i is not found on your system' % voice_id)
        return

    string = "Hello! I am voice number %i" % voice_id
    # string += """
    #     Search Results. Featured snippet from the web. There is a built-in function called len() for getting the total
    #     number of items in a list, tuple, arrays, dictionary, etc. The len() method takes an argument where you may
    #     provide a list and it returns the length of the given list"""

    engine.setProperty('voice', voices[voice_id].id)
    engine.say(string)
    print(string)
    engine.runAndWait()


if voices_to_try:
    for voice_number in voices_to_try:
        sample_voice(voice_number)
else:
    for voice_number in range(len(voices)):
        sample_voice(voice_number)

utilites.exit_voice_engine(engine)
