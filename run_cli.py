from greitazita.ai import GreitaZitaAI
from greitazita.database import DatabaseManager
from greitazita.file_export import FinanceFileManager

def main():
    print("🚀 GreitaZita CLI - AI Finance Tracker for Beauty Salons")
    print("Type your 3-month expenses/earnings (e.g., 'Rent 1200, Haircut 5000')\n")
    
    db = DatabaseManager()
    ai = GreitaZitaAI()
    file_mgr = FinanceFileManager()
    salon_id = 1

    while True:
        message = input("\n💬 Client message (or 'exit'): ")
        if message.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break
        
        response = ai.process_message(salon_id, message)
        print("\n" + response)
        
        # Optional: export to CSV as well
        # file_mgr.export_to_csv([], "backup.csv")

if __name__ == "__main__":
    main()
