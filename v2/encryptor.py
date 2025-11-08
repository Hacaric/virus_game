import zlib, os, base64, sys
sys.path.append(os.path.dirname(__file__))

target = input("Enter target file: ")
encryped_file = f"encrypted_{target}"
if os.path.exists(encryped_file):
    if input("Encrypted version of this file already exists. Overwrite? (y/n): ") != "y":
        print("Abort.")
        exit()

content = open(target, "rt").read()
func = base64.encodebytes
func_str_reverse = "base64.decodebytes"
# func_reverse = base64.decodebytes
# func_str = "base64.encodebytes"


# encrypted_content = base64.encodebytes(zlib.compress(content.encode("utf-8")).decode('utf-8'))#.decode('utf-8')
encrypted_content = func(content.encode('utf-8'))[:-1].decode('utf-8')

new_content = f"import {func_str_reverse.split()[0]}; exec({func_str_reverse}('''{encrypted_content}'''.encode('utf-8')).decode('utf-8'))"

with open(encryped_file, "w") as f:
    f.write(new_content)

print("Done.")


