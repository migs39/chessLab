#include <WiFi.h>
#include <PubSubClient.h>

// WiFi
const char *ssid = "DESKTOP-D670JL6 5351"; // Enter your Wi-Fi name
const char *password = "senha.00";  // Enter Wi-Fi password

// MQTT Broker
const char *mqtt_broker = "192.168.137.95";
const char *topic = "emqx/esp32";
const char *mqtt_username = "";
const char *mqtt_password = "";
const int mqtt_port = 1883;


// variaveis
bool mqttConnected =0;
int buttonState = 0;
byte geradaColuna = 1;
byte geradaFileira = 1;
bool acertou = 0;
byte valuecbyte = 0;
char test[2]; // Character array to hold the test


// input pins
const int geradaColuna0  = 20;    
const int geradaColuna1 =  18;  
const int geradaColuna2 =  17; 
const int geradaFileira0  = 16; 
const int geradaFileira1  = 15;     
const int geradaFileira2  = 14; 
const int subirJogada  = 13;
const int acertoujogada  = 12;

// output pins
const int jogadaColuna0  = 21;    
const int jogadaColuna1 =  22;  
const int jogadaColuna2 =  24; 
const int jogadaFileira0  = 25; 
const int jogadaFileira1  = 27;     
const int jogadaFileira2  = 41; 
const int inicar  = 39;    
const int fim  = 36;

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
    // Set software serial baud to 115200;
    Serial.begin(115200);
    // Connecting to a WiFi network
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.println("Connecting to WiFi..");
    }
    Serial.println("Connected to the Wi-Fi network");
    //connecting to a mqtt broker
    client.setServer(mqtt_broker, mqtt_port);
    client.setCallback(callback);
    while (!client.connected()) {
        String client_id = "esp32-client-";
        client_id += String(WiFi.macAddress());
        Serial.printf("The client %s connects to the public MQTT broker\n", client_id.c_str());
        if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) {
            Serial.println("Public EMQX MQTT broker connected");
            mqttConnected = 1;
        } else {
            Serial.print("failed with state ");
            Serial.print(client.state());
            delay(2000);
            mqttConnected = 0;
        }
    }
    // initialize the pushbutton pin as an input
    pinMode(geradaColuna0, INPUT);
    pinMode(geradaColuna1, INPUT);
    pinMode(geradaColuna2, INPUT);
    pinMode(geradaFileira0, INPUT);
    pinMode(geradaFileira1, INPUT);
    pinMode(geradaFileira2, INPUT);
    pinMode(subirJogada, INPUT);
    pinMode(acertoujogada, INPUT);


    // initialize the LED pin as an output
    pinMode(jogadaColuna0, OUTPUT);
    pinMode(jogadaColuna1, OUTPUT);
    pinMode(jogadaColuna2, OUTPUT);
    pinMode(jogadaFileira0, OUTPUT);
    pinMode(jogadaFileira1, OUTPUT);
    pinMode(jogadaFileira2, OUTPUT);
    pinMode(inicar, OUTPUT);
    pinMode(fim, OUTPUT);
    delay(500);
    
    // Publish and subscribe
    client.publish(topic, "Hi, I'm ESP32 ^^");
    client.subscribe(topic);
}

