def detectcategory(subject):
    categorykeywords = {
    "Politics": ["President", "Politician", "Minister", "Government", "Leader", "Activist", "Union"],
    "Entertainment": ["Celebrity", "Actor", "Singer", "YouTube", "Influencer", "Chef", "Famous"],
    "Technology": ["Tech", "AI", "Robot", "Startup", "Scientist", "NASA", "Engineer"],
    "Sports": ["Football", "Athlete", "Stadium", "Superstar", "Champion", "Competition"],
    "Miscellaneous": ["Doctor", "Environmentalist", "Journalist", "Alien", "Billionaire", "Teacher", "Hacker"]
    }
    
    for category, keywords in categorykeywords.items():
        for keyword in keywords:
            if keyword.lower() in subject.lower(): #lower here represent if we write key word in small or capital letter it can easily compare that except case sensitivity.
                return category
    return "Miscellaneous"
