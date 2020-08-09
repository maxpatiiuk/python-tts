import utilites

starting_time = utilites.get_current_time()

print('Reading text from the file')
text = utilites.get_raw_text()

print('Number of stories: %i' % utilites.get_pages_count(text))


print('Reshaping text')
text = utilites.filter_text(text)
text = utilites.filter_text(text)

print('Saving to txt')
utilites.save_to_txt(text)

print('Generating mp3 file. This can take a while...')
engine = utilites.get_speech_engine()
utilites.save_to_mp3(engine, text)
utilites.exit_voice_engine(engine)

print('Done!')

ending_time = utilites.get_current_time()

print(ending_time, starting_time)
print('Duration: %ds' % (ending_time - starting_time))
