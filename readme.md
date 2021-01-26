# CS:GO Trask Talker

Basically just a python script to automatically compile a config file for all your trash talking needs. Also includes a nice set of trash talk lines for you to use wherever you want.

Simply replace `BIND_KEY` with the key you want to use and add your desired messages in the `trashtalk.txt` file. The program will output a config file that you can use to spam the chat all you need. The bind will loop through each line and send it as a message in game.

*Note: This particular script will also create bindings for built different messages based on the lines in `builtdiff.txt`*

## Usage in CSGO

To actually use the config file, you can either copy and paste its contents to an autoexec. Check out [this guide](https://steamcommunity.com/sharedfiles/filedetails/?l=english&id=257041519) for more information about this. Alternatively you can just move the output config file into your `csgo/cfg` folder and then run the following command in the developer console: `exec trashtalk`