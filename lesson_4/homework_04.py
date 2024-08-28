adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(f"Count of letter 'h' in text is: {adwentures_of_tom_sawer.count('h')}")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
counter = 0
for word in adwentures_of_tom_sawer.split():
    if word[0].isupper():
        counter += 1
print(f"Text contains {counter} words with first upper letter")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_position_index = adwentures_of_tom_sawer.find("Tom")
second_position_index = adwentures_of_tom_sawer.find("Tom", first_position_index+1)
print(f"First position of Tom is {first_position_index}")
print(f"Second position of Tom is {second_position_index}")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.strip(".").split(".")
# delete spaces
for index, sentence in enumerate(adwentures_of_tom_sawer_sentences):
    adwentures_of_tom_sawer_sentences[index] = sentence.strip()
print("\n".join(adwentures_of_tom_sawer_sentences))
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(f"Fourth sentence is: {adwentures_of_tom_sawer_sentences[3]}")
adwentures_of_tom_sawer_sentences[3] = adwentures_of_tom_sawer_sentences[3].lower()
print(f"Lower sentence is: {adwentures_of_tom_sawer_sentences[3]}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
# no find, because in task 08 I made sentence with "By the time" to lower

by_the_time_is_found = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        by_the_time_is_found = True
        break
text_to_print = "By the time is found!" if by_the_time_is_found else "By the time didn`t found"
print(f"result is: {text_to_print}")

# but if I capitalise sentence it will found
adwentures_of_tom_sawer_sentences[3] = adwentures_of_tom_sawer_sentences[3].capitalize()
by_the_time_is_found = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        by_the_time_is_found = True
        break
text_to_print = "By the time is found!" if by_the_time_is_found else "By the time didn`t found"
print(f"result is: {text_to_print}")
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

print(f"Count of words in last sentence is: {len(adwentures_of_tom_sawer_sentences[-1].split())}")
