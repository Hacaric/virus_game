import time

with open(__file__, "r") as f:
    content = f.readlines()

while True:
    time.sleep(10)
    try:
        with open(__file__, "r") as f:
            curr_content = f.readlines()
        if curr_content != content:
            raise Exception()
    except:
        with open(__file__, "w") as f:
            f.writelines(content)