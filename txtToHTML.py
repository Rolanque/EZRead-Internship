import math
html = '<!DOCTYPE html> <html><head><title>Page Title</title></head><style>body { background: repeating-linear-gradient(to bottom, #004AAD 0px 75px, #FEFCE8 75px 1122px);}</style><body><div><h1 style="color:#ffffff; width: 100%;"> &nbsp &nbsp The Sociological Imagination: Chapter 1</h1></div><div><br><ul>'
txt_summary = open("summary.txt", "r").read()

bullet_point_count = 0
word_count = 0
line_length = 0
bullet_point_length = 0
average_sentence_length = 18
page_word_threshold = 780
max_word_count = 870

for bullet_point in txt_summary.split('*'):

    if len(bullet_point) != 0:
        bullet_point_count += 1
        bullet_point = "<li>" + bullet_point[1:] + "</li>"
        bullet_point_length = bullet_point.count(" ") + 1
        word_count += bullet_point_length
        line_length += math.ceil(bullet_point_length / average_sentence_length)

        if word_count < page_word_threshold:
           html += bullet_point

        else: 
            html += '</ul>'
            while word_count < max_word_count:
                html += '<br>'
                word_count += average_sentence_length
            html += '<br><div><h1 style="color:#ffffff; width: 100%; padding-top: 15px"> &nbsp &nbsp The Sociological Imagination: Chapter 1</h1></div><br><ul>'
            html += bullet_point
            bullet_point_count = 1
            word_count = bullet_point.count(" ") + 1
            line_length = 0

html += "</ul></body></html>"
with open("yourhtmlfile.html", "w") as file:
    file.write(html)

