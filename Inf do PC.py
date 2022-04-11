import wmi

carregar = wmi.WMI()
sistema = carregar.Win32_ComputerSystem()[0]

print(f"Marca: {sistema.Manufacturer}")
print(f"Modelo: {sistema.Model}")
print(f"Nome: {sistema.Name}")
print(f"Quantidade de CPUs: {sistema.NumberOfProcessors}")
print(f"Arquitetura: {sistema.SystemType}")
print(f"Família: {sistema.SystemFamily}")
