import json, base64, sys, os, argparse

parser=argparse.ArgumentParser(description='This is a little Tool for extracting the certificates from the acme')
parser.add_argument('--file',help='The location of the acme.json file', type= str, default= "acme.json")

args=parser.parse_args()

def main():
    data = json.load(open(args.file))
    for x in data["default"]["Certificates"]:
        cert = x["certificate"]
        f= open(x["domain"]["main"]+".crt","w",encoding="utf-8")
        cert = base64.b64decode(cert)
        f.write(cert.decode("utf-8"))
        f.close()
