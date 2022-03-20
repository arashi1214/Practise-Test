請建立一個.env 放置帳號密碼

金石堂簽到格式如下

ACCOUNT=你的帳號
PASSWORD=你的密碼

300 簽到格式如下

300_NAME=你的暱稱
300_PASSWORD=你的密碼

如果要直接輸入帳密，請將 os.getenv('ACCOUNT')/os.getenv('PASSWORD') 直接改為對應的帳密
