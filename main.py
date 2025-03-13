import customtkinter as ctk
import tkinter.messagebox as messagebox
import ipaddress

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def calculate():
    ip_input = ip_entry.get().strip()
    subnet_input = subnet_entry.get().strip()
    if not ip_input or not subnet_input:
        messagebox.showerror("Fehler", "Bitte IP-Adresse und Subnetzmaske eingeben.")
        return
    try:
        network = ipaddress.ip_network(f"{ip_input}/{subnet_input}", strict=False)
        net_address = network.network_address
        broadcast_address = network.broadcast_address
        if network.num_addresses > 2:
            first_host = ipaddress.ip_address(int(network.network_address) + 1)
            last_host = ipaddress.ip_address(int(network.broadcast_address) - 1)
        else:
            first_host = "Nicht vorhanden"
            last_host = "Nicht vorhanden"
        network_value.configure(text=str(net_address))
        broadcast_value.configure(text=str(broadcast_address))
        first_host_value.configure(text=str(first_host))
        last_host_value.configure(text=str(last_host))
        addresses_value.configure(text=str(network.num_addresses))
    except Exception as e:
        messagebox.showerror("Fehler", f"Ungültige Eingabe: {e}")

f = ctk.CTk()
f.title("IP Calculator")
window_width = 500
window_height = 450
screen_width = f.winfo_screenwidth()
screen_height = f.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
f.geometry(f"{window_width}x{window_height}+{x}+{y}")
f.resizable(False, False)

frame = ctk.CTkFrame(f, corner_radius=10)
frame.pack(padx=20, pady=20, fill="both", expand=True)

ip_label = ctk.CTkLabel(frame, text="IP-Adresse:", font=("Helvetica", 12))
ip_label.pack(pady=(10, 5))
ip_entry = ctk.CTkEntry(frame, width=250, font=("Helvetica", 12), placeholder_text="192.168.1.1")
ip_entry.pack(pady=(0, 10))

subnet_label = ctk.CTkLabel(frame, text="Subnetz (z.B. 24 oder 255.255.255.0):", font=("Helvetica", 12))
subnet_label.pack(pady=(10, 5))
subnet_entry = ctk.CTkEntry(frame, width=250, font=("Helvetica", 12), placeholder_text="24 oder 255.255.255.0")
subnet_entry.pack(pady=(0, 10))

calc_button = ctk.CTkButton(frame, text="Berechnen", font=("Helvetica", 12), command=calculate)
calc_button.pack(pady=(10, 10))

result_frame = ctk.CTkFrame(frame, corner_radius=10)
result_frame.pack(pady=(10, 10), fill="both", expand=True)
result_frame.grid_columnconfigure(0, weight=1)
result_frame.grid_columnconfigure(1, weight=1)
result_frame.grid_rowconfigure(0, weight=1)
result_frame.grid_rowconfigure(1, weight=0)

top_frame = ctk.CTkFrame(result_frame, corner_radius=10)
top_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=1)

left_frame = ctk.CTkFrame(top_frame, corner_radius=10)
left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
left_frame.grid_columnconfigure(0, weight=1)
left_frame.grid_columnconfigure(1, weight=1)

network_label = ctk.CTkLabel(left_frame, text="Netzwerkadresse:", font=("Helvetica", 12))
network_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
network_value = ctk.CTkLabel(left_frame, text="", font=("Helvetica", 12))
network_value.grid(row=0, column=1, sticky="w", padx=5, pady=5)

broadcast_label = ctk.CTkLabel(left_frame, text="Broadcast:", font=("Helvetica", 12))
broadcast_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
broadcast_value = ctk.CTkLabel(left_frame, text="", font=("Helvetica", 12))
broadcast_value.grid(row=1, column=1, sticky="w", padx=5, pady=5)

right_frame = ctk.CTkFrame(top_frame, corner_radius=10)
right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
right_frame.grid_columnconfigure(0, weight=1)
right_frame.grid_columnconfigure(1, weight=1)

first_host_label = ctk.CTkLabel(right_frame, text="Erster Host:", font=("Helvetica", 12))
first_host_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
first_host_value = ctk.CTkLabel(right_frame, text="", font=("Helvetica", 12), anchor="w")
first_host_value.grid(row=0, column=1, sticky="w", padx=5, pady=5)

last_host_label = ctk.CTkLabel(right_frame, text="Letzter Host:", font=("Helvetica", 12))
last_host_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
last_host_value = ctk.CTkLabel(right_frame, text="", font=("Helvetica", 12), anchor="w")
last_host_value.grid(row=1, column=1, sticky="w", padx=5, pady=5)

bottom_frame = ctk.CTkFrame(result_frame, corner_radius=10, width=200, height=50)
bottom_frame.grid(row=1, column=0, columnspan=2, sticky="n", padx=10, pady=10)
bottom_frame.grid_propagate(False)

addresses_label = ctk.CTkLabel(bottom_frame, text="Anzahl Adressen:", font=("Helvetica", 12))
addresses_label.pack(side="left", padx=5, pady=5)
addresses_value = ctk.CTkLabel(bottom_frame, text="", font=("Helvetica", 12))
addresses_value.pack(side="left", padx=5, pady=5)

f.mainloop()
