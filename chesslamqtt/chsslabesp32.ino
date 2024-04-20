#include <WiFi.h>
#include <PubSubClient.h>

// WiFi
const char *ssid = "DESKTOP-D670JL6 0206"; // Enter your Wi-Fi name
const char *password = "senha.00";  // Enter Wi-Fi password

// MQTT Broker
const char *mqtt_broker = "192.168.137.45";
const char *topic = "emqx/esp32";
const char *mqtt_username = "";
const char *mqtt_password = "";
const int mqtt_port = 1883;


// variaveis
bool mqttConnected = 0;
int buttonState = 0;
int comecaAcerto = 0;
byte geradaColuna = 1;
byte geradaFileira = 1;
char acertou;
char valuecbyte = 0;
char test[2]; // Character array to hold the test

// input pins
#define geradaColuna0 13 //20;    
#define geradaColuna1 12 //18;  
#define geradaColuna2 14 //17; 
#define geradaFileira0  27 //16 
#define geradaFileira1  26 //15     
#define geradaFileira2  25 //14 
#define subirJogada  34 //13
#define acertoujogada  35 //12

// output pins
#define jogadaColuna0  15 //21    
#define jogadaColuna1  2 //22  
#define jogadaColuna2  4//24 
#define jogadaFileira0  16//25 
#define jogadaFileira1  17//27     
#define jogadaFileira2  5//34 
#define inicar  18//35    
#define fim  19//38

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
      valuecbyte = (char) payload[i];
      if (i == 2) {
        if (valuecbyte == '1') {
          
          Serial.print(valuecbyte);
          digitalWrite(inicar, HIGH);
        } else if (valuecbyte == '2') {
          digitalWrite(fim, HIGH);
          i = length;
          comecaAcerto = 0;
        }
      } else if (i == 1) {
        if (valuecbyte == '1') {
          digitalWrite(jogadaFileira0, LOW);
          digitalWrite(jogadaFileira1, LOW);
          digitalWrite(jogadaFileira2, LOW);
        } else if (valuecbyte == '2') {
          digitalWrite(jogadaFileira0, HIGH);
          digitalWrite(jogadaFileira1, LOW);
          digitalWrite(jogadaFileira2, LOW);
        } else if (valuecbyte == '3') {
          digitalWrite(jogadaFileira0, LOW);
          digitalWrite(jogadaFileira1, HIGH);
          digitalWrite(jogadaFileira2, LOW);
        } else if (valuecbyte == '4') {
          digitalWrite(jogadaFileira0, HIGH);
          digitalWrite(jogadaFileira1, HIGH);
          digitalWrite(jogadaFileira2, LOW);
        } else if (valuecbyte == '5') {
          digitalWrite(jogadaFileira0, LOW);
          digitalWrite(jogadaFileira1, LOW);
          digitalWrite(jogadaFileira2, HIGH);
        } else if (valuecbyte == '6') {
          digitalWrite(jogadaFileira0, HIGH);
          digitalWrite(jogadaFileira1, LOW);
          digitalWrite(jogadaFileira2, HIGH);
        } else if (valuecbyte == '7') {
          digitalWrite(jogadaFileira0, LOW);
          digitalWrite(jogadaFileira1, HIGH);
          digitalWrite(jogadaFileira2, HIGH);
        } else if (valuecbyte == '8') {
          digitalWrite(jogadaFileira0, HIGH);
          digitalWrite(jogadaFileira1, HIGH);
          digitalWrite(jogadaFileira2, HIGH);
        }
      } else if (i == 0) {
        if (valuecbyte == '1') {
          digitalWrite(jogadaColuna0, LOW);
          digitalWrite(jogadaColuna1, LOW);
          digitalWrite(jogadaColuna2, LOW);
        } else if (valuecbyte == '2') {
          digitalWrite(jogadaColuna0, HIGH);
          digitalWrite(jogadaColuna1, LOW);
          digitalWrite(jogadaColuna2, LOW);
        } else if (valuecbyte == '3') {
          digitalWrite(jogadaColuna0, LOW);
          digitalWrite(jogadaColuna1, HIGH);
          digitalWrite(jogadaColuna2, LOW);
        } else if (valuecbyte == '4') {
          digitalWrite(jogadaColuna0, HIGH);
          digitalWrite(jogadaColuna1, HIGH);
          digitalWrite(jogadaColuna2, LOW);
        } else if (valuecbyte == '5') {
          digitalWrite(jogadaColuna0, LOW);
          digitalWrite(jogadaColuna1, LOW);
          digitalWrite(jogadaColuna2, HIGH);
        } else if (valuecbyte == '6') {
          digitalWrite(jogadaColuna0, HIGH);
          digitalWrite(jogadaColuna1, LOW);
          digitalWrite(jogadaColuna2, HIGH);
        } else if (valuecbyte == '7') {
          digitalWrite(jogadaColuna0, LOW);
          digitalWrite(jogadaColuna1, HIGH);
          digitalWrite(jogadaColuna2, HIGH);
        } else if (valuecbyte == '8') {
          digitalWrite(jogadaColuna0, HIGH);
          digitalWrite(jogadaColuna1, HIGH);
          digitalWrite(jogadaColuna2, HIGH);
        }
      }
    Serial.println();
    Serial.println("-----------------------");
    }
  delay(1);
  digitalWrite(inicar, LOW);
  digitalWrite(fim, LOW);
}


void loop() {
  if (mqttConnected) {
    test[1] = '\0'; // Null-terminate the string
    buttonState = digitalRead(acertoujogada);
    if (buttonState == HIGH) {
      acertou = '0';
      test[0] = acertou; // Assign the character to the array
      client.publish(topic, test);
      delay(150);
    }
    buttonState = digitalRead(subirJogada);
    if (buttonState == HIGH) {
      if (comecaAcerto < 3) {
        comecaAcerto++;
      } else {
        acertou = '1';
        test[0] = acertou; // Assign the character to the array
        client.publish(topic, test);
        delay(150);
      }
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
      if (buttonState == HIGH)
 {
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
      char cGeradaColuna = geradaColuna + '0';
      test[0] = cGeradaColuna; // Assign the character to the array
      client.publish(topic, test);
      Serial.println("aqui");
      delay(150);
      char cGeradaFileira = geradaFileira + '0';
      test[0] = cGeradaFileira; // Assign the character to the array
      client.publish(topic, test);
      delay(150);
      geradaColuna = 1;
      geradaFileira = 1;
    } 
  }
    client.loop();
}