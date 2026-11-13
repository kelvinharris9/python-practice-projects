MAX_FAILURES = 3
WINDOW_MINUTES = 30
file_name = "test_log_full.txt"

def read_log(filename):
    temp_entries = []
    entries = []
    try:
        with open(filename, "r") as f:
            for line in f.readlines():
                temp_entries.append(line.strip().split(" | "))
    except FileNotFoundError:
        print("File not found.\n\n")
        exit()

    for login_attempt in temp_entries:
        entries.append({"Timestamp": login_attempt[0],
                        "Username": login_attempt[1],
                        "IP": login_attempt[2],
                        "Result": login_attempt[3]})
    return entries

def find_flagged_accts(entries):
    consec_fails = {}
    flagged = {}
    for entry in entries:
        if entry["Result"] == "FAILED":
            if entry["Username"] not in consec_fails:
                consec_fails[entry["Username"]] = 1
            else:
                consec_fails[entry["Username"]] += 1
            if consec_fails[entry["Username"]] >= MAX_FAILURES and entry["Username"] not in flagged:
                flagged[entry["Username"]] = {"Consecutive Fails": consec_fails[entry["Username"]]}
            elif consec_fails[entry["Username"]] >= MAX_FAILURES and entry["Username"] in flagged:
                if consec_fails[entry["Username"]] > flagged[entry["Username"]]["Consecutive Fails"]:
                    flagged[entry["Username"]] = {"Consecutive Fails": consec_fails[entry["Username"]]}
        elif entry["Result"] == "SUCCESS":
            consec_fails[entry["Username"]] = 0
    return flagged

def display_report(flagged):
    print("-----Flagged Accounts-----\n"
          "  Flagged | Consecutive  \n"
          "   Acct   |  Failures  \n"
          "--------------------------")
    for entry, consec_fails in flagged.items():
        print(f"{entry:^10}|{consec_fails["Consecutive Fails"]:^12}")

def main():
    entries = read_log(file_name)
    flagged = find_flagged_accts(entries)
    display_report(flagged)

if __name__ == "__main__":
    main()