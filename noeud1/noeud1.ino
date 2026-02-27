#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>
#include "DHT.h"
#include <WiFiClient.h>

// WiFi
#define WIFI_SSID "xxxxx"
#define WIFI_PASSWORD "xxxxxx"

// Serveur Arduino

#define SERVER_IP "10.130.13.100"  
String getServerUrl() {
  return "http://" + String(SERVER_IP) + ":80/";
}


// Capteurs
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

#define PIR_PIN 14

void setup() {
  Serial.begin(115200);
  pinMode(PIR_PIN, INPUT);
  dht.begin();

  Serial.println("Connexion au WiFi...");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connecté !");
  Serial.print("Adresse IP : ");
  Serial.println(WiFi.localIP());
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  int pir = digitalRead(PIR_PIN);

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Erreur DHT11");
    return;
  }

  StaticJsonDocument<256> doc;
  doc["room"] = "salle1";
  doc["temperature"] = temperature;
  doc["humidity"] = humidity;
  doc["pir"] = pir;
  doc["timestamp"] = millis();

  String json;
  serializeJson(doc, json);

  Serial.println("----- Données envoyées (Salle 1) -----");
  Serial.print("Température : "); Serial.println(temperature);
  Serial.print("Humidité    : "); Serial.println(humidity);
  Serial.print("PIR         : "); Serial.println(pir);
  Serial.print("JSON        : "); Serial.println(json);
  Serial.println("--------------------------------------");

  // Test de connectivité avant envoi
if (WiFi.status() == WL_CONNECTED) {
  Serial.print("Test ping superviseur : ");
  Serial.println(WiFi.localIP());  // Vérifiez que c'est la bonne IP
} else {
  Serial.println(" WiFi déconnecté !");
  return;
}

  if (WiFi.status() == WL_CONNECTED) {
    WiFiClient client;  
    HTTPClient http;
    http.begin(client, getServerUrl());   
    http.addHeader("Content-Type", "application/json");
    int code = http.POST(json);
    Serial.print("Réponse HTTP : ");
    Serial.println(code);
    http.end();
}


  delay(5000);
}
