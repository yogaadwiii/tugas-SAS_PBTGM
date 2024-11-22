class Contact:
    def __init__(self, name, phone, email=None):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Nama: {self.name}, Telepon: {self.phone}, Email: {self.email if self.email else 'Tidak ada'}"


class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email=None):
        if name in self.contacts:
            print(f"Kontak dengan nama {name} sudah ada.")
        else:
            contact = Contact(name, phone, email)
            self.contacts[name] = contact
            print(f"Kontak {name} berhasil ditambahkan.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Kontak {name} berhasil dihapus.")
        else:
            print(f"Kontak dengan nama {name} tidak ditemukan.")

    def display_contacts(self):
        if not self.contacts:
            print("Tidak ada kontak yang disimpan.")
        else:
            print("Daftar Kontak:")
            for contact in self.contacts.values():
                print(contact)

    def find_contact(self, name):
        if name in self.contacts:
            print(self.contacts[name])
        else:
            print(f"Kontak dengan nama {name} tidak ditemukan.")


def main():
    manager = ContactManager()
    
    while True:
        print("\n--- Sistem Manajemen Kontak ---")
        print("1. Tambah Kontak")
        print("2. Hapus Kontak")
        print("3. Tampilkan Kontak")
        print("4. Cari Kontak")
        print("5. Keluar")

        choice = input("Pilih opsi (1-5): ")

        if choice == '1':
            name = input("Masukkan Nama kontak: ")
            phone = input("Masukkan nomor telepon: ")
            email = input("Masukkan email (opsional): ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            name = input("Masukkan nama kontak yang ingin dihapus: ")
            manager.remove_contact(name)
        elif choice == '3':
            manager.display_contacts()
        elif choice == '4':
            name = input("Masukkan nama kontak yang ingin dicari: ")
            manager.find_contact(name)
        elif choice == '5':
            print("Keluar dari sistem.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()