#include <WiFiS3.h>
#include <ArduinoJson.h>
#include <ctype.h>  // ← AJOUT CRITIQUE !

// WiFi
char ssid[] = "Ansumdine";
char pass[] = "1234567890";

// Serveur
WiFiServer server(80);

// Variables globales
float temp_s1 = 0, hum_s1 = 0, temp_s2 = 0, hum_s2 = 0;
int pir_s1 = 0, pir_s2 = 0;
float SEUIL_TEMP = 28.0;


void setup() {
  Serial.begin(115200);
  while (!Serial);

  Serial.println("=== SUPERVISEUR FINAL ===");
  
  IPAddress local_IP(10, 130, 13, 100);
  IPAddress gateway(10, 130, 13, 36);
  IPAddress subnet(255, 255, 255, 0);
  
  WiFi.config(local_IP, gateway, subnet);
  WiFi.begin(ssid, pass);
  
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 30) {
    delay(1000);
    Serial.print(".");
    attempts++;
  }
  
  Serial.println("\n✅ WiFi connecté");
  Serial.print("IP: "); Serial.println(WiFi.localIP());
  server.begin();
  Serial.println("Serveur HTTP 80 ✅");
}

void loop() {
  WiFiClient client = server.available();
  
  if (client) {
    Serial.println("\n--- ⚡ NOUVELLE CONNEXION DETECTEE ---");
    String currentLine = "";
    String requestLine = ""; 
    int contentLength = 0;
    bool isPost = false;

    // 1. LECTURE DES HEADERS
    unsigned long headerTimeout = millis();
    while (client.connected() && (millis() - headerTimeout < 2000)) {
      if (client.available()) {
        char c = client.read();
        if (requestLine == "") requestLine = currentLine; 
        
        if (c == '\n') {
          if (currentLine.length() == 0) break; // Fin des headers
          
          if (currentLine.startsWith("POST")) isPost = true;
          
          int clIdx = currentLine.indexOf("Content-Length:");
          if (clIdx == -1) clIdx = currentLine.indexOf("content-length:");
          if (clIdx != -1) {
            contentLength = currentLine.substring(clIdx + 15).toInt();
          }
          currentLine = "";
        } else if (c != '\r') {
          currentLine += c;
        }
      }
    }

    // 2. CAS DU POST (Réception des données des ESP)
    if (isPost && contentLength > 0) {
      Serial.print("📏 Content-Length detecte : "); Serial.println(contentLength);
      
      String body = "";
      unsigned long bodyTimeout = millis();
      // On attend que tout le JSON arrive
      while (body.length() < contentLength && (millis() - bodyTimeout < 2000)) {
        if (client.available()) {
          body += (char)client.read();
        }
      }
      
      Serial.print("📥 BODY RECU : "); Serial.println(body); 

      StaticJsonDocument<512> doc;
      DeserializationError error = deserializeJson(doc, body);
      
      if (!error) {
        String room = doc["room"];
        if (room == "salle1") {
          temp_s1 = doc["temperature"]; 
          hum_s1 = doc["humidity"]; 
          pir_s1 = doc["pir"];
        } else if (room == "salle2") {
          temp_s2 = doc["temperature"]; 
          hum_s2 = doc["humidity"]; 
          pir_s2 = doc["pir"];
        }
        Serial.print("✅ Donnees enregistrees pour : "); Serial.println(room);
        
        
      } else {
        Serial.print("❌ Erreur JSON : "); Serial.println(error.c_str());
      }
      
      // Reponse HTTP courte pour l'ESP
      client.println("HTTP/1.1 200 OK\r\nConnection: close\r\n\r\n");
    } 
    
    // 3. CAS DU GET (Interface du collegue ou navigateur)
    else {
      Serial.println("🌐 Envoi des donnees JSON au Front-end...");
      client.println("HTTP/1.1 200 OK");
      client.println("Content-Type: application/json");
      client.println("Access-Control-Allow-Origin: *"); 
      client.println("Connection: close");
      client.println();
      
      StaticJsonDocument<512> root;
      JsonObject s1 = root.createNestedObject("salle1");
      s1["temp"] = temp_s1; s1["hum"] = hum_s1; s1["pir"] = pir_s1;
      
      JsonObject s2 = root.createNestedObject("salle2");
      s2["temp"] = temp_s2; s2["hum"] = hum_s2; s2["pir"] = pir_s2;
      
      serializeJson(root, client);
    }
    
    delay(10);
    client.stop();
    Serial.println("--- 🏁 FIN DE TRANSACTION ---\n");
  }
}