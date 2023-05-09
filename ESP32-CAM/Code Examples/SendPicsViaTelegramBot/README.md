# Send Pictures Via Telegram Bot
This code is for an ESP32-CAM that connects to a Telegram bot and takes pictures, sends them to the bot and interacts with it through commands. It uses the UniversalTelegramBot library, the ESP32-CAM library, and the ArduinoJson library.

The code defines the ssid and password of the Wi-Fi network, as well as the Telegram BOTtoken and CHAT_ID of the chat the bot will use.

It also initializes the camera with its pins, frequency, and quality. The function handleNewMessages receives any new messages from the Telegram bot, checks if the user is authorized, and then performs the corresponding action according to the received command. 

The `/photo` command takes a new photo and sends it to the user, while the `/flash` command toggles the state of the flash LED.

# Changes that Required:

`const char* ssid = "WIFI_NETWORK";` <br>
`const char* password = "WIFI_PASS";` <br>

Change ssid to your WIFI Network
Change pass to your network password

#### Genarate Telegram Bot

Open Telegran and search for `BotFather`
Type `/start` and send. Then, type `/newbot` and send. Choose a valid name for the bot.

![image](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/76903853/feb4cac3-7e7a-42b9-81d0-040caa67ba44)

`String BOTtoken = "XXXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";` // your Bot Token (Get from Botfather)

Now, copy the TOKEN from the message above.

#### Get Chat ID

Open Telegram and search for `IDBot`
Type `/getid` and send.
copy the Code that you got, and paste below.

`String CHAT_ID = "XXXXXXXXXX";` // Use @myidbot to find out the chat ID of an individual or a group

# How To RUN:

#### Click on this button for compiling the code:  <br>
![image](https://user-images.githubusercontent.com/76903853/236200840-fb242ca4-5ba9-4a60-b0c9-c165ff2ba3b9.png)

#### After the compiling ends, It should look like this on the output: <br>
![image](https://user-images.githubusercontent.com/76903853/236426487-aeec3cf7-5e4e-4b1d-9fb7-75d3e2d3b64d.png)

#### Open Serial Monitor, by click this button: <br>
![image](https://user-images.githubusercontent.com/76903853/236426240-da57971c-684e-4442-b519-90536e79bc6d.png)

#### Click on Reset Button: <br>
![image](https://user-images.githubusercontent.com/76903853/236427674-db04422e-c951-467c-84fc-641df776c93b.png)

#### Now, You should see this command on the Serial Monitor:
![image](https://github.com/bargoldenberg/New_Space_EDU_SATALLITE/assets/76903853/71428463-d1d9-479e-bd6f-a0321c59371c)

#### Make sure your device connected to the same Network with the Board.
Go to your Telegram account and open a conversation with your bot. Send the following commands and see the bot responding:

`/start` shows the welcome message with the valid commands.
`/flash` inverts the state of the LED flash.
`/photo` takes a new photo and sends it to your Telegram account.

#### Press on Strat Stream
![image](https://user-images.githubusercontent.com/76903853/236431559-48110ba3-eb25-4520-9916-36ab9d624e00.png)

![image](https://user-images.githubusercontent.com/76903853/236431974-2ee14caa-7fb5-44fe-8f21-c6c3c9ff7eaa.png)

#### You can Play with all the features, such as Face Recognition, The image Resolution, etc...
### Enjoy!
