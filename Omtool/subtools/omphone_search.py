import json
import os
import time
import sys
from colorama import Fore
import socket
import requests
import argparse
import schedule
import time
import logging

main_url = "https://ipqualityscore.com/api/json/phone/3xCII0XTawnHlluREioX4XIhIgaH4NQ2/"
def omphone(phno):
    print("\n")
    print("*********************************************************************************************************\n")
    print("************************************   PhoneNumber  *****************************************************\n")
    print("*********************************************************************************************************\n")
    phone_details = requests.post(main_url+phno).json()
    # print (phone_details)
    print("Validity : " + phone_details["message"])
    logging.info("Validity :"  + phone_details['message'])
    print("Fraud Score : " + str(phone_details["fraud_score"]))
    logging.info("Fraud Score : " + str(phone_details["fraud_score"]))
    print("Recent Abuse: " + str(phone_details["recent_abuse"]))
    logging.info("Recent Abuse: " + str(phone_details["recent_abuse"]))
    print("Name : " + phone_details["name"])
    logging.info("Name : " + phone_details["name"])
    print("Time Zone: " + phone_details["timezone"])
    logging.info("Time Zone: " + phone_details["timezone"])
    print("Carrier: " + phone_details["carrier"])
    logging.info("Carrier: " + phone_details["carrier"])
    print("City :" + phone_details["city"])
    logging.info("City :" + phone_details["city"])
    print("Leaked : " + str(phone_details["leaked"]))
    logging.info("Leaked : " + str(phone_details["leaked"]))
    print("Spammer : " + str(phone_details["spammer"]))
    logging.info("Spammer : " + str(phone_details["spammer"]))
