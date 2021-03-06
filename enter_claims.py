#!/usr/bin/env python3
import sqlite3

def enter_claim(conn):
    c = conn.cursor()

    date = input("enter claim date: ")
    claim_num = input("enter claim number: ")
    code = input("enter claim code: ")
    provider = input("enter claim provider: ")
    amount = input("enter amount you paid to provider: ")

    data = (date, claim_num, code, provider, float(amount))
    c.execute("INSERT INTO claims VALUES (?,?,?,?,?)", data)
    conn.commit()

def main():
    print("Poor man's claim data entry system is initiated. Follows \
instructions please.")

    conn = sqlite3.connect("claims.db")
    c = conn.cursor()

    count = 0
    while True:
        print("")
        enter_claim(conn)
        count += 1
        do_continue = input("Continue? ('q' exit): ")
        if do_continue.lower() == "q":
            conn.close()
            break
    print("Total of {count} claims entered. Claim program exited.".format(
        count=count)

if __name__ == "__main__":
    main()
