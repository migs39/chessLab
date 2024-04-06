import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

hostname = '192.168.137.45'
topic = 'emqx/esp32'

def msgOut(content):
    publish.single(topic, content, hostname = hostname)


def msgIn():
    msg = subscribe.simple(topic, hostname = hostname)
    a = msg.payload
    print(a)
    return (a.decode('utf-8'))

def sqrIn(): #Recebe 2 int de 1 a 8 e converte em uma string de 'a1' a 'h8'
    collumn = msgIn()
    line = msgIn()
    collumns = 'abcdefgh'
    return collumns[int(collumn)-1] + str(line)

def sqrOut(sq):
    line = int(sq[1])
    collumns = 'abcdefgh'
    collumn = collumns.index(sq[0]) + 1
    msg = str(collumn) + str(line) + '1'
    msgOut(msg)

def test():
    msgOut('papos')
    a = msgIn()
    print(a)
    print(type(a))


if __name__ == '__main__' and False:
    test()