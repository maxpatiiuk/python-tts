# Python TTS
This project formats txt file and uses [pyttsx3](https://pypi.org/project/pyttsx3/) to convert it to an `.mp3` file.

The idea behind this tool is to have a TXT file where the user would put web pages in read mode and other text-based information separated by `...` or other separation string you specify.

The script will read the data from the file, remove redundancy, adopt it for TTS and run `pyttsx3` on it 

# Configuration
All of the necessary settings are located in `config.py`.

## Changing voice
Depending on your system, there can be several voices installed. You will want to run `find_voice.py` to get the ID of the voice you like the most.

## Removing unnecessary lines from the file
When copying data from the webpage, you may get unnecessary information like date of the publication, titles for images, and author name even if using the reading mode provided by your browser.

You can run `find_common_lines.py` to see the list of the lines that are most commonly occurring in the file you provided. This would allow you to decide whether to add them to the `removal_list` or `regex_removal_list`

# Run
After specifying correct settings, execute the `run.py` file which will generate an `.mp3` file in the destination specified in the config file.
