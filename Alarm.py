import json
from datetime import datetime, date, timedelta
import os
import time
import pygame
#nextalarms = []
#isPlaying = False
#sound = "alarm.wav"
#data = []


class Alarms(object):

    def __init__(self):
        self.nextalarms = []
        self.isPlaying = False
        self.sound = "alarm.wav"
        self.data = []
        self.playedAlarm = None
        pygame.mixer.init()
        pygame.mixer.music.load(self.sound)
        

    def findAlarms(self):
        try:
            with open('alarms.json') as json_file:  
                self.data = json.load(json_file)
                #for p in data['alarmas']:
                    #print(str(datetime.now().time()))
                    #print(p)
        except:
            print("error") 

            
    def setAlarms(self):
        now = datetime.now().time()
        #print(now)
        f = "%H:%M:%S"
        #print(nextalarms)
        for alarm in self.data['alarmas']:
            alarmtime = datetime.strptime(alarm['time'], f)
            alarmtime = datetime.combine(date.today(), alarmtime.time())
            #print(alarmtime)
            if(alarm['on'] and alarmtime.time() > now):
                #print("added alarm")
                if alarmtime not in self.nextalarms:
                    self.nextalarms.append(alarmtime)
                    
        #print("array after adding:", self.nextalarms, "\n")

    def playAlarm(self):
        for alarm in self.nextalarms:
            now = datetime.now()
            #print("current alarm:", alarm)
            #print("now:", now)
            if alarm < now:
                if self.isPlaying == False:
                    #print("Began playing")
                    self.playedAlarm = self.nextalarms.index(alarm)                    
                    
                    pygame.mixer.music.play(-1)
                    self.isPlaying = True
                    #self.detectFace()
                    #print("Alarm playing")
                    #print(self.isPlaying)

    def stopAlarm(self):
        if(self.isPlaying):
            #time.sleep(5)
            pygame.mixer.music.stop()
            self.nextalarms.pop(self.playedAlarm)
            self.isPlaying = False
            #print("index: \n", self.playedAlarm)
            #print("array after stop:", self.nextalarms)
            f = open("detection.txt", "w+")
            f.write("no")
            f.close()



    def detectFace(self):
        f = open("detection.txt")
        linea = f.readline()
        if linea == "si":
        #time.sleep(5)
            print("apagar alarma")
            self.stopAlarm()        

    def startScript(self):
        now = datetime.now()
        for alarm in self.nextalarms:
            if alarm + timedelta(minutes=-1) < now:
                os.system('python prueba.py')

    def main(self):
        self.findAlarms()
        self.setAlarms()
        self.playAlarm()
        #self.startScript()
        while self.isPlaying == True:
            self.detectFace()


a = Alarms()
while True:
    a.main()    
"""
#now = datetime.now().time()
now = datetime.combine(date.today(), datetime.now().time())
print(now)

f = "%H:%M:%S"
datetime_obj = datetime.strptime(alarm, f)

print(datetime_obj.strftime(f))

# Choose 6PM today as the time the alarm fires.
# This won't work well if it's after 6PM, though.
alarm_time = datetime.combine(date.today(), datetime_obj.time())
#alarm_time = datetime_obj.time()  - now
print(alarm_time)

# Think of time.sleep() as having the operating system set an alarm for you,
# and waking you up when the alarm fires.
time.sleep((alarm_time - now).total_seconds())
#os.system("start sound1.mp3")
winsound.PlaySound(sound, winsound.SND_ASYNC)
time.sleep(2)
winsound.PlaySound(None, winsound.SND_PURGE)    
"""
"""
while existAlarm == True:
    for i in range(0, len(data["alarmas"])):
        alarm = data["alarmas"][i]["time"]
        alarm_time = datetime.strptime(alarm, f)
        now = datetime.now().time()
        print(str(alarm) +" ---- "+ str(now))
        if(alarm == now):
            #os.system("start sound1.mp3")
            winsound.PlaySound(sound, winsound.SND_ASYNC)
            time.sleep(2)
            winsound.PlaySound(None, winsound.SND_PURGE)    
"""