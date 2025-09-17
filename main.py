import argparse
import pyfiglet
from colorama import Fore, Style

def print_banner():
    ascii_banner = pyfiglet.figlet_format("NetProbe", font="slant")
    print(Fore.CYAN + ascii_banner + Style.RESET_ALL)

    print(f"{Fore.YELLOW}A lightweight CLI network reconnaissance tool with OS fingerprinting{Style.RESET_ALL}")
    print(f"Version: 1.0.0")
    print(f"Author : Group 10")
    print("Inspired by Nmap & Masscan - Fast, Lightweight, Extensible\n")

    print(Fore.RED + "[!] Legal Disclaimer:" + Style.RESET_ALL)
    print("    Usage of NetProbe for attacking targets without prior mutual consent is illegal.")
    print("    It is the end user's responsibility to comply with all applicable laws.")
    print("    Developers assume no liability for misuse or damage caused by this tool.\n")

def main():
    print_banner()
    parser=argparse.ArgumentParser(description="Netprobe - Công cụ quét mạng hạng nhẹ ",formatter_class=argparse.RawTextHelpFormatter)
    # Target Specification
    target_group=parser.add_argument_group("Target Specification")
    target_group.add_argument("--target",nargs="+", type=str, help="--target <Ips, Domain, CIDR>")
    target_group.add_argument("-iL",dest="target_file",type=str, help="-iL filename.txt")
    # Scan type
    scan_type_group=parser.add_argument_group("Scan type")
    scan_type_group.add_argument("-sS",action="store_true", help="-sS <target> : Quét kiểu SYN ")
    scan_type_group.add_argument("-sT",action="store_true", help="-sT <target> : Quét kiểu TCP connection ")
    scan_type_group.add_argument("-sU",action="store_true", help="-sU <target> : Quét kiểu UDP ")
    # Host Discovery
    host_discovery_group=parser.add_argument_group("Host Discovery")
    host_discovery_group.add_argument("-sn",action="store_true", help="-sn <target> : Ping scan ")
    host_discovery_group.add_argument("-sL",action="store_true", help="-sL <target> : Liệt kê mục tiêu ")
    host_discovery_group.add_argument("-PA",action="store_true", help="-PA Ports <target> : TCP ACK scan ")
    # Port scanning
    port_group = parser.add_argument_group("Port Scanning")
    exclusive_port_group = parser.add_mutually_exclusive_group()
    exclusive_port_group.add_argument("-p", dest="ports", type=str, help="-p <Port> : Quét một cổng")
    exclusive_port_group.add_argument("-p-", dest="scan_all_ports", action='store_true', help="-p- : Quét tất cả các cổng")
    exclusive_port_group.add_argument("-F", dest="fast_scan", action='store_true', help="-F : Quét nhanh 100 cổng")
    # Service & Version Detection
    service_version_group=parser.add_argument_group("Service & Version Detection")
    service_version_group.add_argument("-sV", dest="service_version", action="store_true", help="-sV <target> : Phát hiện phiên bản & dịch vụ")
    service_version_group.add_argument("--version-light", action="store_true", help="-sV --version-light <target> : Quét chế độ nhẹ")
    service_version_group.add_argument("--version-all", action="store_true", help="-sV --version-all <target> : Quét chế độ mạnh")
    # OS Detection
    os_group=parser.add_argument_group("OS Detection")
    os_group.add_argument("-O",dest="os_detection", action="store_true" ,help="-O <target> : Phát hiện hệ điều hành")
    os_group.add_argument("--osscan-guess",dest="os_guess", action="store_true", help="-O ---osscan-guess <target> : Đoán hệ điều hành")
    # Output Options
    output_group=parser.add_argument_group("Output Options")
    output_group.add_argument("-oN",dest="output_normal",type=str, help="-oN <file> <target> : Đầu ra thông thường")
    output_group.add_argument("-oX",dest="output_xml",type=str, help="-oX <file> <target> : Đầu ra XML")
    output_group.add_argument("--open", action="store_true" ,help="--open <target> : Chỉ hiển thị cổng mở")

    args=parser.parse_args()
    print(f"{Fore.GREEN}[+] Arguments parsed successfully:{Style.RESET_ALL}")
    print(vars(args))

if __name__=="__main__":
    main()
