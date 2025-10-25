from Crypto.Util.number import isPrime, bytes_to_long
import random
import os

FLAG = os.getenv("FLAG", "vgucypher{fake_flag}")

class Broadcast:
    def __init__(self):
        self.e = 3

    def getWYSIprime(self):
        # osu!gaming CTF 2024
        while True:
            digits = [random.choice("727") for _ in range(272)]
            prime = int("".join(digits))
            if isPrime(prime):
                return prime

    def encrypt(self, msg: bytes):
        p = self.getWYSIprime()
        q = self.getWYSIprime()
        while p == q:
            q = self.getWYSIprime()
        
        n = p * q
        cypher = pow(bytes_to_long(msg), self.e, n)
        return cypher, n

def handle_client():
    channel = Broadcast()
    print("Welcome to the witch's loudspeaker in the jungle!", flush=True)
    print("What do you want to hear from loudspeaker?")
    running = True
    while running:
        menu = (
            "1. Use magic on your talk!\n"
            "2. Get special witch spellcast!\n"
            "3. Leave\n"
            "Enter number: "
        )
        print(menu, end="", flush=True)
        
        try:
            usr_inp = input().strip()
            if usr_inp == "1":
                print("Your message: ", end="", flush=True)
                msg_inp = input().strip()
                if len(msg_inp) >= 1:
                    c, n = channel.encrypt(msg_inp.encode())
                    print(f"Your message after being fused with spell: {c}")
                    print(f"The spell name: {n}", flush=True)
                else:
                    print(f"Oops, something wrong with this?", flush = True)
            elif usr_inp == "2":
                c, n = channel.encrypt(FLAG.encode())
                print(f"The witch's secret message but been fused with special spell: {c}")
                print(f"The spell name: {n}", flush=True)
            else:
                print("Thank for joining, did you know osu! is a free-to-play rhythm game?", flush=True)
                running = False
        except EOFError:
            running = False

if __name__ == "__main__":
    handle_client()
    exit()