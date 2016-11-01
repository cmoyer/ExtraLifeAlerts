import json
import urllib.request
import time

#####################################################################
# Global variables to customize for your own donations.
participantID = 196451
textFileFolders = ""
teamID = 27277
#####################################################################

# URLs to pull data
participantInfoURL = "http://www.extra-life.org/index.cfm?fuseaction=donordrive.participant&participantID=" + str(participantID) + "&format=json"
participantDonationInfoURL = "http://www.extra-life.org/index.cfm?fuseaction=donordrive.participantDonations&participantID=" + str(participantID) + "&format=json"
teamInfoURL = "http://www.extra-life.org/index.cfm?fuseaction=donorDrive.team&teamID=" + str(teamID) + "&format=json"


while True:

    # Get the Participant Info JSON object
    participantInfoJSON = urllib.request.urlopen(participantInfoURL)
    tmpParticipantInfoResponse = participantInfoJSON.read().decode('utf-8')
    participantInfoObj = json.loads(tmpParticipantInfoResponse)

    # Get the Participant Donation Info JSON object
    participantDonationInfoJSON = urllib.request.urlopen(participantDonationInfoURL)
    tmpParticipantDonationInfoResponse = participantDonationInfoJSON.read().decode('utf-8')
    participantDonationInfoObj = json.loads(tmpParticipantDonationInfoResponse)

    # Get the Team Info JSON object
    teamInfoJSON = urllib.request.urlopen(teamInfoURL)
    tmpTeamInfoResponse = teamInfoJSON.read().decode('utf-8')
    teamInfoObj = json.loads(tmpTeamInfoResponse)



    #print(participantInfoObj)

