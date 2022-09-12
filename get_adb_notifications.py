import subprocess
import os

class Android_Notifications:
    def __init__(self):
        self.notifications = {}

    def get_notifications(self):
        temp_path = "./sms.txt"
        subprocess.getoutput(f'adb shell dumpsys notification --noredact > {temp_path}')
        notification_logs = None

        with open(temp_path, "r", encoding="utf-8") as f:
            notification_logs = f.read()
        os.remove(temp_path)

        notification_logs = notification_logs[notification_logs.find("NotificationRecord"):].split("NotificationRecord")
        self.notifications = {}
        for n_log in notification_logs:
            n_logs = n_log.split("\n")
            temp = {}
            pkg = None
            for l in n_logs[0].split(" "):
                if l.startswith("pkg="):
                    pkg = l[4:]
                    if not self.notifications.get(pkg):
                        self.notifications[pkg] = []

            if pkg:
                for log in n_logs:
                    line = log.strip()
                    if line.startswith("android.text="):
                        if "String" in line:
                            self.notifications[pkg].append(line[line.find("(")+1:-1])
                    if line.startswith("android.messages=Parcelable[]"):
                        self.notifications[pkg] = []
                    if "Bundle[{" in line:
                        self.notifications[pkg].append(line[line.find(", text")+7:-22])

        return self.notifications

    def get_sms(self):
        return self.get_notification_by_pakage_name("com.google.android.apps.messaging")

    def get_notification_by_pakage_name(self, pkg_name: str):
        self.get_notifications()
        return self.notifications.get(pkg_name) if self.notifications.get(pkg_name) else []

if __name__ == "__main__":
    notifications = Android_Notifications()
    smss = notifications.get_sms()
    test = notifications.get_notification_by_pakage_name("com.facebook.orca")
    print(smss)
    print(test)
    import json
    print(json.dumps(notifications.get_notifications(), ensure_ascii=False, indent=4))