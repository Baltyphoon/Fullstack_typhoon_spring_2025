import sys 
import io 

print("Aldaanii messege", file=sys.stderr)

# standart garalt (stdout)
sys.stdout.write("Ene bol standart garalt\p")

# standart aldaa (stderr)
sys.stderr.write("ene bol aldaanii messej\p")

# standart orolt (stdin)
print("yamar neg zuil bicheed enter daran uu:")
user_input = sys.stdin.readline().strip()
print(f"ta bichsen: {user_input}")

# stdout-g tur chigluuleh 
original_stdout = sys.stdout
string_io = io.StringIO()
sys.stdout = string_io

print("ene barigdsan")
print("ene ch bas ")

sys.stdout = original_stdout
