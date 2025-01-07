This project is an amateur implementation of an invoice and receipt recognition system, created purely for recreational purposes to test my skills in Python. The application uses Google Cloud Vision and OpenAI’s GPT-4. It was developed in 4 hours as a quick test and might contain some errors.

The system enables users to upload images of receipts or invoices, which are processed to extract key data such as:
	1.	Amount Spent (in €),
	2.	Purchase Date (printed on the receipt/invoice),
	3.	Expense Category (e.g., Rent, Groceries, Travel, etc.).

Key Features:
	•	Image Upload and Processing: Users can upload receipt or invoice images in PNG, JPG, or JPEG formats.
	•	Text Recognition: Google Cloud Vision API extracts text from uploaded images.
	•	AI-Based Categorization: OpenAI GPT-4 classifies the extracted data into predefined categories.
	•	Dynamic Expense Classification: Includes web-based search for invoice sender details to accurately assign categories.
	•	Clean and Secure: Automatically deletes uploaded files after processing.

Note: This is a basic project made in a limited time frame and is not intended for production use.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Questo progetto è un’implementazione amatoriale di un sistema di riconoscimento di scontrini e fatture, creato esclusivamente per scopi ricreativi e per testare le mie capacità in Python. L’applicazione utilizza Google Cloud Vision e OpenAI GPT-4. È stata sviluppata in sole 4 ore come prova e potrebbe contenere degli errori.

Il sistema permette agli utenti di caricare immagini di scontrini o fatture, che vengono processate per estrarre dati chiave come:
	1.	Importo Speso (in €),
	2.	Data di Acquisto (stampata sullo scontrino/fattura),
	3.	Categoria di Spesa (es. Affitto, Alimentari, Viaggi, ecc.).

Funzionalità Principali:
	•	Caricamento e Elaborazione Immagini: Supporta immagini in formato PNG, JPG o JPEG.
	•	Riconoscimento Testo: L’API Google Cloud Vision estrae il testo dalle immagini caricate.
	•	Classificazione AI: OpenAI GPT-4 classifica i dati estratti in categorie predefinite.
	•	Classificazione Dinamica: Effettua ricerche online sul mittente per fatture, garantendo una categorizzazione precisa.
	•	Pulizia e Sicurezza: I file caricati vengono automaticamente eliminati dopo l’elaborazione.

Nota: Si tratta di un progetto base, sviluppato in un tempo limitato e non destinato ad un utilizzo in produzione.
