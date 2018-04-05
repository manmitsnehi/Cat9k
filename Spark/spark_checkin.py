from ciscosparkapi import CiscoSparkAPI
import cli

if __name__ == '__main__':
    # Use ArgParse to retrieve command line parameters.
    from argparse import ArgumentParser

    #parser = ArgumentParser("Spark Check In")
    ## Retrieve the Spark Token and Destination Email
    #parser.add_argument(
    #    "-t", "--token", help="Spark Authentication Token", required=True
    #)
    ## Retrieve the Spark Token and Destination Email
    #parser.add_argument(
    #    "-e", "--email", help="Email to Send to", required=True
    #)
    #args = parser.parse_args()
    #token = args.token
    #email = args.email

    output = cli.execute('show logging')
    #print(output)

    message = "**Alert:** Config Changed "+ output
    api = CiscoSparkAPI(access_token="ZTRlYTY5YjQtODMxNC00NDJhLWFmM2YtZmU5OGI0MDAxN2Y1MjEyNDg0YzYtZmFi")
    api.messages.create(toPersonEmail="sajustin@cisco.com", markdown=message)
