import subprocess


def exe_cmd_wr(command, *args):
    try:
        sp = subprocess.Popen([command, *args], shell=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except:
        pass


exe_cmd_wr('ls -a -l')
#exe_cmd_wr('ls', ['-a', '-l'])
