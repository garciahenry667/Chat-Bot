import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?-_]\s*', user_input)
    response = check_all_message(split_message)
    return response

def message_probability(user_message, reconized_words, single_response=False, required_word=[]):
    message_certainy = 0
    has_requird_words = True

    for word in user_message:
        if word in reconized_words:
            message_certainy +=1

    percentage = float(message_certainy) / float (len(reconized_words))

    for word in required_word:
        if word not in user_message:
            has_requird_words = False
            break
    if has_requird_words or single_response:
        return int(percentage * 100)
    else:
        return 0
    
    def check_all_message(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response,  required_word)
        response('Hola', ['hola',  'klk', 'saludos', 'buenas'], single_response = True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_word=['como'])
        response('Estamos ubicados en la calle konoha de la tierra del fuego en la torre hokague', ['ubicados', 'direccion', 'donde', 'ubicacion', ], single_response=True)
        response('Siempre a la orden', ['gracias','te lo agradezco', 'thanks'], single_response=True)

        best_mach = max(highest_prob,  key=highest_prob.get)
        print(highest_prob)

        return unknows() if highest_prob[best_mach] < 1 else best_mach
    
    def unknows():
        response(['Repita porfavor', 'Espere mientras se contactan con usted'], [random.randrage(2)])

while True:
    print('Bot: ' + get_response(input('You: ')))