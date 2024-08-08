# Nova-Voice-Assistant
This is a Python-based voice assistant project with a graphical user interface (GUI) built using the Tkinter library. The assistant can perform a variety of tasks, including opening desktop applications, playing music, searching on Google, and providing responses powered by the OpenAI API.

## Features
* User Authentication : Includes a secure login and registration system.
* Voice Interaction: Users can interact with the assistant through voice commands.
* Task Automation: The assistant can open desktop apps, play music, perform web searches, use openai to give answers, tell about news , cricket and other info.
* AI-Powered Responses: Integrated with OpenAI's API for accurate and context-aware responses.
* User-Friendly Interface: The UI is simple and intuitive, built using Tkinter.
# Installation
### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/voice-assistant.git
cd voice-assistant
```
### 2. Install the required dependencies:
Ensure you have Python 3.x installed, then install the necessary Python packages:

```bash

pip install -r requirements.txt
```
The `requirements.txt` file should include the necessary libraries, such as:

* tkinter
* SpeechRecognition
* pyttsx3
* openai
* Pillow (if using images in the UI)
* Any other dependencies your project might have.
### 3. Set up OpenAI API:
You need to set up an environment variable for your OpenAI API key. Create a .env file in the root directory and add your API key:

```bash
OPENAI_API_KEY=your_openai_api_key
```
## Usage
### 1.Run the application:


```bash
python main.py
```
### 2. Login or Register:
On startup, you'll be prompted to either log in or register. New users should register first.

### 3. Interact with the Assistant:
Once logged in, you'll reach the main page where you can start interacting with the assistant. Use voice commands to perform various tasks like opening apps, playing music, or asking questions.

## Screenshots
![Screenshot 2024-01-09 163513](https://github.com/user-attachments/assets/1782cace-c72b-4690-ba6a-7d4371006a68)
![Screenshot 2024-01-09 163531](https://github.com/user-attachments/assets/ef6a86bc-ad5b-496f-ba61-4e906e37bb30)
![Screenshot 2023-12-16 162721](https://github.com/user-attachments/assets/641f5d52-5767-467b-8f7d-0a91906d1a45)
![Screenshot 2023-12-16 170851](https://github.com/user-attachments/assets/b5e9ba87-4cb1-4b26-b0d6-7a1ad3140b73)
![Screenshot 2023-12-16 172526](https://github.com/user-attachments/assets/05894127-c73c-44d7-a401-a5c4de943f74)
![Screenshot 2023-12-16 174509](https://github.com/user-attachments/assets/ee1c0c7c-bd5c-4ef0-9e2f-9653b600daf9)
![Screenshot 2023-12-16 174702](https://github.com/user-attachments/assets/c291224d-66b8-47db-b9df-eaa58beb466a)
![Screenshot 2023-12-16 173229](https://github.com/user-attachments/assets/bce4575c-82e4-482a-aa94-59d97de668c1)
![Screenshot 2023-12-16 172039](https://github.com/user-attachments/assets/490ee3f7-d2a6-480f-bf07-710a489ef883)
![Screenshot 2023-12-16 172214](https://github.com/user-attachments/assets/de2b26d4-da7c-4cea-b01a-396cf2cd3c17)



Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
