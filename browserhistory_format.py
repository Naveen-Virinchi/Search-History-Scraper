
import browserhistory as bh
dict_obj = bh.get_browserhistory()
dict_obj.keys()

# Write the data to csv files in the current working directory.
# safari_browserhistory.csv, chrome_browserhistory.csv, and firefox_browerhistory.csv.
bh.write_browserhistory_csv()
# Create csv files that contain broswer history in working directory

import pandas as pd
chrome_data = pd.read_csv("chrome_history.csv",names=["website","description","date"])
firefox_data = pd.read_csv("firefox_history.csv",names=["website","description","date"])
my_browser_history = chrome_data.append(firefox_data).reset_index(drop=True).dropna()

sensitive_keywords = ["account", "accounts", "admissions", "amazon", "app.box"
                        "bank", "basecamp", "bing", "bookings", "bookshelf",
                         "calendar", "career", "cas", "chase",
                        "check-in", "chrome", "console", "docs.google",
                        "drive.google", "epay",
                         "facebook.com", "file:", "flywire", "funds",
                         "hotstar", "instructure", "launchpad","linkedin",
                         "localhost", "login", "mail", "maps", "messages",
                         "microsoft", "mozilla",
                         "netflix", "Naveen", "nofap", "outlook", "password",
                         "permission", "primevideo", "piazza.com", "pinterest", "portal",
                         "privacy", "quickpay", "reddit", "register", "redirects",
                         "reservations", "resume", "scheduler", "secure",
                         "slack", "support", "tvshows", "twitter", "uber",
                         "udemy", "user", "whatsapp", "wordpress", "yatra",
                         "youtube.com", "zoom"]


for idx, row in my_browser_history.iterrows():

    row["date"] = str(row["date"][:10])

    for word in sensitive_keywords:
        if row["website"].find(word) != -1:
            try:
                my_browser_history = my_browser_history.drop(index=idx)
            except KeyError: pass

    if row["website"].find("https://www.google.com/search") != -1:
        row["website"] = "https://www.google.com/search"


my_browser_history.to_csv("browser_history.csv")