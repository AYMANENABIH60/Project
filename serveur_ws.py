import asyncio
import websockets

# 1) Fonction appelée à chaque connexion d'un client WebSocket
async def handler(websocket):
    print("[+] Nouveau client connecté")
    # Boucle qui écoute les messages du client
    async for message in websocket:
        # Afficher le message recu
        print(f"Message reçu du client : {message}")

# 2) Fonction pour démarrer et maintenir le serveur WebSocket
async def main():
    # création du serveur WebSocket
    server = await websockets.serve(handler, "0.0.0.0", 8765)
    print("[OK] Serveur WebSocket démarré sur 0.0.0.0:8765")
    print("En attente de connexions...")

# 3) Démarrage du serveur en utilisant la boucle asyncio
# Cette condition là evite lancement du code par erreur 
# lorsqu'on réutilises le script
if __name__== "__main__":
    # Créer une nouvelle boucle d'événements asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # Démarrer le serveur WebSocket
    loop.run_until_complete(main())
    # Garder la boucle en vie
    loop.run_forever()
