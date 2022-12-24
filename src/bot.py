from extends import calcular, verificar_expressao
from my_token import TOKEN
from time import ctime, time
import telebot

log = open(f'log{int(time())}.txt', 'w')

bot = telebot.TeleBot(TOKEN)

bot.calculadora_ativada = False

def qualquer_mensagem(mensagem):
    print(f"{mensagem.chat.first_name} {mensagem.chat.last_name} : ({ctime(mensagem.date)}) : {mensagem.text}", file=log)
    return True

@bot.message_handler(commands=['ativar'])
def ativar_calculadora(mensagem):

    print(f"{mensagem.chat.first_name} {mensagem.chat.last_name} : ({ctime(mensagem.date)}) : {mensagem.text}", file=log)

    if bot.calculadora_ativada:
        bot.reply_to(mensagem, 'Calculadora já ativada')
    else:
        bot.calculadora_ativada = True
        bot.reply_to(mensagem, 'Ativando calculadora...')

@bot.message_handler(commands=['desativar'])
def desativar_calculadora(mensagem):

    print(f"{mensagem.chat.first_name} {mensagem.chat.last_name} : ({ctime(mensagem.date)}) : {mensagem.text}", file=log)

    if not bot.calculadora_ativada:
        bot.reply_to(mensagem, 'Calculadora já desativada')
    else:
        bot.calculadora_ativada = False
        bot.reply_to(mensagem, 'Desativando calculadora...')

@bot.message_handler(func=lambda mensagem : qualquer_mensagem(mensagem) and not bot.calculadora_ativada)
def instruir_usuario(mensagem):

    texto = """
    Mensagem não identificada, verificar a tabela de comandos.
    /ativar - Para ativar a calculadora.
    /desativar - Para desativar a calculadora.
    """

    bot.reply_to(mensagem, texto)

@bot.message_handler(func=lambda mensagem : verificar_expressao(mensagem.text) and bot.calculadora_ativada)
def responder_expressao(mensagem):
    
    resposta = str(calcular(mensagem.text))

    bot.reply_to(mensagem, resposta)

@bot.message_handler(func=lambda mensagem : not verificar_expressao(mensagem.text) and bot.calculadora_ativada)
def responder_erro(mensagem):
    
    bot.reply_to(mensagem, 'ERRO! Verifique a expressão!')

bot.polling()

log.close()