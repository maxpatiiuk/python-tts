import utilites

text = utilites.get_raw_text()
text = utilites.filter_text(text, optimize_for_tts=False)

line_limit = 100

lines = text.split(utilites.get_line_separator())
lines_dict = {}
for line in lines:
    if line in lines_dict:
        lines_dict[line] = lines_dict[line] + 1
    else:
        lines_dict[line] = 1

sorted_lines_dict = {k: v for k, v in sorted(lines_dict.items(), key=lambda item: item[1], reverse=True)}

for string, count in sorted_lines_dict.items():
    print("%i\t%s" % (count, string))
    line_limit = line_limit - 1

    if line_limit == 0:
        break