void callback(char *topic, byte *payload, unsigned int length) {
    Serial.print("Message arrived in topic: ");
    Serial.println(topic);
    Serial.print("Message:");
    for(int i = 0; i < length; i++) {
      Serial.print((char) payload[i]);
      valuecbyte = payload[i];
      if (i == 0) {
        if (valuecbyte == 1) {
          digitalWrite(inicar, HIGH);
        } else if (valuecbyte == 2) {
          digitalWrite(fim, HIGH);
          i = length;
        }
      } else if (i == 0) {
        valuecbyte = valuecbyte - 1;
        if (valuecbyte == 1) {
          digitalWrite(jogadaFileira0, LOW);
          digitalWrite(jogadaFileira1, LOW);
          digitalWrite(jogadaFileira2, LOW);
        } else if (valuecbyte == 1) {
          digitalWrite(jogadaFileira0, HIGH);
          digitalWrite(jogadaFileira1, LOW);
          digitalWrite(jogadaFileira2, LOW);
        } else if (valuecbyte == 2) {
          digitalWrite(jogadaFileira0, LOW);
          digitalWrite(jogadaFileira1, HIGH);
          digitalWrite(jogadaFileira2, LOW);
        } else if (valuecbyte == 3) {
          digitalWrite(jogadaFileira0, HIGH);
          digitalWrite(jogadaFileira1, HIGH);
          digitalWrite(jogadaFileira2, LOW);
        } else if (valuecbyte == 4) {
          digitalWrite(jogadaFileira0, LOW);
          digitalWrite(jogadaFileira1, LOW);
          digitalWrite(jogadaFileira2, HIGH);
        } else if (valuecbyte == 5) {
          digitalWrite(jogadaFileira0, HIGH);
          digitalWrite(jogadaFileira1, LOW);
          digitalWrite(jogadaFileira2, HIGH);
        } else if (valuecbyte == 6) {
          digitalWrite(jogadaFileira0, LOW);
          digitalWrite(jogadaFileira1, HIGH);
          digitalWrite(jogadaFileira2, HIGH);
        } else if (valuecbyte == 7) {
          digitalWrite(jogadaFileira0, HIGH);
          digitalWrite(jogadaFileira1, HIGH);
          digitalWrite(jogadaFileira2, HIGH);
        }
      } else if (i == 2) {
        valuecbyte = valuecbyte - 1;
        if (valuecbyte == 0) {
          digitalWrite(jogadaColuna0, LOW);
          digitalWrite(jogadaColuna1, LOW);
          digitalWrite(jogadaColuna2, LOW);
        } else if (valuecbyte == 1) {
          digitalWrite(jogadaColuna0, HIGH);
          digitalWrite(jogadaColuna1, LOW);
          digitalWrite(jogadaColuna2, LOW);
        } else if (valuecbyte == 2) {
          digitalWrite(jogadaColuna0, LOW);
          digitalWrite(jogadaColuna1, HIGH);
          digitalWrite(jogadaColuna2, LOW);
        } else if (valuecbyte == 3) {
          digitalWrite(jogadaColuna0, HIGH);
          digitalWrite(jogadaColuna1, HIGH);
          digitalWrite(jogadaColuna2, LOW);
        } else if (valuecbyte == 4) {
          digitalWrite(jogadaColuna0, LOW);
          digitalWrite(jogadaColuna1, LOW);
          digitalWrite(jogadaColuna2, HIGH);
        } else if (valuecbyte == 5) {
          digitalWrite(jogadaColuna0, HIGH);
          digitalWrite(jogadaColuna1, LOW);
          digitalWrite(jogadaColuna2, HIGH);
        } else if (valuecbyte == 6) {
          digitalWrite(jogadaColuna0, LOW);
          digitalWrite(jogadaColuna1, HIGH);
          digitalWrite(jogadaColuna2, HIGH);
        } else if (valuecbyte == 7) {
          digitalWrite(jogadaColuna0, HIGH);
          digitalWrite(jogadaColuna1, HIGH);
          digitalWrite(jogadaColuna2, HIGH);
        }
      }
    Serial.println();
    Serial.println("-----------------------");
    }
  digitalWrite(inicar, LOW);
  digitalWrite(fim, LOW);
}


void loop() {
  if (mqttConnected) {
    test[1] = '\0'; // Null-terminate the string
    buttonState = digitalRead(subirJogada);
    if (buttonState == HIGH) {
      buttonState = digitalRead(geradaColuna0);
      if (buttonState == HIGH) {
        geradaColuna = geradaColuna + 1;
      }
      buttonState = digitalRead(geradaColuna1);
      if (buttonState == HIGH) {
        geradaColuna = geradaColuna + 2;
      }     
      buttonState = digitalRead(geradaColuna2);
      if (buttonState == HIGH) {
        geradaColuna = geradaColuna + 4;
      }
      buttonState = digitalRead(geradaFileira0);
      if (buttonState == HIGH) {
        geradaFileira = geradaFileira + 1;
      } 
      buttonState = digitalRead(geradaFileira1);
      if (buttonState == HIGH) {
          geradaFileira = geradaFileira + 2;
      } 
      buttonState = digitalRead(geradaFileira2);
      if (buttonState == HIGH) {
          geradaFileira = geradaFileira + 4;
      } 
      test[0] = geradaColuna; // Assign the character to the array
      client.publish(topic, test);
      test[0] = geradaFileira; // Assign the character to the array
      client.publish(topic, test);
      geradaColuna = 1;
      geradaFileira = 1;
    }
    buttonState = digitalRead(acertoujogada);
    if (buttonState == HIGH) {
      acertou = 0;
    } else {
      acertou = 1;
    }
    test[0] = acertou; // Assign the character to the array
    client.publish(topic, test);
  }
    client.loop();
}
