import socket
import sys

def send_commands(s, conn):
    """Prendi un comando dall'utente e invialo al Client."""
    print("\nCtrl + C per chiudere la connessione.")
    print("Naviga il sistema come al solito con cd.")
    print("\n")
    print("$: ", end="")
    while True:
        try:
            cmd = input()
            if len(cmd) > 0:
                conn.sendall(cmd.encode())
                data = conn.recv(64000)
                print(data.decode("windows-1252"), end="")
        except KeyboardInterrupt:
            print("\nA presto.")
            
            sys.exit()
        except Exception as e:
            print(e)
            print("$: ", end="")
                   
        
def server(address):
    """Inizializza un server socket e attendi una connessione."""
    try:
        s = socket.socket()
        s.bind(address)
        s.listen()
        print("Server Inizializzato. Sono in ascolto...")
    except Exception as e:
        print("\nSembra che qualcosa sia andato storto.")
        print(e)
        restart = input("\nVuoi che reinizializzi il server? s/n ")
        if restart.lower() == "s" or restart.lower() == "si":
            print("\nRicevuto. Sto reinizializzando il server...\n")
            server(address)
        else:
            print("\nA presto, ed Happy Coding! ;)\n")
            sys.exit()
    conn, client_addr = s.accept()
    print(f"Connessione Stabilita: {client_addr}")
    send_commands(s, conn)


while __name__ == "__main__":
    
    host = "192.168.1.10"
    port = 25565
    server((host, port))
