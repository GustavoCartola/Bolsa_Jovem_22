import wmi

load = wmi.WMI()
system = load.Win32_ComputerSystem()[0]

print(f"Marca: {system.Manufacturer}")  # Manufacturer
print(f"Modelo: {system.Model}")  # Model
print(f"Nome: {system.Name}")  # Name
print(f"Quantidade de CPUs: {system.NumberOfProcessors}")  # Number of Processors
print(f"Arquitetura: {system.SystemType}")  # System Architecture
print(f"Família: {system.SystemFamily}")  # System Family
