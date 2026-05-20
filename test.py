import requests

REFRESH_TOKEN = "ory_rt_JNkcZdFV8NeHO2P7MDnQyq2VppDvqJ010YWF41ERzVU.R2soCuu6zF_q8awcHsFTH_5pzkchHiFagNdkUwBQkl4"
CLIENT_ID = "1de2c8be-a2dd-48e0-840c-ac0c36307938"
CLIENT_SECRET = ".yRXyV51YKf18DD.SNjHjIXy_p"

r = requests.post(
    "https://prelive-oauth2.quran.foundation/oauth2/token",
    auth=(CLIENT_ID, CLIENT_SECRET),
    data={"grant_type": "refresh_token", "refresh_token": REFRESH_TOKEN},
)
print("Refresh:", r.status_code)
print(r.json())
