import time

username = input("Masukkan username target: ")
password_list = ["admin", "123456", "password", "admin123", "letmein"]

print(f"Mulai brute force ke user: {username}")
for password in password_list:
    print(f"Mencoba password: {password}")
    time.sleep(1)  # simulasi delay
    if password == "admin123":  # password yang 'benar' disimulasikan
        print(f"\n[+] Password ditemukan: {password}")
        break
else:
    print("\n[-] Password tidak ditemukan dalam daftar")
