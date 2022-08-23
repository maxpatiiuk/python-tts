source_file_location = '/Users/maxpatiiuk/site/git/private-dotfiles/notes/TEMP'
destination_txt_file_location = 'result.txt'
destination_mp3_file_location = '/Users/maxpatiiuk/Downloads/result.mp3'

line_separator = '\n'
initial_page_separator = '...'
end_page_separator = '...'

remove_unicode = True
strip_html = True
remove_similar_pages = True
remove_repeated_lines = True

speaking_voice = 5  # run find_voice.py to find the voice you like
speaking_rate = 300  # default is 200
#speaking_rate = 350  # default is 200
speaking_volume = 1.0  # default is 1.0. the range of possible values: [0.0,1.0]

# run find_common_lines.py to see the list of the commonly used lines that you want to exclude
removal_list = [
    'Advertisement',
    'RECOMMENDED VIDEOS FOR YOU...',
    'Image for post',
    'Quincy Larson',
    'Eric Leung',
    'Karl Hughes',
    'Sam Williams',
    'Jason Evangelho',
    'Milecia McGregor',
    'A version of this article appeared in the “Musk Reads” newsletter. Sign up for free here.',
    'Got any comments or queries? Don’t forget to send them over to muskreads@inverse.com.',
    'logout',
    'Watch on YouTube',
    'ADVERT',
    'Share via',
    'Copy link',
    'Related Topics:',
    'Subscribe to Visual Capitalist',
    'Get your mind blown on a daily basis:',
    'If you read this far, tweet to the author to show them you care. Tweet a thanks',
    'Recommended Reading:',
    'Sponsored Content',
    'Learn to code for free. freeCodeCamp\'s' +
    ' open source curriculum has helped more than 40,000 people get jobs as developers. Get started',
    'Image for post',
    'MORE:',
    'RELATED:',
    'RELATED: ',
    '____________________________________',
    '.',
    'Painting by the author Javier Ideami@ideami.com',
    'Conclusion',
    'Featured Videos From The Verge',
    'If you buy something from a Verge link, Vox Media may earn a commission. See our ethics statement.',
    'More from The Verge',
    '(Image credit: Shutterstock)',
    'Credit',
    'Continue scrolling to keep reading',
    'Click the button below to start this article in quick view.',
    'Getty Images',
    'Final Thoughts',
    'More about',
    'SUMMARY',
    'Related Story',
    'Share this:',
    'Share',
    'KEY FACT',
    'newsletter promo',
    'Sign up for Scientific American’s free newsletters. Sign Up',
    'ADVERTISEMENT',
    'This is an opinion and analysis article; the views expressed by ' +
    'the author or authors are not necessarily those of Scientific American.',
    '(Summary of changes)',
    'Merge made by recursive.',
    'Credit: Getty Images',
    'Source',
    'Alexandru Paduraru',
    'Share on LinkedIn',
    'Calendar Icon',
    'Source: Bloomberg',
    'Sign Up',
    
    # '',
]

regex_removal_list = [
    r"\n\d+\n",
    r"Last modified on [^\n]+",
    r"(Mon|Tue|Wed|Thu|Fri|Sat|Sun) \d{1,2} [^\n]+",
    r"\d{1,2} (January|February|March|April|May|June|July|August|September|October|November|December) [^\n]+",
    r"Image source and credits: [^\n]+",
    # r"",
]
