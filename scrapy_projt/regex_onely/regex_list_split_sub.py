import re
ips = ['123.123.123','234.234.234, 456.456.456','678.678.678 (hello)']
clean_ips = [x for sublist in
             [re.findall(r'([\d.]+)', ip) for ip in ips]
             for x in sublist]
print(clean_ips)
# ['123.123.123', '234.234.234', '456.456.456', '678.678.678']
