# Deploying a simple pyrus bot to heroku

* Create a Pyrus bot on the [bots page](https://pyrus.com/t#bots) (if you already have one to access the Pyrus API, you can use it).
* Clone the initial bot application from github and go to its folder:
~~~sh
$ git clone https://github.com/simplygoodsoftware/heroku-python-bot.git
$ cd heroku-python-bot
~~~
* Specify bot's security key in the config file config.json
~~~json
{
    "SECRET_KEY": "Your-Bot-Secret-Key"
}
~~~
* Create and run a Heroku application:
~~~sh
$ heroku create
$ git add .
$ git commit -m "replaced SECRET_KEY in config.json"
$ git push heroku master
$ heroku ps:scale web=1
~~~
* Specify the received on the previous step URL in the Pyrus bot settings.
* Create a task in Pyrus and assign it to the bot. You should see the comment with the bot's response on it:
~~~
Hello, {user_name}! You said "{comment_text}".
~~~