from tkinter import *
start_time=int(input("Enter start time: "))
class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.pack()
        self.createWidgets()
        self._alarm_id = None
        self._paused = False
        self._starttime = start_time * 60
    def demoColorChange(): button1.configure(bg="red", fg="yellow")
    def createWidgets(self):
        self.someFrame = Frame(self)
        self.labelvariable = StringVar()
        self.labelvariable.set(start_time)

        self.thelabel = Label(self,textvariable = self.labelvariable,font=('Helvetica',50))
        self.thelabel.pack(side=TOP)
        self.startButton = Button(self.someFrame, text="Start",command=self.startTime,fg='green',bg='white')
        self.startButton.pack(side=LEFT)

        self.stopButton = Button(self.someFrame, text="Pause", command=self.stopTime,fg='red',bg='white')
        self.stopButton.pack(side=LEFT)

        self.resetButton = Button(self.someFrame, text="Reset", command=self.resetTime,bg='white')
        self.resetButton.pack(side=LEFT)
        self.someFrame.pack(side=TOP)

     

        #self.firstButton = Button(self,text="pomodoro",command=self.pomodoro)
        #self.firstButton.pack(side=LEFT)

        #self.secondButton = Button(self,text="short break",command=self.shortBreak)
        #self.secondButton.pack(side=LEFT)

        #self.thirdButton = Button(self,text="long break",command=self.longBreak)
        #self.thirdButton.pack(side=LEFT)

   #def pomodoro(self):
        #if self._alarm_id is not None:
        #    self.master.after_cancel(self._alarm_id)
        #self.countdown(1500)

    #def shortBreak(self):
        #if self._alarm_id is not None:
        #    self.master.after_cancel(self._alarm_id)
        #self._paused = False
        #self.countdown(300)

    #def longBreak(self):
        #if self._alarm_id is not None:
        #   self.master.after_cancel(self._alarm_id)
        #self._paused = False
        #self.countdown(600)

    def startTime(self):
        """ Resume """
        self._paused = False
        if self._alarm_id is None:
            self.countdown(self._starttime)

    def stopTime(self):
        """ Pause """
        if self._alarm_id is not None:
            self._paused = True

    def resetTime(self):
        """ Restore to last countdown value. """
        if self._alarm_id is not None:
            self.master.after_cancel(self._alarm_id)
            self._alarm_id = None
            self._paused = False
            self.countdown(self._starttime)
            self._paused = True

    def countdown(self, timeInSeconds, start=True):
        if start:
            self._starttime = timeInSeconds
        if self._paused:
            self._alarm_id = self.master.after(1000, self.countdown, timeInSeconds, False)
        else:
            mins, secs = divmod(timeInSeconds, 60)
            if(mins!=0 or secs !=0):
                timeformat = "{0:02d}:{1:02d}".format(mins, secs)
                print(timeformat)
                app.labelvariable.set(timeformat)
                self._alarm_id = self.master.after(1000, self.countdown, timeInSeconds-1, False)
            app.labelvariable.set(timeformat)


if __name__ == '__main__':
    root = Tk()
    root.title("My Timer")
    root.geometry('350x450+700+200')
    app = Application(root)
    root.mainloop()
