import datetime

def now():
    ntime=datetime.datetime.now()
    nt=ntime.strftime('%H:%M:%S')
    return nt

now()