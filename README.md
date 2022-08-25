# Get Android Notifications

## 1. Download Android Debug Bride(ADB)
- Download ADB: [https://developer.android.com/studio/releases/platform-tools](https://developer.android.com/studio/releases/platform-tools)

## 2. Set ADB to your system environment variable

## 3. Enjoy
```
notifications = Android_Notifications()

# show all notifications
print(notifications.notifications)

# if you only want to get sms messages
sms = notifications.get_sms()

# if you want to get another app's notifications
notifications.get_notification_by_pakage_name("your_app_pakage_name")
```