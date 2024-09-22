import paho.mqtt.client as mqtt

def ao_conectar(client, userdata, flags, rc):
    print("Nos conectamos com o seguinte código de resultado {}".format(str(rc)))

def ao_receber(client, userdata, msg):
    print("{} --- {}".format(msg.topic, str(msg.payload)))
    if "DESLIGAR" in str(msg.payload).upper():
        print("DESLIGANDO O SISTEMA")
cliente = mqtt.Client()

cliente.on_connect = ao_conectar
cliente.on_message = ao_receber
cliente.connect("broker.hivemq.com", 1883, 60)
cliente.subscribe("aula3b")
#cliente.loop_forever()

cliente.loop_start()
while True:
    cliente.publish("aula3b", input("Envie uma mensagem"))
cliente.loop_finish()
