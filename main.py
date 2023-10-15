'''
{Tugas 4 KAMSIS}
Silahkan baca README.txt
'''
import random #import random 
def step1 (input_num): # Step 1 ada di README.txt mengambil angka input dari user
    n = input_num - 1 # melakukan rumus angka_input - 1 (pada README.txt adalah n)
    test = True # Boolean untuk testing
    k = 1 # Menentukan k awal pasti 1
    while test:
        m = n//(2**k) # Menentukan m dengan rumus n / 2^k (Penggunaan floored division untuk mendapatkan angka pembulatan agar tidak dapat menjadi float)
        # print(f"ini m: {m}")
        # print(f"ini k: {k}")
        if m%2 == 1: # Mengecek apakah angka bisa di menjadi float
            fixed_m = int(m) # Mendapatkan m dan mengubahnya menjadi integer (Parno karna pas di coba awalnya jadi float terus)
            fixed_k = k # Mendapatkan k atau banyaknya iterasi
            # print(f"ini fix m: {fixed_m}")
            # print(f"ini fix k: {fixed_k}")
            test = False # testing dihentikan
        else:
            k+=1 # Apabila kondisi salah k ditambah 1 untuk menambah iterasi yang dibutuhkan
            # print(f"ini k: {k}")
            # print(f"ini m: {m}")
    return fixed_m, fixed_k # Mengeluarkan output m dan k yang sudah benar

def step2 (input_num): # Step 1 ada di README.txt mencari a
    a = random.randint(2, input_num-2) # a di random agar setiap perulangan bisa berbeda-beda
    print(f"ini a: {a}")
    return a # Mengeluarkan output a yang sudah benar

def step3(a, input_num, fixed_m, fixed_k): # Step 1 ada di README.txt testing prima atau bukan
    b = pow(a, fixed_m, input_num) # Melakukan Modular Expantion dengan fungsi pow() (awalnya buat sendiri ternyata udah ada dong)
    # print(f"ini b: {b}")
    if b == 1: # Kondisi apabila b = 1 maka angka merupakan prima
        return True
    else: 
        for _ in range(fixed_k): # Kalau bukan, angka akan di lakukan pengulangan kondisi terus sebanyak k
            if b == input_num - 1 or b == -1: # Kondisi menentukan untuk iterasi setelahnya jika sama dengan kondisi maka angka prima
                # print(f"ini b di looping (kalau benar): {b}")
                return True
            b = (b * b) % input_num # Algoritma komputasi setelah iterasi ke 1
    return False # Jika sudah dilakukan sebanyak k kali maka angka ditentukan bukan prima
        
def main():
    print('''NB: Must do at least three iterations to find the primality
    if 1 test has an output of Composite, means that the number
    is for sure a composite number fr fr no cap
          ''') # Kondisi penting 
    iter = int(input("Input for iterations: ")) # Input pengulangan pengencekan
    x = int(input("Enter number to find primality: ")) # Input angka yang di cek
    test_comp = 0 # Number of test kalau hasilnya bukan prima
    for _ in range(iter):
        m, k = step1(x) # Step 1
        a = step2(x) # Step 2
        state = step3(a, x, m, k) # Step 3
        if state == True:
            print("Number is Primal")
        elif state == False:
            print("Number is Composite")
            test_comp += 1
    if test_comp == 0:
        print("Number is probably a Primal")
    else:
        print("Number is definitely a Composite")
    
if __name__ == "__main__":
    main()