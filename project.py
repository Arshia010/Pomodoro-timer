import sys
import time
import subprocess
 
WORK_MINUTES=25
BREAK_MINTUES=5

def main():
    try:
        if len(sys.argv)<=1:
            print(f"🍅 tomato {WORK_MINUTES} minutes. Ctrl+C to exit")
            tomato(WORK_MINUTES,"It is time to take break")
            print(f"☕ break{BREAK_MINTUES} minutes. Ctrl+C to exit")
            tomato(BREAK_MINUTES, "It is time to work")

        elif sys.argv[1]=="-t": #-time"
            minutes=int(sys.argv[2])if len(sys.argv)>2 else WORK_MINUTES
            print(f"🍅 tomato {minutes} minutes. Ctrl+C to exit")
            tomato(minutes, "It is time to take a break")

        elif sys.argv[1]=="-b": #"-break"
            minutes=int(sys.argv[2]) if len(sys.argv)>2 else BREAK_MINTUES
            print(f"☕ break{minutes} minutes. Ctrl+C to exit")
            tomato(minutes, "It is time to work")

        elif sys.argv[1]=="-h": #"-help"
            help()
        else:
            help()

    except KeyboardInterrupt:
        print("\n 👋 goodbye")

    except Exception as ex:
        print(ex)
        exit(1)



def tomato(minutes,notification_message):
    start_time=time.perf_counter()
    while True:
        diff_seconds=int(round(time.perf_counter()-start_time))
        left_seconds=minutes*60-diff_seconds
        if left_seconds<=0:
            print("")
            break


        countdown=(f"{int(left_seconds / 60)}:{int(left_seconds % 60)} ⏱️")
        duration=min(minutes,25)
        progress(diff_seconds, minutes * 60, duration, countdown)
        time.sleep(1)

    notification(notification_message)



def progress(curr,total,duration=10,extra=""):
    frac = curr / total
    filled=round(frac*duration)

    print(
        "\r",
        "🍅" * filled + "--" * (duration - filled),
        f"[{frac:.0%}]",
        extra,
        end="",
    )



def notification(message):
    print(message)
    try:
        if sys.platform.startswitch("Windows"):
            subprocess.Popen(["send_notification","🍅 ",message])
        else:
            pass
    except:
        pass


def help():
    appname = sys.argv[0]
    appname = appname if appname.endswith(".py") else "tomato"  # tomato is pypi package
    print(" 🍅 Tomato Clock ")
    print(
        f"{appname}         # start a {WORK_MINUTES} minutes tomato clock + {BREAK_MINUTES} minutes break"
    )
    print(f"{appname} -t      # start a {WORK_MINUTES} minutes tomato clock")
    print(f"{appname} -t <n>  # start a <n> minutes tomato clock")
    print(f"{appname} -b      # take a {BREAK_MINUTES} minutes break")
    print(f"{appname} -b <n>  # take a <n> minutes break")
    print(f"{appname} -h      # help")

if __name__=="__main__":
    main()
