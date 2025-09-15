# Nama file: nested_if_statement.py
jenis_kelamin = "pria"
umur = 20
if (jenis_kelamin == "pria"):
    if(umur >= 25):
        print("Print boleh menikah")
    else:
        print("Pria tidak boleh menikah")
elif (jenis_kelamin == "wanita"):
    if (umur >= 20):
        print("Wanita boleh menikah")
    else:
        print("Wanita tidak boleh menikah")
else:
    print("Jenis kelamn tiodak terdaftar")
    print("Hari tidak valid")