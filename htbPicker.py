#!/usr/bin/env python3
#
# Author: Andres Moreno (TheGoodHacker)
# x.com/thegoodhackertv

import argparse
import json
import os
import random
import requests
import sys
import urllib3

urllib3.disable_warnings()

API_KEY=os.environ['HTBKEY'] # export HTBKEY="YOUR_API_KEY"
BASE_URL="https://www.hackthebox.com/api/v4/"

def banner():
    banner = r'''
                                _                 
                    |_ _|_ |_  |_) o  _ |   _  ._ 
                    | | |_ |_) |   | (_ |< (/_ |  
                                            
            '''
    print(banner)

def arg_parse():
    example = 'Example:\n\n'
    example += '$ python3 htbPicker.py --update\n'
    example += '$ python3 htbPicker.py -d Easy -s 4.2 -os Windows\n'
    example += '$ python3 htbPicket.py -d Medium -s 3.2 -os Linux --random'
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=banner(), epilog=example)
    parser.add_argument('-u', '--update', dest='update', help="Update machine database", default=False, action="store_true", required=False)
    parser.add_argument('-d', '--difficulty',metavar="DIFFICULTY", dest='difficulty', help="Machine difficulty", required=False)
    parser.add_argument('-s', '--stars',metavar="MIN_STARS", dest='stars', type=float, help="Minimum stars", required=False)
    parser.add_argument('-os', '--op-system', metavar="OS", dest='os', help="Operating System", required=False)
    parser.add_argument('-r', '--random', dest='random', help="Pick a random machine", default=False,action="store_true", required=False)

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return args

def get_retired_all():
    retired_url = f"{BASE_URL}machine/list/retired"
    headers = {"Authorization": f"Bearer {API_KEY}", "Accept": "application/json, */*", "User-Agent": "htbPicker v1.0"}
    print("Downloading machines into allmachines.json\n wait..")
    response = requests.get(retired_url, headers=headers)
    if response.status_code == 200:
        print("Done!")
    else:
        print("Failed...")
    allMachines = response.json()
    json_object = json.dumps(allMachines, indent=4)

    with open("allmachines.json", "w") as outfile:
        outfile.write(json_object)

def printall():
    total=0
    filtered=0
    id_list = list()

    with open('allmachines.json', 'r') as openfile:
        json_object = json.load(openfile)
    
    for machine in json_object["info"]:
        if machine["difficultyText"] == args.difficulty.title() and machine["stars"] >= float(args.stars) and machine["os"] == args.os.title():
            filtered+=1
            id_list.append(machine["id"])
            #print("id: " + str(machine["id"]))
            print("Name: " + machine["name"])
            print("Difficulty: " + machine["difficultyText"])
            print("Stars: " + str(machine["stars"]))
            print()
        total+=1
    print(f"Found {filtered} machines from {total}\n")
    return id_list

def get_random(id_list):
    print("Picking a random machine from results...\n")

    rand = random.randint(0, len(id_list)-1)

    with open('allmachines.json', 'r') as openfile:
        json_object = json.load(openfile)

    for machine in json_object["info"]:
        if machine["id"] == id_list[rand]:
            print("="*20)
            #print("id: " + str(machine["id"]))
            print("Name: " + machine["name"])
            print("Difficulty: " + machine["difficultyText"])
            print("OS: " + machine["os"])
            print("Stars: " + str(machine["stars"]))
            print("="*20)
            print()

def main():
    if args.update:
        get_retired_all()
    else:
        id_list = printall()
        if args.random:
            get_random(id_list)

if __name__ == "__main__":
    try:
        args = arg_parse()
        main()
    except Exception as e:
        print(e)