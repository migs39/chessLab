#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// WiFi
const char *ssid = "Souza 2.4ghz"; // Enter your WiFi name
const char *password = "elicris10";  // Enter WiFi password

// MQTT Broker
const char *mqtt_broker = "Souza 2.4ghz";
const char *topic = "esp8266/test";
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
const int geradaColuna0  = 1;    
const int geradaColuna1 =  2;  
const int geradaColuna2 =  3; 
const int geradaFileira0  = 4; 
const int geradaFileira1  = 5;     
const int geradaFileira2  = 6; 
const int subirJogada  = 7;
const int acertoujogada  = 16;

// output pins
const int jogadaColuna0  = 8;    
const int jogadaColuna1 =  9;  
const int jogadaColuna2 =  10; 
const int jogadaFileira0  = 11; 
const int jogadaFileira1  = 12;     
const int jogadaFileira2  = 13; 
const int inicar  = 14;    
const int fim  = 15;

WiFiClient espClient;
PubSubClient client(espClient);

void setup(void) {
  // Set software serial baud to 115200;
  Serial.begin(115200);
  // connecting to a WiFi network
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
  //connecting to a mqtt broker
  byte attempt = 0;
  client.setServer(mqtt_broker, mqtt_port);
  client.setCallback(callback);

  while (!client.connected() && attempt < 5) {
      String client_id = "esp8266-client-";
      client_id += String(WiFi.macAddress());
      Serial.printf("The client %s connects to the public mqtt broker\n", client_id.c_str());
      if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) {
          Serial.println("Public emqx mqtt broker connected");
      } else {
          Serial.print("failed with state ");
          Serial.print(client.state());
          delay(2000);
      }
      attempt++;
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



  // publish and subscribe
  if (attempt < 5) {
    client.publish(topic, "hello emqx");
    client.subscribe(topic);
    mqttConnected = 1;
  } else {
    Serial.print("failed to connect ");
    mqttConnected = 0;
  }
  
}

void callback(char *topic, byte *payload, unsigned int length) {
    Serial.print("Message arrived in topic: ");
    Serial.print(topic);
    Serial.print("Message: ");
    for(int i = 0; i < length; i++) {
      Serial.print((char) payload[i]);
      valuecbyte = payload[i];
      if (i == 0) {
        valuecbyte = valuecbyte - 1;
        if (valuecbyte == 0) {
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
      } else if (i == 1) {
        valuecbyte = valuecbyte - 1;
        if (valuecbyte == 1) {
          digitalWrite(inicar, HIGH);
          i = length;
        } else if (valuecbyte == 2) {
          digitalWrite(fim, HIGH);
          i = length;
        }
      }
      
    }
    Serial.println("---------------------------------");
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
      acertou = 1;
    } else {
      acertou = 0;
    }
    test[0] = acertou; // Assign the character to the array
    client.publish(topic, test);
    client.loop();
  }
}