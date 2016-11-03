import json
import urllib.request
import time

# Global variables to customize for your own donations.
participant_id = 196451
text_file_folders = ""
team_id = 27277

# Global variables used in logic for top donations and whether or not to play a sound file on a new donation.
current_top_donation = 0
is_dev = True


# URLs to pull data
participant_info_url = "http://www.extra-life.org/index.cfm?fuseaction=donordrive.participant&participantID=" + str(participant_id) + "&format=json"
participant_donation_info_url = "http://www.extra-life.org/index.cfm?fuseaction=donordrive.participantDonations&participantID=" + str(participant_id) + "&format=json"
team_info_url = "http://www.extra-life.org/index.cfm?fuseaction=donorDrive.team&teamID=" + str(team_id) + "&format=json"


def write_to_text_file(data, filename):
    if not is_dev:
        f = open(text_file_folders + filename, 'w')
        f.write(data)
        f.close()
    else:
        print(data)


def check_for_changes(data, filename):
    print("hi")


def latest_donation(json):
    latest_donation_amount = str(json[0]['donorName'] + " - $" + json[0]['donationAmount'])
    write_to_text_file(latest_donation_amount, "LastDonation.txt")
    donation_amount = int(json[0]['donationAmount'])
    donor_name = json[0]['donorName']
    top_donation(donor_name, donation_amount)


def top_donation(new_donor, new_donation):
    global current_top_donation
    if new_donation > current_top_donation:
        top_donation_string = new_donor + " - $" + str(new_donation)
        write_to_text_file(top_donation_string, 'TopDonation.txt')
        current_top_donation = new_donation


def my_total_raised(json):
    my_current_total = "$" + json('totalRaisedAmount')
    write_to_text_file(my_current_total, "MyTotalRaised.txt")


def team_total_raised(json):
    team_current_total = "$" + json('totalRaisedAmount')
    write_to_text_file(team_current_total, "TeamTotalRaised.txt")


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
    latest_donation(participantDonationInfoJSON)
    top_donation(participantDonationInfoJSON)
    my_total_raised(participantInfoJSON)
    team_total_raised(teamInfoJSON)

    time.sleep(60)



