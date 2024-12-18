def Variation_2():
    list_of_IP_Addresses = [
        "192.168.1.1", "10.0.0.1", "172.16.0.0", "255.255.255.255", "0.0.0.0", "127.0.0.1",
        "192.168.0.256", "192.168.1", "192.168.1.300", "10.10.10", "10.10.10.10", "10.10.10.256",
        "300.168.0.1", "192.168.1.01", "123.456.78.90", "192.168.1.1.1", "192.168.1.abc", "10.0.0.0",
        "172.31.255.255", "192.168.001.1", "192.168.1.1a", "256.256.256.256", "111.111.111.111",
        "10.10.10.10.10", "192.0.2.146", "169.254.0.1", "10.0.0.256", "203.0.113.0", "172.16.0.1",
        "192.168.10.255", "1.2.3.4", "200.100.50.25", "172.16.1.2", "203.0.113.255", "255.255.255.0",
        "172.32.0.1", "8.8.8.8", "192.168.100.100", "123.045.067.089", "66.249.64.1", "192.168.1.999",
        "198.51.100.0", "203.0.113.1", "198.51.100.255"
    ]

    def is_valid_ip(ip):
        # Split the IP address by dots
        parts = ip.split(".")
        
        # Check if there are exactly 4 octets
        if len(parts) != 4:
            return False
        
        for part in parts:
            # Check if each part is a digit
            if not part.isdigit():
                return False
            
            # Convert part to an integer
            num = int(part)
            
            # Check if the number is in the valid range (0-255)
            if num < 0 or num > 255:
                return False
            
            # Check if there are no leading zeros (e.g., "01" is invalid but "0" is valid)
            if len(part) > 1 and part[0] == '0':
                return False

        # If all checks passed, the IP is valid
        return True

    # Iterate over the list and check each IP address
    valid, invalid = [], []
    for ip in list_of_IP_Addresses:
        if is_valid_ip(ip):
            valid.append(ip)
        else:
            invalid.append(ip)
    return valid, invalid

# Call the function
validIps, invalidIps = Variation_2()
print("\nHere  lies the Valid IPS:")
for ip in validIps: print(f'{ip} is valid')
print("\nHere  lies the InValid IPS:")
for ip in invalidIps: print(f'{ip} is invalid')
print("sari is so hot ".upper())