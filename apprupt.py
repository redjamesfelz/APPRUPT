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
