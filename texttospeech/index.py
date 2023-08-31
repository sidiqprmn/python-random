import speech_recognition as sr
import webbrowser
from datetime import datetime

def get_current_date():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def listen_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Katakan sesuatu...")
        audio_data = recognizer.listen(source)
    return audio_data

def recognize_and_search():
    recognizer = sr.Recognizer()
    try:
        audio_data = listen_microphone()
        text = recognizer.recognize_google(audio_data, language="id-ID")
        print("Anda mengatakan: " + text)

        # Mendapatkan format tanggal saat ini
        current_date = get_current_date()

        # Menyimpan hasil teks beserta tanggal ke dalam file teks
        with open("hasil_input_suara.txt", "a") as file:
            file.write(f"{current_date}: {text}\n")

        # Memisahkan perintah "cari..." atau "carikan..." dari kata kunci pencarian
        if "carikan" in text.lower() or "search" in text.lower():
            keyword = ""
            if "carikan" in text.lower():
                keyword = "carikan"
            elif "search" in text.lower():
                keyword = "search"

            search_query = text.lower().split(keyword, 1)[-1].strip()
            if search_query:
                # Mencari sesuatu dengan Google menggunakan Chrome
                search_url = "https://www.google.com/search?q="
                encoded_query = search_query.replace(" ", "+")
                full_url = search_url + encoded_query
                webbrowser.get("opera").open(full_url)
                print(f"Mencari '{search_query}' di Google menggunakan opera...")

    except sr.UnknownValueError:
        print("Maaf, tidak dapat mengenali suara Anda.")
    except sr.RequestError as e:
        print("Terjadi kesalahan pada layanan penerjemahan suara; {0}".format(e))

# Fungsi main untuk menjalankan skrip
def main():
    recognize_and_search()

if __name__ == "__main__":
    main()
