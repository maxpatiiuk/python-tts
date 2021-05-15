import utilites

# voices_to_try = []  # leave empty to try all
voices_to_try = [5, 34]
# voices_to_try = [5, 18, 29, 34, 38]


engine = utilites.get_speech_engine(use_default_voice=False)
voices = engine.getProperty('voices')


def sample_voice(voice_id):

    if not voices[voice_id]:
        print('Voice number %i is not found on your system' % voice_id)
        return

    # string = "Hello! I am voice number %i" % voice_id
    # string += """
    #     Search Results. Featured snippet from the web. There is a built-in function called len() for getting the total
    #     number of items in a list, tuple, arrays, dictionary, etc. The len() method takes an argument where you may
    #     provide a list and it returns the length of the given list"""
    string = """Custom Voice (beta)
Train a custom speech synthesis model using your own audio recordings to create a unique and more natural-sounding voice for your organization. You can define and choose the voice profile that suits your organization and quickly adjust to changes in voice needs without needing to record new phrases. Learn more.

WaveNet voices
Take advantage of 90+ WaveNet voices built based on DeepMind’s groundbreaking research to generate speech that significantly closes the gap with human performance.

Voice tuning
Personalize the pitch of your selected voice, up to 20 semitones more or less from the default. Adjust your speaking rate to be 4x faster or slower than the normal rate.

Text and SSML support
Customize your speech with SSML tags that allow you to add pauses, numbers, date and time formatting, and other pronunciation instructions."""

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
