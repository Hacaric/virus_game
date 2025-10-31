import time

with open(__file__, "r") as f:
    content = f.read()

while True:
    try:
        with open(__file__, "r") as f:
            curr_content = f.read()
        if curr_content != content:
            raise Exception()
    except:
        with open(__file__, "w") as f:
            f.write(content)
    time.sleep(10)