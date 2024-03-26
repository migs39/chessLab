import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

hostname = 'Souza 2.4ghz'
topic = 'esp8266/test'

def msgOut(content):
    publish.single(topic, content, hostname = hostname)


def msgIn():
    msg = subscribe.simple(topic, hostname = hostname)
    return msg.payload

def sqrIn(): #Recebe 2 int de 1 a 8 e converte em uma string de 'a1' a 'h8'
    collumn = msgIn()
    line = msgIn()
    collumns = 'abcdefgh'
    return collumns[collumn-1] + str(line)

def sqrOut(sq):
    line = int(sq[1])
    collumns = 'abcdefgh'
    collumn = collumns.index(sq[0]) + 1
    msgOut(collumn)
    msgOut(line)
