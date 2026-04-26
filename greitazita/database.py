def save_chat_message(self, salon_id: int, user_message: str, ai_response: str):
    """Išsaugo vartotojo žinutę ir AI atsakymą į MySQL"""
    try:
        with self._get_session() as session:
            record = ChatMessage(
                salon_id=salon_id,
                user_message=user_message,
                ai_response=ai_response
            )
            session.add(record)
            session.commit()
            print(f"✅ Išsaugota į DB: salon_id={salon_id}")
    except Exception as e:
        print(f"❌ DB klaida: {e}")
