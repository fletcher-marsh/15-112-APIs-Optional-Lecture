## Installation

Run the following commands:

```bash
python3 -m pip install google-cloud-speech
python3 -m pip install cffi
python3 -m pip install sounddevice
```

## Create a Google Cloud Service Account

1. Create a Google Account (might be blocked on your andrew account).
2. Go [here](https://console.cloud.google.com/apis/credentials/serviceaccountkey)
3. Select New Service account. Choose any service account name, and select the role as Project > Owner. 
4. Click create and save the file that is downloaded into your current directory.
5. Rename that file to clientSecret.json

## Run the given demo file by doing the following commands

```bash
GOOGLE_APPLICATION_CREDENTIALS=./clientSecret.json python3 demo.py
```

Note: This file is a modified version of this tutorial: 
https://cloud.google.com/docs/authentication/getting-started