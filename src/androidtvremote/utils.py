import re


def extract_services(input_string) -> list:
    lines = input_string.split("\n")
    lines = lines[1:]
    services = []
    pattern = r"(\d+)\t(\w+):\s+\[(.*?)\]"

    for line in lines:
        if match := re.search(pattern, line):
            service_id = int(match[1])
            service_name = match[2]
            service_process = match[3]

            service_info = {
                "id": service_id,
                "name": service_name,
                "package": service_process,
            }

            services.append(service_info)

    return services


def extract_ip(output):
    ip_pattern = r"\d+\.\d+\.\d+\.\d+:\d+"
    ip_addresses = []
    for line in output:
        ips = re.findall(ip_pattern, line)
        ip_addresses.extend(ips)
    if ip_addresses:
        return ip_addresses[0]
