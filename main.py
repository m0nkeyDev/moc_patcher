import os
from glob import glob
import subprocess


def is_moceable(str_analyze):
    if str_analyze.find("Q_OBJECT") > 0:
        return True

    else:
        return False


all_headers = [y for x in os.walk("/home/{{user}}/git/worktips-lite-wallet") for y in glob(os.path.join(x[0], '*.h'))]

for c_result in all_headers:

    with open(c_result) as file:
        moceable = is_moceable(file.read())

        if moceable is True:
            full_path = os.path.dirname(c_result)

            file_n = os.path.basename(c_result)
            file_n = os.path.splitext(file_n)[0]
            file_n = full_path + "/moc_" + file_n + ".cpp"

            print("Generating MOC file over " + file_n)

            #subprocess.call(['/mnt/g/Qt/Qt5.10.1/5.10.1/msvc2017_64/bin/moc.exe', c_result, "-o", file_n])
