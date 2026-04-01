from greitazita.ai import GreitaZitaAI
from greitazita.database import DatabaseManager

def main():
    print("🚀 GreitaZita CLI - AI Finance Tracker for Beauty Salons")
    print("Type your 3-month expenses/earnings exactly as clients do on poesimus.lt\n")
    db = DatabaseManager()
    ai = GreitaZitaAI()
    salon_id = 1  # Demo salon (multiple salons supported)

    while True:
        message = input("\n💬 Client message (or 'exit'): ")
        if message.lower() in ['exit', 'quit']:
            print("👋 Goodbye! All messages saved to MySQL.")
            break
        response = ai.process_message(salon_id, message)
        print("\n" + response)

if __name__ == "__main__":
    main()
