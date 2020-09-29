import config
import pyttsx3
import re
import time
import sys
from io import StringIO
from html.parser import HTMLParser


def get_raw_text():

    if len(sys.argv) > 1:
        file_path  = sys.argv[1]
    else:
        file_path = config.source_file_location

    print('Reading text from file: %s' % file_path)

    with open(file_path, 'r') as file:
        return file.read()


def filter_text(text, optimize_for_tts=True):

    if config.strip_html:
        text = strip_html(text)

    if config.remove_unicode:
        text = remove_unicode(text)

    if config.remove_similar_pages:
        text = remove_similar_pages(text)

    text = remove_blacklisted(text)

    lines = text.split(config.line_separator)

    if config.remove_repeated_lines:
        lines = remove_repeated_lines(lines)

    if optimize_for_tts:
        lines = optimize_lines(lines)

    text = config.line_separator.join(lines)

    return text


def optimize_lines(lines):
    new_lines = []

    for line in lines:
        trimmed_line = line.strip()

        if trimmed_line == '':
            continue

        if trimmed_line[-1].isalnum():
            trimmed_line += '.'

        new_lines.append(trimmed_line)

    return new_lines


def strip_html(text):
    class MLStripper(HTMLParser):
        def __init__(self):
            super().__init__()
            self.reset()
            self.strict = False
            self.convert_charrefs = True
            self.text = StringIO()

        def handle_data(self, d):
            self.text.write(d)

        def get_data(self):
            return self.text.getvalue()

    s = MLStripper()
    s.feed(text)
    return s.get_data()


def remove_unicode(text):
    regex_pattern = re.compile(pattern="["
                                       u"\U0001F600-\U0001F64F"  # emoticons
                                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                       "]+", flags=re.UNICODE)
    return regex_pattern.sub(r'', text)


def remove_blacklisted(text):
    for removal_text in config.removal_list:
        text = text.replace('%s%s%s' % (config.line_separator, removal_text, config.line_separator), '')

    for removal_regex in config.regex_removal_list:
        text = re.sub(removal_regex, '', text)

    return text


def remove_similar_pages(text):
    pages = text.split(config.initial_page_separator)
    result_pages = []

    for page in pages:
        new_page = page.strip()
        if new_page not in result_pages:
            result_pages.append(new_page)

    return (config.line_separator+config.end_page_separator+config.line_separator).join(result_pages)


def remove_repeated_lines(lines):

    new_lines = []

    for line in lines:
        if not new_lines or new_lines[-1] != line:
            new_lines.append(line)

    return new_lines


def get_speech_engine(use_default_voice=True):
    engine = pyttsx3.init()
    engine.setProperty('rate', config.speaking_rate)
    engine.setProperty('volume', config.speaking_volume)

    if use_default_voice:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[config.speaking_voice].id)

    return engine


def save_to_txt(text):
    with open(config.destination_txt_file_location, 'w') as file:
        file.write(text)


def save_to_mp3(engine, text):
    engine.save_to_file(text, config.destination_mp3_file_location)
    engine.runAndWait()


def exit_voice_engine(engine):
    engine.stop()


def get_line_separator():
    return config.line_separator


def get_pages_count(text):
    return text.count(config.line_separator + config.initial_page_separator + config.line_separator)


def get_current_time():
    return int(round(time.time()*1000))/1000
