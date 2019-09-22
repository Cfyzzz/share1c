import re
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

spec_symbols = r'().,:;*+-/=[]{}<>?&'

key_words_query = ['выбрать', 'из', 'где', 'сгруппировать по', 'имеющие', 'соединение', 'левое',
                   'правое', 'полное', 'левое полное соединение', 'по',
                   'правое полное соединение', 'левое внутреннее соединение', 'правое внутреннее соединение',
                   'внутреннее соединение']

key_words = ['истина', 'ложь', 'новый', 'процедура', 'конецпроцедуры', 'для', 'цикл', 'конеццикла', 'прервать',
             'продолжить', 'для каждого', 'из', 'если', 'тогда', 'иначеесли', 'иначе', 'конецесли', 'перейти',
             'перем', 'экспорт', 'пока', 'попытка', 'исключение', 'конецпопытки', 'вызватьисключение', 'возврат',
             'функция', 'конецфункции', 'null', 'и', 'не']

temp_ram = r'//*'
temp_quote = r'"[^"]*"'

HLSS = "hlss"
HLKWQ = "hlkwq"
HLKW = "hlkw"
HLR = "hlr"
HLQ = "hlq"


@register.filter(name="format1c")
@stringfilter
def format_1c(value):
    result = ""
    for line in map(str, value.split('\n')):
        line_ram = re.search(temp_ram, line)
        if line_ram:
            if line_ram.start():
                line1 = format_1c_line(line[:line_ram.start() - 1])
                line2 = format_1c_line(line[line_ram.start():])
                result += line1 + line2 + '\n'
            else:
                result += format_1c_line(line[:]) + '\n'
        else:
            quotes = list(re.finditer(temp_quote, line))
            if quotes:
                next_idx = 0
                for quote in quotes:
                    if quote.start() > next_idx:
                        line1 = format_1c_line(line[next_idx: quote.start()])
                        line2 = format_1c_line(line[quote.start(): quote.end()])
                        result += line1 + line2
                        next_idx = quote.end()
                    else:
                        result += format_1c_line(line[quote.start(): quote.end()])

                result += format_1c_line(line[next_idx:])
                result += '\n'
            else:
                result += format_1c_line(line) + '\n'

    return result


def format_1c_line(row_line):
    result = ""
    line = row_line.lower()
    ram = re.search(temp_ram, row_line)
    if ram:
        result = wrap(row_line[ram.start():-1], HLR)
        return result

    qoute = re.search(temp_quote, row_line)
    if qoute:
        result = wrap(row_line[qoute.start():qoute.end()], HLQ)
        return result

    old_tag = ''
    phrase = ''
    # row_word = ''
    # idx = -1
    separate_line = [i for i in re.split(r'(\s+)|(\w+)|(\W)', line) if i]
    separate_row_line = [i for i in re.split(r'(\s+)|(\w+)|(\W)', row_line) if i]

    for idx, word in enumerate(separate_line):
        row_word = separate_row_line[idx]
        if word in spec_symbols:
            tag = HLSS
        elif word in key_words_query:
            tag = HLKWQ
        elif word in key_words:
            tag = HLKW
        else:
            tag = ''

        if old_tag == tag:
            phrase += row_word
        else:
            result += wrap(phrase, old_tag)
            phrase = row_word

        old_tag = tag

    # if phrase != row_word or idx == 0:
    result += wrap(phrase, old_tag)

    return result


def wrap(phrase, tag_class_name):
    if tag_class_name == '':
        return phrase
    return "<snap class='{0}'>{1}</snap>".format(tag_class_name, phrase)
