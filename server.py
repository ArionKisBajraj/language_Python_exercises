import socket
import sys

def gestisci_cliente(client_socket):
    dati = client_socket.recv(1024).decode('utf-8')
    stringa_da_modificare, carattere_da_rimuovere = dati.split(',')

    risultato_stringa = stringa_da_modificare.replace(carattere_da_rimuovere, '')

    client_socket.send(risultato_stringa.encode('utf-8'))
    client_socket.close()

def avvia_server(indirizzo, porta):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((indirizzo, porta))
    server.listen(5)
    print(f"[*] In ascolto su {indirizzo}:{porta}")

    while True:
        client, addr = server.accept()
        print(f"[*] Connessione accettata da {addr[0]}:{addr[1]}")
        gestisci_cliente(client)

if len(sys.argv) != 3:
    print("Utilizzo: python3 server.py <indirizzo-server> <porta>")
    sys.exit(1)

indirizzo_server = sys.argv[1]
porta_server = int(sys.argv[2])
avvia_server(indirizzo_server, porta_server)
