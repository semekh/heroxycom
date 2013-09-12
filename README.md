heroxycom
=========
Heroxycom is yet another HTTP proxy, (currently) aiming to be easily deploy-able on Heroku free plans, thus providing an accessible solution everywhere.

Requirements
------------
Dependencies are listed in `requirements.txt`, do a `sudo pip install -r requirements.txt` and you should be good to go.

Getting started
---------------
1. Create a free app on Heroku.
2. Clone this repository and push it to your app
3. Edit `config.py` and replace your app name
4. Run `python client.py` on your local device
5. Point your browser to use `IP: 127.0.0.1, Port: 8080` as proxy
6. You have a free proxy in front of you. Happy surfing!

Demo
----
It is already deployed on `heroxycom.herokuapp.com`, please use it for testing purposes only.

TODO
----
* It currently supports HTTP only. Support for other protocols (HTTPS, FTP, SSH, SOCKS, Websocket, etc.) may be added whenever I get some spare time -- or dive in the code and pull-requests are more than welcome.
* It does not encrypt data, and may thus be tracked easily.

The name
--------
Author of the software, having hard days because of joint pain, decided to take a rest on the weekend. And what's going to happen when you're not working on *the* project, I'll work on *another* project! Hope this partly reliefs the pain of those behind firewalls, just like Piroxicam does.
