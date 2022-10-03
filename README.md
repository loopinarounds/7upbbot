# 7upbbot
(NO LONGER LIVE) A program that auto-enters the 7up Uber Eats Sweepstakes.

## GUIDE to Use 


<img width="629" alt="Screenshot 2022-10-03 at 15 02 07" src="https://user-images.githubusercontent.com/86264161/193657638-93f3eceb-705d-44e1-8460-c3ac29d6ad7a.png">




See Bible.csv (pictured Above) to enter all of your personal details as follows:

**Proxy**: Must be in IP:Port:User:Pass format (standard format), no other will work. If a proxy fails, the program will retry using the next proxy in the list. Always add more proxies than you have active emails etc.

**Email**: Required, gmail has higher success rate than any other format.

**First Name**: Required, can be random.

**Last Name**: Required, can be random.

**Phone Number**: Required, British Format + can be random as prizes are delivered via email.

**County**: Required, Must be a standard British County.

**Store**: Required, taken from a drop down box on the website. Options are stated in the Bible.csv, any can be chosen it does not affect the outcome.

```webhook = DiscordWebhook(url = 'Enter Webhook Here',rate_limit_retry=True)``` User **must** enter their Discord webhook into the driver_final.py file. The program will log successful entries to a discord webhook file, stating all of the bible.csv column values that were used to make the entry.

## COMMENTS:

The file is not compiled to an exe for ease of changing properties of the code. Threading is used to assure that multiple entries can be sent t once, however, because the 7up Website is slow to respond this can sometimes cause crashing. Anyone is welcome to remove the threading and have the program enter the raffle 1by1.

All packages used will need to be downloaded before running in shell.
