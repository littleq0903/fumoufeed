import sys
import os

def main():
    #if len(sys.argv) == 1:
    #    return

    #appId = sys.argv[1]
    appId = "fumoufeed"
    print "appId", appId

    # Update Main System
    # for macbook air environment
    # cmd = r'python "C:\Program Files (x86)\Google\google_appengine\appcfg.py"'
    # for normal environment
    #cmd = r'"C:\Program Files (x86)\Google\google_appengine\appcfg.py"'
    cmd = r'"appcfg.py"'
    os.system(cmd + " update app.yaml " + " -A %s -e zorro0555@gmail.com --passin "%appId)


if __name__ == "__main__":
    main()
