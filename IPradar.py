#######  LIBRARIES  #######
import psutil
import time
# ipwhois
###########################

###### Check if ipwhois is Installed #######
try:
    from ipwhois import IPWhois
    print("[!] IPWhois is installed :-)")
except ImportError:
    print("[!] IPWhois is not installed :-(")
############################################


processed_ips = set() # Set of IPs to avoid duplicates


########################## FUNCTIONS #########################
def fetch_info(ip):
    """
    Fetches the organization name, country, state, and city for 'ip' parameter
    """
    try:
        obj = IPWhois(ip)                                                                        # Create an IPWhois object
        results = obj.lookup_whois()                                                             # Perform "whois" lookup
        org_name = results.get('org') or results.get('nets', [{}])[0].get('name') or "?"         # Get the organization name
        country = results.get('nets', [{}])[0].get('country') or "?"                             # Get the country
        state = results.get('nets', [{}])[0].get('state') or "?"                                 # Get the state
        city = results.get('nets', [{}])[0].get('city') or "?"                                   # Get the city
        return org_name, country, state, city
    except Exception as e:
        return str(e), "N/A", "N/A", "N/A"

# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #

def monitor():
    """
    Monitors established connections and displays their organization name, country, state, and city
    """
    B_PURPLE = '\033[38;5;165;1m' # Bright Purple
    WHITE = '\033[97m'            # White
    max_org_length = 20           # Max string length for organization name
    max_country_length = 6        # Max string length for country name
    max_state_length = 4          # Max string length for state name
    max_city_length = 15          # Max string length for city name
    header = "|       IP        |  PORT  |    ORGANIZATION       |      CITY       |  STATE  | COUNTRY |"
    table_thick = "=" * len(header)
    table_thin = "-" * len(header)
    tbcl = B_PURPLE               # Table Color
    txtc = WHITE                  # Text Color
    incol = f"{tbcl}|{txtc}"      # Inner Column Lines
    print(tbcl + table_thick)
    print(tbcl + header)
    print(tbcl + table_thin)
    while True:
        connections = set()       # A set that holds IP data
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == 'ESTABLISHED':
                connections.add((conn.laddr.ip, conn.laddr.port, conn.raddr.ip, conn.raddr.port))  # Add Connection to the Set

        for conn in connections:
            l_ip, l_port, r_ip, r_port = conn
            if r_ip not in processed_ips:
                # Get organization name, country, state, and city for IP
                org_name, country, state, city = fetch_info(r_ip)
                print(f"{incol} {r_ip:<15} {incol}  {r_port:<5} {incol}  {org_name[0:max_org_length]:<{max_org_length}} {incol} {city[0:max_city_length]:<{max_city_length}} {incol}   {state:<{max_state_length}}  {incol}   {country:<{max_country_length}}{tbcl}{incol}")
                processed_ips.add(r_ip)
        time.sleep(1)   # Refresh Rate
##############################################################


########### MAIN FUNCTION ##########
if __name__ == "__main__":
    try:
        # Check and display Python version
        import sys
        print(f"[!] Running Python version: {sys.version}")

        # Start
        monitor()
    except KeyboardInterrupt:
        print("[!] Terminating...")
###################################



#                             @@@@@@@@@@@@@                                            
#                          @@@@@@@@@@@@@@@@@@@                                            
#                      @@@@@@@@@@@@@@@@@@@@@@@@@@@                                        
#                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                     
#                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                  
#              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                
#             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                               
#           @@@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@                             
#          @@@@@@@@@        @@@@@@     @@@@@@        @@@@@@@@@                            
#         @@@@@@@@@@                                 @@@@@@@@@@                           
#        @@@@@@@@@@@                                 @@@@@@@@@@@                          
#       @@@@@@@@@@@@                                 @@@@@@@@@@@*                         
#       @@@@@@@@@@@                                   @@@@@@@@@@@                         
#      @@@@@@@@@@@                                     @@@@@@@@@@@                        
#      @@@@@@@@@@@ https://github.com/hassanfarescodes @@@@@@@@@@@                        
#      @@@@@@@@@@.                                     :@@@@@@@@@@                        
#      @@@@@@@@@@                                       @@@@@@@@@@                        
#      @@@@@@@@@@@                                     @@@@@@@@@@@                        
#      @@@@@@@@@@@                                     @@@@@@@@@@@                        
#      @@@@@@@@@@@                                     @@@@@@@@@@@                        
#      %@@@@@@@@@@@                                   @@@@@@@@@@@                         
#       @@@@@@@@@@@@                                 @@@@@@@@@@@@                         
#        @@@@@@@@@@@@@                             @@@@@@@@@@@@@                          
#        @@@@@@   @@@@@@@@                     @@@@@@@@@@@@@@@@@                          
#         @@@@@@    @@@@@@@@@@             @@@@@@@@@@@@@@@@@@@@                           
#          @@@@@@@   @@@@@@@@               @@@@@@@@@@@@@@@@@@                            
#            @@@@@@     @@@@                @@@@@@@@@@@@@@@@                              
#             @@@@@@                        @@@@@@@@@@@@@@@                               
#               @@@@@@@                     @@@@@@@@@@@@@                                 
#                 @@@@@@@@@@@               @@@@@@@@@@@                                   
#                   @@@@@@@@@               @@@@@@@@@                                     
#                      @@@@@@               @@@@@@
#                         @@@@@@@@@@@@@@@@@@@@@
#                            @@@@@@@@@@@@@@@
