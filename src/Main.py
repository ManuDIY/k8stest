import requests

message = "Hello world!"
hook = "616744282329579610/VuzdsQr6uhudvqYE7UToBSsGObOu_jtkeJeeR_zGRrimTq7buelB9TDoLDyGl1bIxQuv"  # replace w/ ur hook
response = requests.post("https://discordapp.com/api/webhooks/{hook}".format(hook=hook),
                         json={"content": message})
