import telebot
import random

people_who_want_a_burrito = set()

bot = telebot.TeleBot("156611535:AAG9OvxZHbt_wR9B9SfOR8HcmHOgCG7K5r0")

@bot.message_handler(commands=["burrito"])
def register_interest_in_burrito(message):
    global people_who_want_a_burrito
    people_who_want_a_burrito.add(message.from_user.first_name)
    bot.reply_to(message, "You want a burrito today, noted")

def anglicized_list(set_of_names, highlight_names=True):
    list_of_names = list(set_of_names)

    if highlight_names == True:
        list_of_names = ['*'+x+'*' for x in list_of_names]

    if len(list_of_names) == 0:
        return ''
    elif len(list_of_names) == 1:
        return list_of_names[0]
    elif len(list_of_names) > 1:
        return ", ".join(list_of_names[:-1]) + " and " +list_of_names[-1]

@bot.message_handler(regexp="(?i)(up.*for)|(want).*[burito]{6,7}\?")
def who_wants_a_burrito(message):
    global people_who_want_a_burrito
    if len(people_who_want_a_burrito) > 0:
        _string = anglicized_list(people_who_want_a_burrito)+" previously mentioned they might be up for one. (I can't tell the time, so it might've been a while ago...)"
        bot.send_message(message.chat.id, _string, parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "I've not heard anything", parse_mode='Markdown')
        
@bot.message_handler(regexp="(?i)[lL]ove.*[buritoBURITO]{6,7}")
def proclaim_love(message):
    possible_prefixes = [
        'Thinking about it,',
        'You must understand that',
        'What a coincidence!',
        "I'm a robot, but"
    ]
    possible_verbs = [
        'am crazy for',
        'love',
        'have deep emotions for',
        'have an interest in',
        'often find myself casually adoring',
        'would rob a bank for',
        'would trade my parity bit for'
    ]
    verb = random.choice(possible_verbs)
    if(random.randint(0,2) == 0):
        prefix = random.choice(possible_prefixes)
        bot.send_message(message.chat.id, prefix+" I "+verb+" burritos")
    else:
        bot.send_message(message.chat.id, "I "+verb+" burritos")

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
