import json
import urllib.request
import time

#####################################################################
# Global variables to customize for your own donations.
participant_id = 196451
text_file_folders = ""
team_id = 27277
#####################################################################

# URLs to pull data
participant_info_url = "http://www.extra-life.org/index.cfm?fuseaction=donordrive.participant&participantID=" + str(participant_id) + "&format=json"
participant_donation_info_url = "http://www.extra-life.org/index.cfm?fuseaction=donordrive.participantDonations&participantID=" + str(participant_id) + "&format=json"
team_info_url = "http://www.extra-life.org/index.cfm?fuseaction=donorDrive.team&teamID=" + str(team_id) + "&format=json"


def write_to_text_file(data, filename):
    f = open(text_file_folders + filename, 'w')
    f.write(data)
    f.close()

def latest_donation(json):
    latest_donation_amount = str(json[0]['donorName'] + " - " + "$" + json[0]['donationAmount'])
    write_to_text_file(latest_donation_amount, "LastDonation.txt")

def top_donation(json):


def my_total_raised(json):


def team_total_raised(json):




while True:

    # Get the Participant Info JSON object
    participantInfoJSON = urllib.request.urlopen(participant_info_url)
    tmpParticipantInfoResponse = participantInfoJSON.read().decode('utf-8')
    participantInfoObj = json.loads(tmpParticipantInfoResponse)

    # Get the Participant Donation Info JSON object
    participantDonationInfoJSON = urllib.request.urlopen(participant_donation_info_url)
    tmpParticipantDonationInfoResponse = participantDonationInfoJSON.read().decode('utf-8')
    participantDonationInfoObj = json.loads(tmpParticipantDonationInfoResponse)

    # Get the Team Info JSON object
    teamInfoJSON = urllib.request.urlopen(team_info_url)
    tmpTeamInfoResponse = teamInfoJSON.read().decode('utf-8')
    teamInfoObj = json.loads(tmpTeamInfoResponse)

    # Write the data to our text files
    latestdonation(participantDonationInfoJSON)
    topdonation(participantDonationInfoJSON)
    mytotalraised(participantInfoJSON)
    teamtotalraised(teamInfoJSON)

    time.sleep(60)

    #print(participantInfoObj)

