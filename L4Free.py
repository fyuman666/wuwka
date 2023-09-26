import argparse
import random
import socket
import threading
import telebot
from telebot import types

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", type=str, help="Host ip")
ap.add_argument("-p", "--port", type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=50000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
args = vars(ap.parse_args())

ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

bot = telebot.TeleBot("6349839287:AAHdwQbGVdUIaBhZA9dK153X4BdABNnaUmk")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn_udp = types.KeyboardButton('UDP Flood')
    btn_tcp = types.KeyboardButton('TCP Flood')
    markup.add(btn_udp, btn_tcp)
    bot.send_message(message.chat.id, "Выберите тип атаки:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def process_message(message):
    if message.text == 'UDP Flood':
        bot.send_message(message.chat.id, "Введите IP адрес:")
        bot.register_next_step_handler(message, get_ip_udp)
    elif message.text == 'TCP Flood':
        bot.send_message(message.chat.id, "Введите IP адрес:")
        bot.register_next_step_handler(message, get_ip_tcp)
    else:
        bot.send_message(message.chat.id, "Некорректная команда! Пожалуйста, выберите тип атаки.")

def get_ip_udp(message):
    global ip
    ip = message.text
    bot.send_message(message.chat.id, "Введите порт:")
    bot.register_next_step_handler(message, get_port_udp)

def get_port_udp(message):
    global port
    port = int(message.text)
    run_threaded_attack('udp')
    bot.send_message(message.chat.id, "DDoS атака началась!")

def get_ip_tcp(message):
    global ip
    ip = message.text
    bot.send_message(message.chat.id, "Введите порт:")
    bot.register_next_step_handler(message, get_port_tcp)

def get_port_tcp(message):
    global port
    port = int(message.text)
    run_threaded_attack('tcp')
    bot.send_message(message.chat.id, "DDoS атака началась!")

def run_udp_attack():
    # Остальной код атаки UDP

def run_tcp_attack():
    # Остальной код атаки TCP

def run_threaded_attack(attack_type):
    # Остальной код запуска атаки

bot.polling()
