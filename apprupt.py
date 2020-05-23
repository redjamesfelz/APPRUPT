f=open("Apprupt.txt", "r")
if f.mode == 'r':
    contents = f.read()
print(contents)

input('Press ENTER to continue...')

print('\n ### SELECT APPSTORE ###')
print('[1]  To Select Google Play Store, Press "1"')
print('[2]  To Select Apple App Store, Press "2"')

appstore = int(input('Select Appstore... 1 OR 2\n'))
if appstore == 1:
    print("You have selected Google play store")
else:
    print("You have selected Apple Appstore")

#if appstore ==1:
#for 500 times
#read logins.txt file
#get username
#get password
#Sign in
#https://accounts.google.com/
#Go to
#https://play.google.com/store/apps/details?id=<app id>
#Click Install Button
#//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[2]/div/div[2]/div/c-wiz/c-wiz/button
#Click Write a # REVIEW button
#//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/div/div[1]/div[1]/span/button
#Write in text box
#//*[@id="yDmH0d"]/div[2]/div/div[2]/span/div/div[3]/textarea
#Click 1 star
#//*[@id="yDmH0d"]/div[2]/div/div[2]/span/div/div[3]/div[2]/div[1]/span/div[1]/div
#Click Submit
#//*[@id="yDmH0d"]/div[2]/div/div[2]/div[3]/div/button[2]
#Click avatar
#//*[@id="gb"]/div[1]/div[1]/div[1]/div[2]/div[1]/a/span
#Click SignOut
#//*[@id="gb_71"]

