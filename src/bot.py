from extends import calcular, verificar_expressao
from my_token import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda mensagem : verificar_expressao(mensagem.text))
def responder_expressao(mensagem):
    
    resposta = calcular(mensagem.text)

    bot.reply_to(mensagem, resposta)

@bot.message_handler(func=lambda mensagem : not verificar_expressao(mensagem.text))
def responder_erro(mensagem):
    
    bot.reply_to(mensagem, 'ERRO! Verifique a expressão!')

bot.polling()
